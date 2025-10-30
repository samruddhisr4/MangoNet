import os
from flask import Flask, request, jsonify, render_template, render_template, redirect, url_for
from werkzeug.utils import secure_filename
import numpy as np

# Try to import TensorFlow and Keras
try:
    import tensorflow as tf
    from tensorflow.keras.preprocessing import image
    TF_AVAILABLE = True
except ImportError:
    print("TensorFlow/Keras not available")
    TF_AVAILABLE = False
    tf = None
    image = None

app = Flask(__name__)

# Configure upload folder
UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Load your trained model (replace with your model path)
MODEL_PATH = 'mango_classification_model.h5'
model = None
if TF_AVAILABLE:
    try:
        model = tf.keras.models.load_model(MODEL_PATH)
    except Exception as e:
        print(f"Error loading model: {e}")
        model = None

# List of class names (replace with your actual classes)
CLASS_NAMES = ['Anwar Ratool', 'Chaunsa (Black)', 'Chaunsa (Summer Bahisht)', 'Chaunsa (White)', 'Dosehri', 'Fajri', 'Langra', 'Sindhri']

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/upload_page')
def upload_page():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(url_for('home'))
    file = request.files['file']
    if file.filename == '':
        return redirect(url_for('home'))
    if file:
        filename = secure_filename(file.filename or '')
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # Preprocess image
        if TF_AVAILABLE and image is not None:
            img = image.load_img(filepath, target_size=(224, 224))
            img_array = image.img_to_array(img)
            img_array = np.expand_dims(img_array, axis=0)
            img_array = img_array / 255.0

            # Predict
            if model is not None:
                prediction = model.predict(img_array)
                predicted_class = CLASS_NAMES[np.argmax(prediction)]
            else:
                predicted_class = "Model not loaded"
        else:
            predicted_class = "TensorFlow/Keras not available"

        return render_template('results.html', prediction=predicted_class, image_url=filepath)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)