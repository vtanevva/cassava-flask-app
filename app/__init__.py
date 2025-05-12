from flask import Flask
from flask_cors import CORS
from .routes import configure_routes

def create_app():
    app = Flask(__name__)  # Create the app inside the create_app function
    CORS(app)  # Enable CORS
    configure_routes(app)  # Configure routes
    return app
