# Final Project
# Spotify Hit Analysis

## Overview
### Selected topic  
We analyzed various features of 177,000 different Spotify tracks across genres to see which features are the most predictive in determining the popularity of the track. Tools, languages and libraries we will use include Python, Pandas, Flask, Tableau, AWS databases, PostGRE, among others. Our hope is to produce a web application that will share the findings, enabling a user to explore the data and enter characteristics to predict the popularity of a track.  

### Reason we selected the topic  
Both project participants are musicians. Regardless of the type of music we play or the instruments, we found the data set to be an interesting one for further study.  Are the various features of a track sufficient in helping to identify whether a song will be a hit?  

### Questions we hope to answer with the data
* What features are the most predictive in determining track popularity?
* What are the optimal combination of features for popular tracks?
* Are there any differences across genres?

## Description of the Communication Protocols  
Our group will meet regularly during class times (Tuesdays and Thursdays from 7 to 9 pm), will decide upon separate tasks for completion, and will contact each other as needed via Slack.

## Participants  
Project produced in January 2022 by Elle Jacobs and Vince Chandler.

## Data Source  
Data was sourced from kaggle.com and includes 232,725 various tracks from the Spotify API.  Data was compiled by internet user Zaheen Hamidani and includes approximately 10,000 tracks per genre.  CSV file is located in this repository, as well as here: https://www.kaggle.com/zaheenhamidani/ultimate-spotify-tracks-db

