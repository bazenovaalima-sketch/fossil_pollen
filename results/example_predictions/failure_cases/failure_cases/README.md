# Failure cases and model limitations

This folder presents representative examples where the model produced incorrect or sub-optimal predictions.
These cases are shown to highlight current limitations of the approach and to avoid selection bias.

## 1. Over-detection of *Pinus stomata*
In some images, the model repeatedly predicts *Pinus stomata* where no such pollen grain is present.
This likely results from morphological similarity between vesiculated debris and pinus air sacs,
combined with class imbalance in the training dataset.

## 2. False positive: *Chenopodiaceae* instead of *Artemisia*
In complex scenes with overlapping organic material, the model may incorrectly classify
*Artemisia* pollen as *Chenopodiaceae*.
This suggests sensitivity to partial occlusion and background artefacts.

## 3. False negative: missed pine pollen
In some cases, clearly visible pine pollen grains are not detected at all.
Possible reasons include unusual orientation, partial focus loss, or low local contrast.

These failure cases indicate that while the model performs well for abundant and morphologically
distinct taxa, further improvements are needed for robust performance under challenging imaging conditions.
