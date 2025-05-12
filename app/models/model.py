from keras.models import load_model
from keras.preprocessing.image import img_to_array, smart_resize
import numpy as np

# Load your trained model
model = load_model('efficient.keras')
model.summary()

def predict(model, img):
    img = img_to_array(img)  # Convert PIL image to a numpy array
    img = smart_resize(img, (224, 224))  # Resize image if needed
    img = np.expand_dims(img, axis=0)  # Add batch dimension
    prediction = model.predict(img)
    predicted_label = np.argmax(prediction, axis=1)[0]
    return predicted_label
