# fossil_pollen

Deep learning–based object detection of fossil pollen grains in microscope images using YOLO.

## Overview

This repository contains code and documentation for a deep learning approach to automatically detect and classify fossil pollen grains in microscope images. The aim of the project is to support semi-automated pollen identification in palynological studies, particularly in contexts where manual counting is time-consuming and taxonomic ambiguity is high.

The dataset is derived from sediment samples collected at the Latoriței site (Southern Carpathians, Romania) at depths of 1101–1102 m, corresponding to the Late Glacial period.

## Dataset

- Total images: 2,025 microscope images
- Total annotated objects: 2,770
- Annotation type: bounding boxes (YOLO format)
- Annotation tool: Roboflow
- Task: multi-class object detection

Due to strong class imbalance and morphological similarity between taxa, several rare pollen types were merged at the family or functional group level. Details of the dataset and taxonomic merging strategy are provided in `data/README.md`.

## Method

The model is based on the YOLO (You Only Look Once) object detection framework. Training and inference were performed using the Ultralytics YOLO implementation.

Key characteristics:
- Multi-class pollen detection
- Family-level merging for rare taxa
- Evaluation on unseen microscope images

## Repository structure

```text
fossil_pollen/
├── training/    # YOLO training scripts
├── inference/   # Inference on unseen images
├── data/        # Dataset documentation
├── results/     # Evaluation metrics and example predictions
├── figures/     # Performance figures 
