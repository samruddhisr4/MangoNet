# MangoNet
# MangoNet: VGG16-Based Deep Learning for Mango Classification

## Overview

**MangoNet** is a deep learning project that leverages transfer learning with the VGG16 architecture to classify mango varieties from images. The system is designed for practical deployment in agriculture, fruit markets, and processing facilities, enabling automated, accurate, and scalable mango sorting and grading.

## Features

- **Transfer Learning**: Utilizes pre-trained VGG16 for efficient feature extraction and classification.
- **Multi-Class Classification**: Supports identification of 8 mango varieties.
- **Data Augmentation**: Applies real-time augmentation to improve model robustness and prevent overfitting.
- **Web Application**: Includes a Flask-based web interface for easy image upload and prediction.
- **High Accuracy**: Achieves over 96% accuracy on the test set.

## Project Structure
![image](https://github.com/user-attachments/assets/73dabf67-20be-47f7-b8c5-2be71961a9f6)


## Dataset

- **Source**: [Kaggle - Mango Varieties Classification and Grading](https://www.kaggle.com/datasets/saurabhshahane/mango-varieties-classification)
- **Content**: 3,200+ images, 8 classes (varieties), organized in train/validation/test splits[1].

## Model Architecture

- **Base Model**: VGG16 (pre-trained on ImageNet, convolutional layers frozen)
- **Custom Layers**:
  - Flatten
  - Dense (256 units, ReLU)
  - Dropout (0.5)
  - Dense (8 units, Softmax)

## Training & Evaluation

- **Data Preprocessing**: Images resized to 224x224, normalized to [0,1], with augmentation for training.
- **Training**: 10 epochs, Adam optimizer, categorical cross-entropy loss.
- **Performance**:
  - **Validation Accuracy**: ~84%
  - **Test Accuracy**: ~96.7%
  - **Test Loss**: 0.159

## How to Run

1. **Clone the repository**
git clone https://github.com/samruddhisr4/MangoNet.git
cd MangoNet

2. **Install dependencies**
pip install -r requirements.txt

3. **Download the dataset**
- Download from Kaggle and place in the appropriate directory (`/Dataset/Classification_dataset`).

4. **Train the model (optional)**
- Run `mangonet.ipynb` to reproduce model training and evaluation.

5. **Start the web app**
python app.py
- Open your browser and go to `http://127.0.0.1:5000`

## Usage

- Upload a mango image via the web interface.
- The model predicts the variety and displays the result with the image.

## Example Results

- **Validation Accuracy**: 84%
- **Test Accuracy**: 96.7%
- **Sample Prediction**: User uploads an image, receives the predicted mango variety with high confidence.

## Applications

- **Agricultural Sorting**: Automate classification and packaging at farms.
- **Market Grading**: Grade and display mangoes by variety and ripeness in markets.
- **Processing Quality Control**: Detect defects and ensure consistency during processing.

## Limitations

- Model performance depends on the quality and diversity of the training data.
- May misclassify images with severe occlusion or poor lighting.

## Future Work

- Expand dataset with more varieties and real-world images.
- Explore advanced architectures (EfficientNet, attention models).
- Deploy on edge devices for real-time, in-field use.

## License

This project is licensed under the MIT License.

---

**Project maintained by [Samruddhi SR](https://github.com/samruddhisr4/MangoNet)**

References:
mangonet.ipynb (see for code and training details)
