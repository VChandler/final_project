# Import necessary libraries
from flask_sqlalchemy import SQLAlchemy
import sys
import pandas as pd
import sklearn as sklearn
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import make_pipeline
import numpy as np
import joblib
import pickle
import os
from flask import (
    Flask,
    render_template,
    jsonify,
    request)

# Flask Setup
app = Flask(__name__)

# Database Setup
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///spotify.sqlite"

# # Remove tracking modifications
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# engine = db.create_engine(app.config['SQLALCHEMY_DATABASE_URI'], {})

model = joblib.load(open("../../random_forest.joblib", 'rb'))
loaded_scaler = joblib.load(open("../../scaler_model.joblib", 'rb'))

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

        return render_template("index.html", feature=feature, prediction_text='Hit or Not?: '.format(prediction))

    # return render_template("index.html", feature=feature)


@app.route('/test', methods=['POST'])
def test():
    if request.method == 'POST':
        print("hello*****************")
        print(model)
        print(StandardScaler().fit_transform(model))
        to_predict_list = request.form.to_dict()
        # print(to_predict_list)
        predict_list_df = pd.DataFrame(
            [to_predict_list.values()], columns=to_predict_list.keys())
        print(predict_list_df)
        print(predict_list_df.shape)

        predict_list_df_copy = predict_list_df.copy()


        col_names = ['loudness', 'tempo']
        features = predict_list_df_copy[col_names]
        print(features.values)
        
        scaler = model.fit(features.values)
        # features = scaler.transform(features.values)
        print(scaler)
        predict_list_df_copy[col_names] = features
        
        print(predict_list_df_copy)

        song_data = scaler.fit(predict_list_df_copy)
        print(song_data)
        print("********************")
        prediction = ValuePredictor(song_data)
        print(prediction)
        

        return render_template("index.html", prediction_text=prediction)


def ValuePredictor(to_predict_list):
    result = model.predict(to_predict_list)
    return result[0]


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        print("hello****")
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        print(to_predict_list)
        result = ValuePredictor(to_predict_list)
        if int(result) == 1:
            prediction = 'This song is a hit'
        else:
            prediction = 'This song is not a hit'
        return render_template("index.html", prediction_text=prediction)


if __name__ == "__main__":

    app.run(debug=True)
