# Training

The model used in this project is **RT-DETR-L** from Ultralytics, fine-tuned on a custom annotated dataset of ~2,500 microscopy images covering 24 palynological taxa.

## Recipe

| Setting | Value |
|---|---|
| Architecture | RT-DETR-L (310 layers, 32.0 M params, 103.5 GFLOPs) |
| Framework | Ultralytics 8.4.46 |
| Backend | PyTorch 2.10.0 + CUDA 12.8 |
| Hardware | Tesla T4 (14.9 GB) on Google Colab |
| Epochs | 100 |
| Wall-clock time | ~5 hours |
| Input resolution | 640 × 640 |
| Validation split | 401 images / 546 instances |

## Final metrics (best checkpoint)

| Metric | Value |
|---|---:|
| Precision | 0.811 |
| Recall    | 0.734 |
| mAP@50    | 0.751 |
| mAP@50–95 | 0.590 |

See the per-class table and the full training curves in the top-level [README](../README.md).

## Reproducing

The training notebook (`train_rtdetr.ipynb`) is meant to be run on Google Colab with GPU. Drop your dataset (in YOLO/Ultralytics format with a `data.yaml`) onto Drive and update the path at the top of the notebook.
