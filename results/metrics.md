# Model performance

## Overall performance

The model was evaluated on the validation set consisting of 328 microscope images and 448 annotated instances.

| Metric | Value |
|------|------:|
| Precision | 0.679 |
| Recall | 0.603 |
| mAP@0.50 | 0.620 |
| mAP@0.50–0.95 | 0.482 |

These metrics reflect the complexity of pollen morphology, strong class imbalance, and taxonomic similarity between several pollen types. Overall performance is sufficient for semi-automated pollen detection and relative abundance estimation.

---

## Per-class performance

Per-class evaluation metrics are reported below. Performance is highest for abundant and morphologically distinctive taxa (e.g. Pine, Lycopodium, Artemisia, Poaceae, Chenopodiaceae), while metrics for rare taxa with very few instances should be interpreted cautiously.

| Class               | Images | Instances | Precision | Recall | mAP@50 | mAP@50–95 |
| ------------------- | -----: | --------: | --------: | -----: | -----: | --------: |
| all                 |    328 |       448 |  0.679 | 0.603 |  0.620 |    0.482 |
| Acer                |      2 |         2 |  0.151 | 0.500 |  0.511 |    0.410 |
| Alnus viridis       |     12 |        13 |  1.000 | 0.741 |  0.943 |    0.681 |
| Apiaceae            |     10 |        10 |  1.000 | 0.854 |  0.914 |    0.692 |
| Artemisia           |     46 |        52 |  0.902 | 0.923 |  0.942 |    0.707 |
| Betula pendula      |     14 |        15 |  0.567 | 0.933 |  0.826 |    0.655 |
| Botryococcus        |      3 |         3 |  0.000 | 0.000 |  0.256 |    0.242 |
| Charcoal            |     33 |        35 |  0.705 | 0.943 |  0.892 |    0.627 |
| Chenopodiaceae      |     17 |        17 |  0.847 | 0.979 |  0.971 |    0.711 |
| Corylus             |      2 |         2 |  0.652 | 1.000 |  0.663 |    0.548 |
| Cyperaceae          |      6 |         6 |  0.656 | 0.333 |  0.367 |    0.281 |
| Equisetum           |      2 |         2 |  0.000 | 0.000 |  0.081 |    0.059 |
| Ferns               |     21 |        22 |  0.886 | 0.709 |  0.833 |    0.632 |
| Filipendula         |      1 |         1 |  1.000 | 0.000 |  0.045 |    0.032 |
| Fraxinus            |      7 |         7 |  0.504 | 0.436 |  0.538 |    0.428 |
| Gymnosperms         |      5 |         5 |  0.727 | 0.545 |  0.588 |    0.499 |
| Juglans             |      3 |         3 |  1.000 | 0.000 |  0.191 |    0.153 |
| Juniperus           |      3 |         3 |  1.000 | 0.000 |  0.129 |    0.129 |
| Larix               |      1 |         1 |  1.000 | 0.000 |  0.083 |    0.066 |
| Lycopodium          |     45 |        48 |  0.793 | 0.958 |  0.958 |    0.759 |
| Others              |      3 |         3 |  0.475 | 0.333 |  0.350 |    0.315 |
| Pediastrum boryanum |      4 |         4 |  0.668 | 0.750 |  0.808 |    0.461 |
| Pediastrum integrum |     12 |        13 |  0.758 | 0.769 |  0.888 |    0.597 |
| Picea               |      3 |         3 |  0.408 | 0.667 |  0.631 |    0.539 |
| Pine                |     96 |       106 |  0.850 | 0.964 |  0.971 |    0.802 |
| Pinus stomata       |      1 |         1 |  0.457 | 1.000 |  0.995 |    0.895 |
| Plantago            |      2 |         2 |  0.640 | 0.919 |  0.828 |    0.630 |
| Poaceae             |     48 |        49 |  0.744 | 0.959 |  0.906 |    0.726 |
| Quercus             |      2 |         2 |  1.000 | 0.000 |  0.114 |    0.101 |
| Rumex               |      4 |         4 |  0.451 | 1.000 |  0.674 |    0.572 |
| Salix               |      9 |         9 |  0.554 | 0.667 |  0.600 |    0.445 |
| Steraceae           |      5 |         5 |  0.641 | 0.800 |  0.718 |    0.546 |
