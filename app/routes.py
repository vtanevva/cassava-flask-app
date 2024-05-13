from flask import render_template, request, jsonify
from .model import load_model, predict
from PIL import Image

# This function needs to be adjusted to accept the app instance.
from werkzeug.utils import secure_filename
from PIL import Image
import os

def configure_routes(app):
    model = load_model('efficient.keras')

    @app.route('/', methods=['GET', 'POST'])
    def index():
        if request.method == 'POST':
            image_file = request.files.get('image')
            if image_file:
                # Ensure the file is an image
                if allowed_file(image_file.filename):
                    # Secure the filename and optionally save or directly predict
                    
                    image = Image.open(image_file.stream)
                    prediction = predict(model, image) 

                    messages = {
                        0: "Cassava Bacterial Blight (CBB)",
                        1: "Cassava Brown Streak Disease (CBSD)",
                        2: "Cassava Green Mottle (CGM)",
                        3: "Cassava Mosaic Disease (CMD)",
                        4: "Your Cassava plant is healthy :)"
                    }
                    message = messages.get(prediction, "Unknown prediction")
                    
                    
                    return render_template('index.html', message=message)
                else:
                    return "No image provided", 400
            else:
                return render_template('index.html', message=message)

        # GET request just returns a simple message or could be more complex data
        return render_template('index.html')
    
    def allowed_file(filename):
        return '.' in filename and \
               filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg', 'gif'}

# Ensure you have set '/path/to/save/images' to the correct path where you want to save images

    @app.route('/api/data')
    def get_data():
        return jsonify({"message": "Hello from Flask!"})
    
    @app.route('/data')
    def android_data():
        return jsonify({"message": "Data from Flask"})


