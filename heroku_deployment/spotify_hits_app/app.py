# Import necessary libraries
import os
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

# Flask Setup
app = Flask(__name__)

# Database Setup
from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '') or "sqlite:///spotify.sqlite"

# # Remove tracking modifications
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# from .models import popular_hit

# Create route that renders index.html template
@app.route("/")
def home():
    return render_template('index.html', text="Final Project")

if __name__ == "__main__":
    app.run(debug=True)