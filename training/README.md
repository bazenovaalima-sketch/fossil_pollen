# Training

## Phase 1 — YOLOv8

**Script:** `training/train_yolo.py`

```bash
python training/train_yolo.py --data /path/to/data.yaml --weights yolov8m.pt --epochs 100
```

### Augmentations

| Augmentation | Value | Reason |
|---|---|---|
| `degrees` | 180° | Pollen grains have no canonical orientation — any rotation is valid |
| `flipud` | 0.5 | Vertical flip is equally valid for microscopy images |
| `hsv_s` | 0.7 | Staining intensity varies between slides and sessions |
| `hsv_v` | 0.6 | Brightness varies with illumination and camera exposure |

---

## Phase 2 — RT-DETR-L

**Script:** `training/train_rtdetr.py`

```bash
# Google Colab (recommended — Tesla T4 required)
python training/train_rtdetr.py

# Local (comment out Colab-specific code first, set USE_COLAB = False)
python training/train_rtdetr.py --epochs 100
```

### Hardware & settings

| Setting | Value |
|---|---|
| Architecture | RT-DETR-L (310 layers, 32.0 M params, 103.5 GFLOPs) |
| Framework | Ultralytics 8.4.46 |
| Backend | PyTorch 2.10.0 + CUDA 12.8 |
| Hardware | Tesla T4 (14.9 GB) on Google Colab |
| Epochs | 100 (early stopping: patience 20) |
| Wall-clock time | ~5 h |
| Input resolution | 640 × 640 |
| Validation split | 401 images / 546 instances |

### Class imbalance and oversampling

The dataset is heavily imbalanced — Pine alone accounts for ~27 % of all annotations, while several taxa have fewer than 15 annotated instances in the entire dataset:

| Rare taxon | Training instances |
|---|---:|
| Aconitum | 11 |
| Convolvulus | 11 |
| Fagus | 11 |
| Galium | 10 |
| Juniperus | 15 |
| Picea | 10 |
| Pinus stomata | 16 |
| Thalictrum | 16 |

To address this, `train_rtdetr.py` applies **smart oversampling** before training starts: any training image that contains at least one rare-class annotation is duplicated **5×** with strong albumentations augmentations. This happens only on the training split; the validation set is never modified.

### Augmentations

Two layers of augmentation are applied:

**Layer 1 — oversampling pipeline (albumentations, rare classes only)**

Applied offline before training to generate 5 synthetic copies of each rare-class image:

| Transform | Parameters | Reason |
|---|---|---|
| `HueSaturationValue` | hue ±40, sat ±30, val ±20, p=0.8 | Stain colour and intensity vary between slide preparations |
| `GaussianBlur` | kernel (3–7), p=0.5 | Simulates slight focus drift at different stage positions |
| `GaussNoise` | std 0.1–0.3, p=0.3 | Mimics sensor noise from long-exposure microscopy captures |
| `RandomRotate90` | p=1.0 | Pollen orientation is arbitrary; all 90° rotations are valid |
| `HorizontalFlip` | p=0.5 | Symmetric taxa look identical when mirrored |
| `VerticalFlip` | p=0.5 | Same as above |

Bounding boxes are transformed together with the image using albumentations' YOLO-format `BboxParams`.

**Layer 2 — Ultralytics online augmentations (all classes, applied during training)**

| Augmentation | Value | Reason |
|---|---|---|
| `degrees` | 180° | Pollen has no canonical orientation |
| `flipud` | 0.5 | Valid symmetry for microscopy |
| `fliplr` | 0.5 | Valid symmetry for microscopy |
| `hsv_h` | 0.05 | Minor hue shift for colour robustness |
| `hsv_s` | 0.8 | Handles staining intensity variation |
| `mixup` | 0.1 | Regularises features and slightly helps minority classes |

### Google Drive backup

The script registers an `on_train_epoch_end` callback that copies `best.pt`, `last.pt`, and `results.csv` to Google Drive after every epoch, guarding against Colab runtime disconnections.

---

For full metrics and a YOLO vs RT-DETR comparison see the top-level [README](../README.md).
