from ultralytics import YOLO
from pathlib import Path

"""
Run inference on a folder of unseen microscope images.

Usage:
python inference/predict_folder.py --weights best.pt --input NOT_SEEN --out predictions_run1 --conf 0.3
"""

import argparse


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--weights", type=str, required=True, help="Path to trained weights (best.pt)")
    p.add_argument("--input", type=str, required=True, help="Folder with images")
    p.add_argument("--out", type=str, default="predictions_run1", help="Output folder name (created inside input folder)")
    p.add_argument("--conf", type=float, default=0.3)
    p.add_argument("--device", type=str, default="mps")
    return p.parse_args()


def main():
    args = parse_args()

    weights = Path(args.weights)
    input_dir = Path(args.input)

    if not weights.exists():
        raise FileNotFoundError(f"Weights not found: {weights}")
    if not input_dir.exists() or not input_dir.is_dir():
        raise FileNotFoundError(f"Input folder not found: {input_dir}")

    out_dir = input_dir / args.out
    out_dir.mkdir(parents=True, exist_ok=True)

    model = YOLO(str(weights))

    model.predict(
        source=str(input_dir),
        save=True,
        conf=args.conf,
        device=args.device,
        project=str(input_dir),
        name=out_dir.name,
        exist_ok=True,
    )

    print(f"Done! Results saved to: {out_dir}")


if __name__ == "__main__":
    main()
