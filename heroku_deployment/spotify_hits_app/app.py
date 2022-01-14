# Import necessary libraries
import pandas as pd
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
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///spotify.sqlite"

# # Remove tracking modifications
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

engine = db.create_engine(app.config['SQLALCHEMY_DATABASE_URI'], {})

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
    print(request.form)
    print(feature)
    # hit = popular_hit(acousticness=acousticness, danceability=danceability, energy=energy, instrumentalness=instrumentalness, liveness=liveness, loudness=loudness, speechiness=speechiness, tempo=tempo, valence=valence)
    # db.session.add(hit)
    # db.session.commit()

    return render_template("index.html", feature=feature)



if __name__ == "__main__":
    app.run(debug=True)