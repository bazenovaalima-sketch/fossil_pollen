# Figures

This folder contains **curated, publication-ready figures** summarizing the performance of the pollen and microfossil detection model.  
Only selected figures that provide clear scientific insight are included here; raw training outputs are stored elsewhere.

---

## 📊 Performance Figures

### 1. Normalized Confusion Matrix  
**File:** `confusion_matrix_normalized.png`

- Displays class-wise prediction performance normalized by true class frequency
- Highlights systematic misclassifications between morphologically similar taxa
- Used to interpret model behavior under class imbalance

This figure is the primary diagnostic tool for understanding classification errors.

---

### 2. Precision–Recall Curve (All Classes)  
**File:** `BoxPR_curve.png`

- Shows the global precision–recall trade-off across all taxa
- The area under the curve corresponds to the reported **mAP@0.5**
- Standard evaluation metric for object detection models

---

### 3. mAP per Taxon  
**File:** `map_per_class_bar.png`

- Bar plot of mean Average Precision (mAP) per taxonomic class
- Illustrates performance differences between well-represented and rare taxa
- Used to justify class merging and discuss dataset imbalance effects

---

## 🖼 Example Predictions

Representative annotated examples are included to provide qualitative validation of the model.

- **Two examples per class**
- Selected from the test set
- Illustrate typical detection quality and taxon-specific morphology

These figures complement quantitative metrics by showing how predictions appear in practice.
