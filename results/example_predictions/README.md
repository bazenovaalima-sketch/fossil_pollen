# Example predictions

Representative examples of correct model predictions are provided in:
`results/example_predictions/`.

The examples demonstrate:
- Accurate detection and classification of common and abundant pollen taxa (e.g. Pine, Artemisia, Lycopodium, Poaceae)
- Correct identification of morphologically distinctive taxa (e.g. Pediastrum integrum, Alnus viridis)
- Robust performance in images containing multiple pollen types and non-pollen particles (e.g. charcoal)

## Model limitations

Example failure cases, including false positives and missed detections, are documented in  
`results/example_predictions/failure_cases/`.

These errors are mainly associated with:
- strong class imbalance,
- overlapping particles and organic debris,
- morphologically similar pollen types.

Future work should address these issues through additional training data,
class rebalancing, and improved annotation of ambiguous cases.
