# Usage

## Prerequisites

- Python 3.8+
- Packages in `requirements.txt`
- Data files: `training.csv`, `Testing.csv` in the repository root

## Running the Desktop App

```powershell
# From the repo root
python -m venv .venv
. .venv\Scripts\Activate.ps1
pip install -r requirements.txt
python ui.py
```

Select your symptoms, choose an algorithm (or Auto), and click Predict.

## Programmatic API

You can use the prediction functions from Python as well:

```python
from PEP import build_models, predict_symptoms

# Build models (cached after first call)
build_models(verbose=False)

# Predict with a list/set of symptoms
prediction = predict_symptoms({"itching", "skin_rash"}, algorithm="tree")
print(prediction)
```
