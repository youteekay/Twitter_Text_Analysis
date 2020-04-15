# Twitter_Text_Analysis
Text Analytics Of Cryptocurrency Tweets Using Sentiment Analysis

## Overview
The purpose of this project is to conduct an investigation into the online marketplace for cryptocurrency through analyzing tweets via text analytics. We analyzed 10,000 tweets over October 5th and 6th, 2018.

## Subject
Cryptocurrency has taken the world by storm in the last decade. For the sake of simplicity, we only analyzed tweets related to keywords 'Ethereum' and 'Bitcoin' seeing as they are the two most popular currencies out there.

## Objective
Through sentiment analysis of cryptocurrency tweets, we hope to differentiate between genuine traders (buyers, sellers) and scammers (bots, people) of the abovementioned cryptocurrencies on the twitter space. We hope to do this by categorizing the tweets based on objectivity and polarity

Please check report for in-depth discussion of the Same

# File Descriptions

#### stream_twitter_data.ipynb 
Downloading live tweets through twitter streaming API

#### preliminary_analysis.ipynb
Preliminary summary statistics on tweets

#### get_wordcloud.ipynb
Wordcloud generatio indicating most popular words with greater size indicating higher popularity

#### sentiment_analysis.ipynb
Sentiment analysis of the data

#### data_analytics.ipynb
Some basic insights that we extracted from the data

*Please update your API keys before running the code in credentials/twython_credentials.json
