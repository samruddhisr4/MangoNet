try:
    import tensorflow as tf
    print(f"TensorFlow version: {tf.__version__}")
    
    # Test Keras
    from tensorflow.keras.preprocessing import image
    print("Keras preprocessing module imported successfully")
    
    # Test model loading capability
    from tensorflow.keras.models import load_model
    print("Keras models module imported successfully")
    
    print("All imports successful!")
except ImportError as e:
    print(f"Import error: {e}")
except Exception as e:
    print(f"Other error: {e}")