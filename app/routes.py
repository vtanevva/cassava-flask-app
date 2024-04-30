from flask import render_template, request
from .model import load_model, predict  # Assume these functions in your model.py
from app import app
from PIL import Image
import io

# Load your model
model = load_model('efficient.keras')



@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        image_file = request.files['image']
        if image_file:
            # Convert the FileStorage to a PIL Image
            image = Image.open(image_file.stream)
            prediction = predict(model, image)  # Now passing a PIL image
            return render_template('index.html', prediction=prediction)
        else:
            return "No image provided", 400
    return render_template('index.html')




# model = load_model('efficient.keras')

# @app.route('/predict', methods=['POST'])
# def make_prediction():
#     if request.method == 'POST':
#         # Process file upload
#         image_file = request.files['image']
#         image_path = os.path.join('path_to_save_image', image_file.filename)
#         image_file.save(image_path)
        
#         # Make prediction
#         result = predict(model, image_path)
#         return result