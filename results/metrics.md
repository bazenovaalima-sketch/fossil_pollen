# Model performance

## Phase 1 — YOLOv8 (baseline)

Evaluated on the validation set: **328 images · 448 annotated instances**.

| Metric | Value |
|------|------:|
| Precision | 0.679 |
| Recall | 0.603 |
| mAP@0.50 | 0.620 |
| mAP@0.50–0.95 | 0.482 |

<details>
<summary>Per-class YOLO results</summary>

| Class | Images | Instances | Precision | Recall | mAP@50 | mAP@50–95 |
|---|---:|---:|---:|---:|---:|---:|
| all | 328 | 448 | 0.679 | 0.603 | 0.620 | 0.482 |
| Acer | 2 | 2 | 0.151 | 0.500 | 0.511 | 0.410 |
| Alnus viridis | 12 | 13 | 1.000 | 0.741 | 0.943 | 0.681 |
| Apiaceae | 10 | 10 | 1.000 | 0.854 | 0.914 | 0.692 |
| Artemisia | 46 | 52 | 0.902 | 0.923 | 0.942 | 0.707 |
| Betula pendula | 14 | 15 | 0.567 | 0.933 | 0.826 | 0.655 |
| Botryococcus | 3 | 3 | 0.000 | 0.000 | 0.256 | 0.242 |
| Charcoal | 33 | 35 | 0.705 | 0.943 | 0.892 | 0.627 |
| Chenopodiaceae | 17 | 17 | 0.847 | 0.979 | 0.971 | 0.711 |
| Corylus | 2 | 2 | 0.652 | 1.000 | 0.663 | 0.548 |
| Cyperaceae | 6 | 6 | 0.656 | 0.333 | 0.367 | 0.281 |
| Equisetum | 2 | 2 | 0.000 | 0.000 | 0.081 | 0.059 |
| Ferns | 21 | 22 | 0.886 | 0.709 | 0.833 | 0.632 |
| Filipendula | 1 | 1 | 1.000 | 0.000 | 0.045 | 0.032 |
| Fraxinus | 7 | 7 | 0.504 | 0.436 | 0.538 | 0.428 |
| Gymnosperms | 5 | 5 | 0.727 | 0.545 | 0.588 | 0.499 |
| Juglans | 3 | 3 | 1.000 | 0.000 | 0.191 | 0.153 |
| Juniperus | 3 | 3 | 1.000 | 0.000 | 0.129 | 0.129 |
| Larix | 1 | 1 | 1.000 | 0.000 | 0.083 | 0.066 |
| Lycopodium | 45 | 48 | 0.793 | 0.958 | 0.958 | 0.759 |
| Others | 3 | 3 | 0.475 | 0.333 | 0.350 | 0.315 |
| Pediastrum boryanum | 4 | 4 | 0.668 | 0.750 | 0.808 | 0.461 |
| Pediastrum integrum | 12 | 13 | 0.758 | 0.769 | 0.888 | 0.597 |
| Picea | 3 | 3 | 0.408 | 0.667 | 0.631 | 0.539 |
| Pine | 96 | 106 | 0.850 | 0.964 | 0.971 | 0.802 |
| Pinus stomata | 1 | 1 | 0.457 | 1.000 | 0.995 | 0.895 |
| Plantago | 2 | 2 | 0.640 | 0.919 | 0.828 | 0.630 |
| Poaceae | 48 | 49 | 0.744 | 0.959 | 0.906 | 0.726 |
| Quercus | 2 | 2 | 1.000 | 0.000 | 0.114 | 0.101 |
| Rumex | 4 | 4 | 0.451 | 1.000 | 0.674 | 0.572 |
| Salix | 9 | 9 | 0.554 | 0.667 | 0.600 | 0.445 |
| Steraceae | 5 | 5 | 0.641 | 0.800 | 0.718 | 0.546 |

</details>

---

## Phase 2 — RT-DETR-L (current)

Evaluated on the validation set: **401 images · 546 annotated instances**.  
Architecture: RT-DETR-L · 310 layers · 32.0 M params · 103.5 GFLOPs  
Training: 100 epochs · Tesla T4 (Google Colab) · ~5 h

| Metric | Value |
|------|------:|
| Precision | **0.811** |
| Recall | **0.734** |
| mAP@0.50 | **0.751** |
| mAP@0.50–0.95 | **0.590** |

<details>
<summary>Per-class RT-DETR results</summary>

| Taxon | Val Images | Instances | P | R | mAP50 | mAP50-95 |
|---|---:|---:|---:|---:|---:|---:|
| **all** | **401** | **546** | **0.811** | **0.734** | **0.751** | **0.590** |
| Aconitum | 2 | 2 | 0.904 | 0.500 | 0.495 | 0.495 |
| Alnus viridis | 15 | 16 | 0.928 | 0.802 | 0.866 | 0.665 |
| Apiaceae | 9 | 9 | 1.000 | 0.939 | 0.995 | 0.765 |
| Artemisia | 62 | 69 | 0.869 | 0.863 | 0.847 | 0.605 |
| Asteraceae | 6 | 6 | 0.967 | 0.833 | 0.835 | 0.644 |
| Betula pendula | 23 | 24 | 0.837 | 0.875 | 0.834 | 0.659 |
| Charcoal | 38 | 40 | 0.767 | 0.906 | 0.849 | 0.572 |
| Chenopodiaceae | 26 | 26 | 0.952 | 0.771 | 0.832 | 0.652 |
| Convolvulus | 2 | 2 | 0.452 | 0.500 | 0.495 | 0.446 |
| Cyperaceae | 8 | 8 | 0.960 | 0.125 | 0.127 | 0.101 |
| Fagus | 2 | 2 | 0.482 | 0.500 | 0.495 | 0.396 |
| Galium | 1 | 1 | 0.430 | 1.000 | 0.995 | 0.895 |
| Juniperus | 4 | 4 | 1.000 | 0.437 | 0.495 | 0.396 |
| Lycopodium | 74 | 79 | 0.954 | 0.987 | 0.984 | 0.762 |
| Other_pollen | 19 | 20 | 0.860 | 0.350 | 0.363 | 0.281 |
| Pediastrum boryanum | 6 | 6 | 0.626 | 0.566 | 0.679 | 0.486 |
| Pediastrum integrum | 14 | 14 | 0.767 | 0.571 | 0.753 | 0.496 |
| Picea | 3 | 3 | 0.738 | 1.000 | 0.913 | 0.780 |
| Pine | 123 | 138 | 0.901 | 0.942 | 0.959 | 0.800 |
| Pinus stomata | 1 | 1 | 0.885 | 1.000 | 0.995 | 0.895 |
| Poaceae | 56 | 57 | 0.821 | 0.860 | 0.868 | 0.676 |
| Rumex | 9 | 9 | 0.688 | 0.667 | 0.720 | 0.537 |
| Salix | 8 | 8 | 0.728 | 0.625 | 0.629 | 0.509 |
| Thalictrum | 2 | 2 | 0.940 | 1.000 | 0.995 | 0.646 |

</details>

---

## Summary

| Metric | YOLO (Phase 1) | RT-DETR-L (Phase 2) | Δ |
|---|---:|---:|---:|
| Precision | 0.679 | **0.811** | +0.132 |
| Recall | 0.603 | **0.734** | +0.131 |
| mAP@50 | 0.620 | **0.751** | +0.131 |
| mAP@50–95 | 0.482 | **0.590** | +0.108 |
