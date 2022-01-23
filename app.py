# Import necessary libraries
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
import numpy as np
import joblib
from flask import (
    Flask,
    render_template,
    request)

# Flask Setup
app = Flask(__name__)

# Database Setup
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///spotify.sqlite"

# # Remove tracking modifications
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# engine = db.create_engine(app.config['SQLALCHEMY_DATABASE_URI'], {})

model = joblib.load(open("random_forest.joblib", 'rb'))
loaded_scaler = joblib.load(open("scaler_model.joblib", 'rb'))

@app.route("/")
def home():
    predict_list_df = {}
    predict_list_df["acousticness"] = 0.185
    predict_list_df["danceability"] = 0.230
    predict_list_df["energy"] = 0.765
    predict_list_df["instrumentalness"] = 0.925
    predict_list_df["liveness"] = 0.250
    predict_list_df["loudness"] = -24.0
    predict_list_df["speechiness"] = 0.770
    predict_list_df["tempo"] = 48.0
    predict_list_df["valence"] = 0.190
    return render_template('index.html', predict_list_df=predict_list_df)


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
        # Get values from form and put them in a dictionary
        to_predict_list = request.form.to_dict()
        # Turn dictionary into a DataFrame
        predict_list_df = pd.DataFrame([to_predict_list.values()], columns=to_predict_list.keys())
        predict_list_df.drop(["genre"], axis=1, inplace=True)
        # Make a copy of the DataFrame
        predict_list_df_copy = predict_list_df.copy()
        # Get columns to be scaled
        col_names = ['loudness', 'tempo']
        features = predict_list_df_copy[col_names]
        # Use loaded scaler object to fit and transform values
        features = loaded_scaler.transform(features.values)
        # Put scaled values into the DataFrame
        predict_list_df_copy[col_names] = features
        # Use ValuePredictor function to make prediction from RandomForest Model
        prediction = ValuePredictor(predict_list_df_copy)
        print(predict_list_df['acousticness'])
        print(predict_list_df_copy)
        print(prediction)
        hit = ""
        if prediction == 1.0:
            prediction = 'This Song is a Hit!'
            hit = "hit"
        else:
            prediction = 'This Song is Not a Hit!'
            hit = "no-hit"
        return render_template("index.html", prediction_text=prediction, hit=hit, predict_list_df=to_predict_list)

def ValuePredictor(to_predict_list):
    result = model.predict(to_predict_list)
    print(result)
    return result[0]

if __name__ == "__main__":
    app.run(debug=True)
