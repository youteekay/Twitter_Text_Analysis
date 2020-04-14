from collections import Counter
import nltk
import os
import sys
import json
from wordcloud import WordCloud
import datetime
import numpy as np
import matplotlib.pyplot as plt
from textblob import TextBlob as bl


def extract_locations(tweets, keyword):
    location_stopwords = ['Earth', 'Blockchain', 'Assist', 'assist', 'blockchain', 'Worldwide', 'City', 'city']
    locationset = ''
    for tweet in tweets:
        location = tweet['user']['location']
        if location is not None and location not in location_stopwords:
            locationset += ' {}'.format(location)
    wordcloud = WordCloud(max_font_size=40).generate(locationset)
    plt.figure()
    plt.imshow(wordcloud)
    plt.axis('off')
    plt.savefig(os.path.join('insights/{}_location.pdf'.format(keyword)))
    plt.show()
    
def selling_buying_recommendations(tweets, keyword):
    recommendation = {'selling' : 0, 'buying' : 0}
    for tweet in tweets:
        text = tweet['text']
        if 'sell' in text or 'selling' in text:
            recommendation['selling'] += 1
        elif 'buy' in text or 'buying' in text:
            recommendation['buying'] += 1
    #recommendation['selling'] = (recommendation['selling']/100000 * 100)
    #recommendation['buying'] = (recommendation['buying']/100000 * 100)
    plt.bar(range(len(recommendation)), recommendation.values(), align='center')
    plt.xticks(range(len(recommendation)), recommendation.keys(), rotation=25)
    plt.show()

def traders_scammers(tweets, keyword):
    traders = ['buy', 'sell', 'trade', 'finance', 'bull', 'bear', 'ledger', 'chart', 'cryptotrading', 'cryptotrader', 'daytrading']
    scammers = ['giveaway', 'airdrop', 'free', 'quick', 'earn', 'fast', 'limited', 'payment', 'opportunity']
    traders_tweets = []
    scammers_tweets = []
    for tweet in tweets:
        text = tweet['text']
        if any(x in text for x in traders):
            traders_tweets.append(tweet)
        if any(x in text for x in scammers):
            scammers_tweets.append(tweet) 
    traders_subj = []
    traders_pol = []
    scammers_subj = []
    scammers_pol = []
    for s in traders_tweets: 
        ss = bl(s['text'])
        traders_subj.append(ss.sentiment.subjectivity) 
        traders_pol.append(ss.sentiment.polarity) 
    for s in scammers_tweets: 
        ss = bl(s['text'])
        scammers_subj.append(ss.sentiment.subjectivity) 
        scammers_pol.append(ss.sentiment.polarity)
    plt.hist(traders_pol, bins=10) 
    plt.xlabel('traders_polarity score')
    plt.ylabel('tweet count')
    plt.grid(True)
    #plt.savefig('polarity.pdf')
    plt.show()
    plt.hist(traders_subj, bins=10) 
    plt.xlabel('traders_subjectivity score')
    plt.ylabel('tweet count')
    plt.grid(True)
    #plt.savefig('polarity.pdf')
    plt.show()
    plt.hist(scammers_pol, bins=10) 
    plt.xlabel('scammers_polarity score')
    plt.ylabel('tweet count')
    plt.grid(True)
    #plt.savefig('polarity.pdf')
    plt.show()
    plt.hist(scammers_subj, bins=10) 
    plt.xlabel('scammers_subjectivity score')
    plt.ylabel('tweet count')
    plt.grid(True)
    #plt.savefig('polarity.pdf')
    plt.show()     
    
    
    
'''
with open(os.path.join('downloaded_tweets/tweet_stream_bitcoin_10000.json'), 'r') as file:
    tweets = json.load(file)
    extract_locations(tweets, 'bitcoin')

with open(os.path.join('downloaded_tweets/tweet_stream_ethereum_10000.json'), 'r') as file:
    tweets = json.load(file)
    extract_locations(tweets, 'ethereum')   
    '''
'''
with open(os.path.join('downloaded_tweets/tweet_stream_bitcoin_10000.json'), 'r') as file:
    tweets = json.load(file)
    selling_buying_recommendations(tweets, 'bitcoin')
    '''
with open(os.path.join('downloaded_tweets/tweet_stream_bitcoin_10000.json'), 'r') as file:
    tweets = json.load(file)
    traders_scammers(tweets, 'bitcoin')
    
  