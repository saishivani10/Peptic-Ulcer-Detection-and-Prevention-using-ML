# Deployment Guide

## Deploy to Streamlit Community Cloud

1. **Push this repository to GitHub** (if not already done):
   ```powershell
   git add .
   git commit -m "Add Streamlit web app for deployment"
   git push origin main
   ```

2. **Go to Streamlit Community Cloud**:
   - Visit: https://share.streamlit.io
   - Sign in with your GitHub account

3. **Create New App**:
   - Click "New app"
   - Repository: `saishivani10/Peptic-Ulcer-Detection-and-Prevention-using-ML`
   - Branch: `main`
   - Main file path: `streamlit_app.py`

4. **Deploy**:
   - Click "Deploy!"
   - Wait a few minutes for the build to complete
   - You'll get a public URL like: `https://peptic-ulcer-detection-xyz.streamlit.app`

## Alternative: Deploy GitHub Pages (Documentation Only)

Your current workflow deploys MkDocs documentation (not the interactive app) to:
- https://saishivani10.github.io/Peptic-Ulcer-Detection-and-Prevention-using-ML/

To trigger:
```powershell
git add .
git commit -m "Deploy docs to Pages"
git push origin main
```

Make sure Pages is enabled: Repo Settings → Pages → Source: GitHub Actions

## Note

- **Streamlit Cloud** = Interactive web app (actual GUI with predictions)
- **GitHub Pages** = Static documentation site (just info pages)

For the full interactive experience, use Streamlit Community Cloud.
