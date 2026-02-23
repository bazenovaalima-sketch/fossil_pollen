# Dataset description

This project uses microscope images of fossil pollen grains derived from sediment samples collected at the Latoriței site (Southern Carpathians, Romania). Samples originate from depths of 1101 and 1102 m and are interpreted as Late Glacial in age.

## Image data

- Total images: 2,025
- Image type: light microscope images
- Object type: pollen grains and non-pollen particles (e.g. charcoal)
- Task: multi-class object detection

Images were manually annotated using bounding boxes in Roboflow and exported in YOLO format.

## Annotations

- Total annotated objects: 2,770
- Annotation format: YOLO (bounding boxes)
- Each bounding box corresponds to a single pollen grain or particle.
- **32 taxonomic classes** after merging rare taxa at the family or functional group level
    
## Taxonomic strategy

The original annotation included a large number of pollen taxa with highly imbalanced class frequencies. To reduce classification ambiguity and ensure sufficient training samples per class, several rare or morphologically similar taxa were merged at the family or functional group level. After merging the final dataset contains 32 taxonomic classes used for model training:

- Acer  
- Alnus viridis  
- Apiaceae  
- Artemisia
- Asteraceae 
- Betula pendula  
- Botryococcus  
- Charcoal  
- Chenopodiaceae  
- Corylus  
- Cyperaceae  
- Equisetum  
- Ferns  
- Filipendula  
- Fraxinus  
- Gymnosperms  
- Juglans  
- Juniperus  
- Larix  
- Lycopodium   
- Others  
- Pediastrum boryanum  
- Pediastrum integrum  
- Picea  
- Pine  
- Pinus stomata  
- Plantago  
- Poaceae  
- Quercus  
- Rumex  
- Salix  
- Steraceae  

Merged groups include:
- Asteraceae (e.g. Achillea, Ambrosia, Senecio-type, Cirsium-type)
- Apiaceae (including Heracleum and Peucedanum)
- Ferns (e.g. Polypodium, Filicales, Botrychium)
- Gymnosperms (Ephedra types)
- Other rare taxa grouped into an "Others" class

This approach follows common palynological practice and preserves ecological interpretability while improving model robustness.

## Dataset availability

Due to file size constraints, raw microscope images are not stored in this repository. The dataset and annotations can be made available upon reasonable request or via an external data repository.
