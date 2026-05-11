# Training

## Phase 1 — YOLOv8

```bash
python training/train_yolo.py --data /path/to/data.yaml --weights yolov8m.pt --epochs 100
```

Key augmentations: `degrees=180`, `flipud=0.5`, `hsv_s=0.7`, `hsv_v=0.6` — microscopy images can appear at any rotation and with varying stain intensity.

## Phase 2 — RT-DETR-L

| Setting | Value |
|---|---|
| Architecture | RT-DETR-L (310 layers, 32.0 M params, 103.5 GFLOPs) |
| Framework | Ultralytics 8.4.46 |
| Backend | PyTorch 2.10.0 + CUDA 12.8 |
| Hardware | Tesla T4 (14.9 GB) on Google Colab |
| Epochs | 100 |
| Wall-clock time | ~5 h |
| Input resolution | 640 × 640 |
| Validation split | 401 images / 546 instances |

The training notebook (`train_rtdetr.ipynb`) is meant to run on Google Colab with GPU. Drop the dataset (Ultralytics/YOLO format with a `data.yaml`) onto Drive and update the path at the top of the notebook.

For full metrics and a YOLO vs RT-DETR comparison see the [README](../README.md).
