from ultralytics import YOLO
from pathlib import Path

"""
Train YOLOv8 for fossil pollen detection.

Dataset:
- Latoriței sediment core (1101–1102 m)
- Annotated in Roboflow, exported in YOLOm8 format

Usage:
python training/train_yolo.py --data /path/to/data.yaml --project runs --name exp1
"""

import argparse


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--data", type=str, required=True, help="Path to data.yaml")
    p.add_argument("--weights", type=str, default="yolov8m.pt", help="Base model (e.g., yolov8n.pt, yolov8m.pt)")
    p.add_argument("--epochs", type=int, default=100)
    p.add_argument("--imgsz", type=int, default=640)
    p.add_argument("--batch", type=int, default=8)
    p.add_argument("--device", type=str, default="mps", help="mps (Mac), cpu, or cuda")
    p.add_argument("--project", type=str, default="runs/detect")
    p.add_argument("--name", type=str, default="pollen_project")
    return p.parse_args()


def main():
    args = parse_args()

    data_yaml = Path(args.data)
    if not data_yaml.exists():
        raise FileNotFoundError(f"data.yaml not found: {data_yaml}")

    model = YOLO(args.weights)

    model.train(
        data=str(data_yaml),
        epochs=args.epochs,
        imgsz=args.imgsz,
        batch=args.batch,
        device=args.device,
        project=args.project,
        name=args.name,
        # augmentations 
        degrees=180.0,
        flipud=0.5,
        hsv_s=0.7,
        hsv_v=0.6,
    )


if __name__ == "__main__":
    main()
