# Final Project
# Spotify Popularity Analysis

## Overview
### Selected topic  
We will be analyzing various features of 230,000 different Spotify tracks across genres to see which features are the most predictive in determining the popularity of the track.  Tools, languages and libraries we will use include Python, Pandas, Flask, Tableau, AWS databases, PostGRE, among others.  Our hope is to produce a web application that will share the findings and enable a user to enter characteristics to predict the popularity of a track.  

### Reason we selected the topic  
Both project participants are musicians.  Regardless of the type of music we play or the instruments, we found the data set to be an interesting one for further study.  

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
* Popularity: **?????**
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

## Provisional Machine Learning  
For our first pass, we are classifying 'popular' tracks as scored 50 or more.  Since this is a binary classification, we will start with a logistic regression model to see how effective it will be.  The provisional code for this is located in the 'import_clean' notebook on the 'vc' branch.

# Database  
Within the import_clean notebook, code is used to create our provisional database with SQL Alchemy.

## Findings  
TBD

## Link to app  
Link to dashboard (or link to video of dashboard demonstration)

## Link to Google Slides presentation  
Link: 
