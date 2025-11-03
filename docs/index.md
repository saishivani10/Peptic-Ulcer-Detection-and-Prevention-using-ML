# Peptic Ulcer Detection

Welcome to the project website. This site provides an overview, quickstart, and references.

> Note: The application is a desktop GUI (Tkinter) with scikit-learn models. GitHub Pages hosts static content only, so this site documents and showcases the project rather than running the app in-browser.

## Quick Links

- Repository README for full details
- Usage guide: see [Usage](usage.md)
- Model summary: see [Models](models.md)

## Features

- Predicts disease based on selected symptoms using Decision Tree, Random Forest, and Gaussian Naive Bayes
- "Auto" ensemble mode (in the UI) to suggest a robust prediction
- Clean GUI built with Tkinter

## How it works (high level)

- Training data is loaded from `training.csv` (and validated against `Testing.csv`)
- Symptoms are vectorized to a binary feature vector
- Models are trained once and reused on subsequent predictions
- Results include predicted disease and helpful notes/precautions (in the UI)

## Local Run (desktop UI)

1. Create a virtual environment and install requirements.
2. Run the UI script.

```bash
python -m venv .venv
. .venv/bin/activate  # Windows PowerShell: .venv\\Scripts\\Activate.ps1
pip install -r requirements.txt
python ui.py
```

## License & Disclaimer

- For research/education. Not a medical device.
- Always consult a professional for health advice.
