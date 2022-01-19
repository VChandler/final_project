# Import necessary libraries
import pandas as pd
import numpy as np
import joblib
from joblib import dump , load
import os
from flask import (
    Flask,
    render_template,
    jsonify,
    request)

# Flask Setup
app = Flask(__name__)

# model_imported = tf.keras.models.load_model('model.h5')

# Database Setup
from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///spotify.sqlite"

# # Remove tracking modifications
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# engine = db.create_engine(app.config['SQLALCHEMY_DATABASE_URI'], {})

model = joblib.load("/Users/ellejacobs/projects/bootcamp/final_project/random_forest.joblib")

# Create route that renders index.html template
@app.route("/")
def home():
    # with engine.connect() as conn:
    #     df = pd.read_sql("SELECT * FROM songs", conn)
    #     html = df.to_html()
    # return html
    return render_template('index.html', feature={})


# Query the database and send the jsonified results
@app.route("/send", methods=["GET", "POST"])
def send():
    
    feature = {}
    feature["genre"] = request.form.get("genre")
    feature["acousticness"] = request.form.get("acousticness")
    feature["danceability"] = request.form.get("danceability")
    feature["energy"] = request.form.get("energy")
    feature["instrumentalness"] = request.form.get("instrumentalness")
    feature["liveness"] = request.form.get("liveness")
    feature["loudness"] = request.form.get("loudness")
    feature["speechiness"] = request.form.get("speechiness")
    feature["tempo"] = request.form.get("tempo")
    feature["valence"] = request.form.get("valence")
    # print(request.form)
    print(feature)
    # hit = Hit(acousticness=acousticness, danceability=danceability, energy=energy, instrumentalness=instrumentalness, liveness=liveness, loudness=loudness, speechiness=speechiness, tempo=tempo, valence=valence)
    # db.session.add(Hit)
    # db.session.commit()
    if request.method == 'POST':
        int_features = [float(input(x)) for x in request.form.values()]
        final_features = [np.array(int_features)]
        prediction = model.predict(final_features)

        return render_template("index.html", feature=feature, prediction_text = 'Hit or Not?: '.format(prediction))

    # return render_template("index.html", feature=feature)


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        int_features = [int(x) for x in request.form.values()]
        final_features = [np.array(int_features)]
        prediction = model.predict(final_features)

        return render_template("index.html", prediction_text = 'Hit or Not?: '.format(prediction))


if __name__ == "__main__":
    
    app.run(debug=True)