Raw data features include (explanation from [Spotify Developer Documentation](https://developer.spotify.com/documentation/web-api/reference/#/operations/get-audio-features)):
* Popularity: A measure from 0 to 100 calculated by algorithm and is based, in the most part, on the total number of plays the track has had and how recent those plays are. Generally speaking, songs that are being played a lot now will have a higher popularity than songs that were played a lot in the past.
* Acousticness: A confidence measure from 0.0 to 1.0 of whether the track is acoustic. 1.0 represents high confidence the track is acoustic.
* Danceability: Danceability describes how suitable a track is for dancing based on a combination of musical elements including tempo, rhythm stability, beat strength, and overall regularity. A value of 0.0 is least danceable and 1.0 is most danceable.
* Duration_ms: The duration of the track in milliseconds.
* Energy: Energy is a measure from 0.0 to 1.0 and represents a perceptual measure of intensity and activity. Typically, energetic tracks feel fast, loud, and noisy. 
* Instrumentalness: Predicts whether a track contains no vocals. "Ooh" and "aah" sounds are treated as instrumental in this context. Rap or spoken word tracks are clearly "vocal". The closer the instrumentalness value is to 1.0, the greater likelihood the track contains no vocal content. 
* Key: The key the track is in. Integers map to pitches using standard Pitch Class notation. E.g. 0 = C
* Liveness: Detects the presence of an audience in the recording. Higher liveness values represent an increased probability that the track was performed live. A value above 0.8 provides strong likelihood that the track is live.
* Loudness: The overall loudness of a track in decibels (dB). Loudness values are averaged across the entire track and are useful for comparing relative loudness of tracks. Loudness is the quality of a sound that is the primary psychological correlate of physical strength (amplitude). Values typically range between -60 and 0 db.
* Mode: Mode indicates the modality (major or minor) of a track, the type of scale from which its melodic content is derived. Major is represented by 1 and minor is 0.
* Speechiness: Speechiness detects the presence of spoken words in a track. The more exclusively speech-like the recording (e.g. talk show, audio book, poetry), the closer to 1.0 the attribute value. 
* Tempo: The overall estimated tempo of a track in beats per minute (BPM). In musical terminology, tempo is the speed or pace of a given piece and derives directly from the average beat duration.
* Time_signature: An estimated time signature. The time signature (meter) is a notational convention to specify how many beats are in each bar (or measure). The time signature ranges from 3 to 7 indicating time signatures of "3/4", to "7/4".
* Valence: A measure from 0.0 to 1.0 describing the musical positiveness conveyed by a track. Tracks with high valence sound more positive (e.g. happy, cheerful, euphoric), while tracks with low valence sound more negative (e.g. sad, depressed, angry).

## Data Exploration  
In our first pass of examining the data, we used Python code to examine the records.  For example, we examined how many tracks were in each type of genre, which ones were underrepresented? Which features likely had no bearing on whether it was a hit (such as key or tempo)?  How many tracks could be removed from various genres that were not likely to be musical “hits” such as comedy?  By using .value_counts(), we were able to answer many of these types of basic questions.  We also got the preliminary ranges of possible values for each feature, to help us decide whether scaling was needed in the machine learning phase.
We also used Tableau to graph out some early relationships between various features.  

## Analysis Phase  
Analysis will begin with ETL, as outlined in the Machine Learning Preprocessing.  Once the data is ready, it will be outlined using a Random Forest Machine Learning model to help identify which features can help predict whether the track will be a hit.  We will also produce graphs using Tableau to compare features against each other to see if any trends emerge.  Finally, we will put the data onto a Heroku/Flask app to enable users to interact and complete their own analysis.  

# Machine Learning Preprocessing  
For the ETL phase:  
1. Import raw CSV file into Pandas dataframe
2. Convert popularity from 0-100 scale to a ‘1’ if >= 50 (a “hit”) or ‘0’ if < 50.
3. Drop rows that belong to genres: a capella, comedy, anime or children’s music.
4. Cluster and relabel similar genres to reduce number down to 12
5. Drop old genre column along with key, mode, duration, and time signature.
6. Separate artist name, track name, and track id into a new dataframe
7. Load track feature dataframe into sqlite table (“songs”) and artist/track name into table (“trackinfo”)

## Machine Learning: Feature Engineering/Selection
* We removed key, mode, and time signature.  As musicians, we decided these features are interesting but would likely have no impact on hit status. 
* Knowing we would one-hot encode the genres, we decided to pare down the number of possibilities to reduce the number of columns.
* We also separated out artist/track name into a separate table since they were string data types and had no impact on the analysis.
* Loudness and tempo were the only two fields that contained numbers outside the range of 0-1, so those were scaled using StandardScaler from sklearn.
* All features entered were of similar importance, according to a feature_importances check, with values from .087 to .007 (which was a genre, so we kept it).

## Machine Learning: Training and Testing Sets  
Once the data was processed and scaled, we separated out the “hit” column as our y values, and everything else (minus “hit” and “track_id”) as our X values.
We utilized train_test_split from sklearn to create our four sets of data (X train, X test, y train, y test).  This is the data that we ran through two models: logistic regression and random forest.  

## Machine Learning: Model Choice  
* We examined the results from two different models- logistic regression and random forest
* Both produced similar results, but Random Forest (with 128 estimators) was slightly better:
![image](https://user-images.githubusercontent.com/88070999/150053609-e95abcf8-838a-42ac-8a81-5d90990348ae.png)  
* A Random Forest model might miss some variability in the features that a deep learning model might incorporate. On the plus side, however, Random Forest models are good against overfitting the data and handling many features (such as the many genre features that resulted from one-hot encoding.

## Dashboard
Tools used:
* HTML
* JS
* CSS
* Tableau
* Flask
* Heroku
* Joblib
* SQLAlchemy  
![image](https://user-images.githubusercontent.com/88070999/150053738-9ac3a2d6-5ce0-45e5-bb3a-df045e6672f0.png)  

## Database ERD  
![image](https://user-images.githubusercontent.com/88070999/150053963-69b74956-1648-4650-a74c-e4c84627a890.png)  

## Link to dashboard  
Link to dashboard

## Link to Google Slides presentation  
Link: <https://docs.google.com/presentation/d/1kwEtQHDsI_Bbk9MUEEXVeWJwBLRltwzRfAXhaxI8z7U/edit#slide=id.g10d4f5c8827_0_0>


