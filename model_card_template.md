# Model Card
For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
This model was created by a student at Western Govenor's University taking a course on Machine Learning Operations from Udacity.
The model uses a random forest classifier.
## Intended Use
The intended use of this model is to predict whether the salary of someone is above or below 50,000 dollars per year

## Training Data
This model was trained on data from the US Census Bureau.

## Evaluation Data
This model was tested on data from the US Census Bureau.

## Metrics
_Please include the metrics used and your model's performance on those metrics._
The metrics for this model are Precision, Recall, and F1 score.
The model's performance on these metrics were as follows:
Precision: 0.7392 | Recall: 0.6065 | F1: 0.6663
The slice_output.txt file contains performance of model slices on these metrics.

## Ethical Considerations
The data used is from real people, though their names and faces are not included.

## Caveats and Recommendations
This model was trained on data from the United States, so the applications for those outside of the US will likely be limited.
