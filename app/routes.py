from flask import render_template, request, jsonify
from .models.model import load_model, predict
from PIL import Image
from werkzeug.utils import secure_filename
import os

# Load model once when the app starts
model = load_model('efficient.keras')

def configure_routes(app):
    # Check for allowed file types
    def allowed_file(filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg', 'gif'}

    # Route to handle the image prediction
    @app.route('/api/predict', methods=['POST'])
    def predict_api():
        # Ensure the image is part of the request
        if 'image' not in request.files:
            return jsonify({"message": "No file part"}), 400
        
        file = request.files['image']

        # Check if file has a valid name and extension
        if file.filename == '' or not allowed_file(file.filename):
            return jsonify({"message": "No selected file or invalid format"}), 400

        # Ensure the filename is safe to use
        filename = secure_filename(file.filename)
        
        # Define the path to save the file
        uploads_dir = 'uploads'
        
        # Create the 'uploads' directory if it doesn't exist
        if not os.path.exists(uploads_dir):
            os.makedirs(uploads_dir)

        # Save the file
        file_path = os.path.join(uploads_dir, filename)
        file.save(file_path)  # Save file to the 'uploads' directory

        # Process the image
        image = Image.open(file_path)  # Open the image
        prediction = predict(model, image)  # Call your prediction function
        
        # Messages based on prediction results
        messages = {
            0: "Cassava Bacterial Blight (CBB)",
            1: "Cassava Brown Streak Disease (CBSD)",
            2: "Cassava Green Mottle (CGM)",
            3: "Cassava Mosaic Disease (CMD)",
            4: "Your Cassava plant is healthy :)"
        }

        message = messages.get(prediction, "Unknown prediction")
        
        # Return the result as JSON
        return jsonify({"message": message})
