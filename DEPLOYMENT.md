# Deployment Guide for MangoNet on Render

## Prerequisites
1. A Render account (https://render.com)
2. This repository pushed to GitHub

## Deployment Steps

1. **Go to Render Dashboard**
   - Visit https://dashboard.render.com

2. **Create New Web Service**
   - Click "New" > "Web Service"
   - Connect your GitHub repository
   - Select the branch to deploy (usually main)

3. **Configure Settings**
   - Name: MangoNet
   - Region: Choose the closest region
   - Branch: main
   - Root Directory: Leave empty (or set to MangoNet if needed)
   - Runtime: Python 3
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`

4. **Environment Variables**
   - Add these environment variables:
     - `MODEL_PATH`: /opt/render/project/src/mango_classification_model.h5
     - `UPLOAD_FOLDER`: /opt/render/project/src/static/uploads

5. **Python Version**
   - The project now uses Python 3.11.9 for compatibility
   - This is specified in `runtime.txt` and `.python-version` files

6. **Deploy**
   - Click "Create Web Service"
   - Wait for the build and deployment to complete

## Troubleshooting

### TensorFlow Version Issues
If you encounter TensorFlow version issues:
- Ensure requirements.txt specifies compatible versions
- Current working versions:
  - tensorflow==2.20.0
  - keras==2.13.1
  - protobuf==3.20.3

### Missing Model File
The application requires a trained model file:
1. Train the model using the provided Jupyter notebook
2. Save the model as `mango_classification_model.h5`
3. Place it in the root directory before deployment

### Import Errors
If you see import errors:
1. Check that all dependencies are listed in requirements.txt
2. Ensure compatible versions are used
3. Verify that the Python version on Render is compatible with your dependencies

### Python Version Issues
If you encounter Python version compatibility issues:
- The project now uses Python 3.11.9
- This version is compatible with TensorFlow 2.20.0
- Make sure your deployment environment uses Python 3.11.x

## Manual Deployment (if needed)

If automatic deployment fails:

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd MangoNet
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Train and save the model**
   - Run the Jupyter notebook to train the model
   - Save as `mango_classification_model.h5`

4. **Run locally to test**
   ```bash
   python app.py
   ```

5. **Deploy to Render manually**
   - Push all files including the model to GitHub
   - Redeploy on Render