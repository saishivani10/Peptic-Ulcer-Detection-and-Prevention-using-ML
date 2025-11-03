# Models

This project trains three scikit-learn classifiers:

- DecisionTreeClassifier
- RandomForestClassifier
- GaussianNB

Models are trained on `training.csv` with normalized symptom headers. Labels are normalized to avoid key errors. The Testing set is used for sanity checks.

The `build_models()` function builds and caches models for reuse; `predict_symptoms()` accepts a list/set of symptom names and returns the predicted disease as a string.
