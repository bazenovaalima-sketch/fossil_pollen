import subprocess
import shutil
from pathlib import Path
import numpy as np
import cv2
import time
import torch
import queue
import threading
from ultralytics import YOLO

"""
Real-time microscope inference using Ultralytics YOLO + FFmpeg (DirectShow) + OpenCV.

This script captures frames from a Windows DirectShow camera (e.g., microscope camera),
runs YOLO inference in real time, and displays annotated results with a smoothed FPS.

Requirements:
  - ffmpeg installed and available in PATH
  - Python packages: ultralytics, opencv-python, numpy, torch

Recommended repo layout:
  - Put this file at: inference/realtime_microscope.py
  - Place your trained weights as: best.pt (repo root), OR set WEIGHTS to an absolute path.
    (Tip: usually do NOT commit best.pt to GitHub unless you use Git LFS.)

How to find your camera name (Windows / DirectShow):
  Run in PowerShell or CMD:
    ffmpeg -list_devices true -f dshow -i dummy
  Then copy the exact device name into CAM_NAME (case-sensitive).

Run:
  python inference/realtime_microscope.py

Controls:
  - Press 'q' or ESC to quit.
"""

# Path to weights. Default expects best.pt in current working directory (repo root).
WEIGHTS = "best.pt"

# Windows DirectShow camera name. Must match `ffmpeg -list_devices true -f dshow -i dummy`
CAM_NAME = "EuromexCam"

# Resample AFTER capture (safer for some microscope camera drivers)
OUT_W, OUT_H = 960, 720
OUT_FPS = 20

# Inference settings
CONF = 0.30
IMGSZ = 640


def _check_requirements() -> None:
    """Fail fast with clear messages."""
    if shutil.which("ffmpeg") is None:
        raise RuntimeError(
            "ffmpeg not found in PATH. Install ffmpeg and ensure it is accessible from the command line."
        )

    if not Path(WEIGHTS).exists():
        raise FileNotFoundError(
            f"Weights file not found: {WEIGHTS}\n"
            "Place best.pt in the working directory or set WEIGHTS to an absolute path."
        )


def start_ffmpeg() -> subprocess.Popen:
    """Start FFmpeg to read raw BGR frames from the DirectShow camera into stdout."""
    vf = f"scale={OUT_W}:{OUT_H},fps={OUT_FPS},format=bgr24"
    cmd = [
        "ffmpeg",
        "-hide_banner",
        "-nostats",
        "-loglevel", "quiet",
        "-f", "dshow",
        "-rtbufsize", "256M",
        "-i", f"video={CAM_NAME}",
        "-vf", vf,
        "-pix_fmt", "bgr24",
        "-vcodec", "rawvideo",
        "-an",
        "-f", "rawvideo",
        "pipe:1",
    ]
    # IMPORTANT: stderr -> DEVNULL to avoid deadlocks from FFmpeg buffering logs
    return subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        bufsize=10**8
    )


def read_exact(stdout, nbytes: int):
    """Read exactly nbytes from stdout (raw video frame). Return None on EOF."""
    data = bytearray()
    while len(data) < nbytes:
        chunk = stdout.read(nbytes - len(data))
        if not chunk:
            return None
        data.extend(chunk)
    return bytes(data)


def main():
    _check_requirements()

    print("Torch:", torch.__version__)
    print("CUDA available:", torch.cuda.is_available())
    if torch.cuda.is_available():
        print("GPU:", torch.cuda.get_device_name(0))

    device = 0 if torch.cuda.is_available() else "cpu"

    model = YOLO(WEIGHTS)
    try:
        model.fuse()
    except Exception:
        # Not all models/backends support fuse; safe to ignore
        pass

    frame_bytes = OUT_W * OUT_H * 3
    pipe = start_ffmpeg()

    q = queue.Queue(maxsize=1)   # keep only latest frame to reduce latency
    stop = threading.Event()

    def reader():
        """Continuously read frames from FFmpeg stdout and keep only the newest frame."""
        while not stop.is_set():
            if pipe.stdout is None:
                stop.set()
                break

            raw = read_exact(pipe.stdout, frame_bytes)
            if raw is None:
                stop.set()
                break

            frame = np.frombuffer(raw, np.uint8).reshape((OUT_H, OUT_W, 3)).copy()

            # Keep only the latest frame (drop older frames if inference lags)
            if q.full():
                try:
                    q.get_nowait()
                except queue.Empty:
                    pass
            q.put(frame)

    t = threading.Thread(target=reader, daemon=True)
    t.start()

    # Warm up: wait for first frame and run one forward pass
    frame = q.get()
    _ = model.predict(
        source=frame,
        imgsz=IMGSZ,
        conf=CONF,
        device=device,
        half=(device != "cpu"),
        verbose=False
    )

    prev = time.time()
    fps_s = 0.0  # smoothed fps

    try:
        while not stop.is_set():
            try:
                frame = q.get(timeout=1.0)
            except queue.Empty:
                continue

            results = model.predict(
                source=frame,
                imgsz=IMGSZ,
                conf=CONF,
                device=device,
                half=(device != "cpu"),
                verbose=False
            )

            annotated = results[0].plot()

            now = time.time()
            fps = 1.0 / max(now - prev, 1e-6)
            prev = now
            fps_s = fps_s * 0.9 + fps * 0.1

            cv2.putText(
                annotated,
                f"FPS: {fps_s:.1f}",
                (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX,
                1.0,
                (0, 255, 0),
                2
            )

            cv2.imshow("Microscope YOLO (real-time)", annotated)
            key = cv2.waitKey(1) & 0xFF
            if key in (ord("q"), 27):  # q or ESC
                break

    finally:
        stop.set()
        try:
            pipe.terminate()
        except Exception:
            pass
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
