import json
import os
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
import string
import string
import re
import sys
import operator
from pprint import pprint
from collections import Counter

p = string.punctuation
d = string.digits

def most_popular_words(tweets):
    excude_punctuation = set(string.punctuation)
    exclude_digits = set(string.digits)
    tweet_words_set = [ ]
    for tweet in tweets:
        tweet_text = tweet['text']
        clean_tweet = clean_text(tweet_text)
        clean_tweet = re.sub(' +', ' ', clean_tweet)
        tweet_words = word_tokenize(clean_tweet)
        tweet_words_set.extend(tweet_words)
    counter = Counter(tweet_words_set)
    return counter.most_common(10)    

def most_popular_without_stopwords(tweets):
    excude_punctuation = set(string.punctuation)
    exclude_digits = set(string.digits)
    tweet_words_set = [ ]
    for tweet in tweets:
        tweet_text = tweet['text']
        clean_tweet = clean_text(tweet_text)
        clean_tweet = re.sub(' +', ' ', clean_tweet)
        stopwords = nltk.corpus.stopwords.words('english')
        stopwords.extend(["RT", "co", "https", "We",  "https", "We", "via", "'", "’", "…", "I"])
        #print(stopwords)
        tweet_words = word_tokenize(clean_tweet)
        for word in tweet_words:
            if word not in stopwords:
                tweet_words_set.append(word)
    counter = Counter(tweet_words_set)
    return counter.most_common(10) 

def most_popular_hashtags(tweets):
    hashtags_set = [ ] 
    for tweet in tweets:
        hashtags = tweet['entities']['hashtags']
        for hashtag in hashtags:
            hashtags_set.append(hashtag['text'])
    counter = Counter(hashtags_set)
    return counter.most_common(10)  

def most_popular_user_mentions(tweets):
    user_mentions_set = [ ] 
    for tweet in tweets:
        mentions = tweet['entities']['user_mentions']
        for mention in mentions:
            user_mentions_set.append(mention['screen_name'])
    counter = Counter(user_mentions_set)
    return counter.most_common(10)  

def clean_text(unclean_text):
    table_p = str.maketrans(p, len(p) * " ")
    table_d = str.maketrans(d, len(d) * " ")
    text_without_punctuation = unclean_text.translate(table_p)
    text_without_punctuation_numbers = text_without_punctuation.translate(table_d)
    return text_without_punctuation_numbers

def frequent_tweeter(tweets):
    tweeter_set = [ ]
    for tweet in tweets:
        tweeter = tweet['user']['screen_name']
        tweeter_set.append(tweeter)
    counter = Counter(tweeter_set)
    return counter.most_common(1) 

def most_popular_tweet(tweets):
    popular_tweet_set = { }
    for tweet in tweets:
        tweet_id = tweet['id']
        quote_count = tweet['quote_count']
        retweet_count = tweet['retweet_count']
        reply_count = tweet['reply_count']
        favourite_count = tweet['favorite_count']
        try:
            quote_count += tweet['retweeted_status']['quote_count']
        except:
            quote_count = tweet['quote_count']
        try:
            retweet_count += tweet['retweeted_status']['retweet_count']
        except:
            retweet_count = tweet['retweet_count']
        try:
            reply_count += tweet['retweeted_status']['reply_count']
        except:
            reply_count = tweet['reply_count']
        try:
            favourite_count += tweet['retweeted_status']['favorite_count']
        except:
            favourite_count = tweet['favorite_count']
        tweet_score = quote_count + retweet_count + reply_count + favourite_count
        #print(tweet_score)
        popular_tweet_set[tweet_id] = tweet_score
    return max(popular_tweet_set.items(), key = operator.itemgetter(1))[0] 

with open(os.path.join('downloaded_tweets/tweet_stream_ethereum_10000.json')) as file:
    data = json.load(file)

most_popular_words = most_popular_words(data)
print('10 most popular words with stopwords')
print(most_popular_words)
most_popular_without_stopwords = most_popular_without_stopwords(data)
print('10 most popular words without stopwords')
print(most_popular_without_stopwords)
most_popular_hashtags = most_popular_hashtags(data)
print('10 most popular hashtags')
print(most_popular_hashtags)
most_popular_users = most_popular_user_mentions(data)
print('10 most popular users')
print(most_popular_users)
frequent_tweeter = frequent_tweeter(data)
print('The most frequently tweeting person (tweet author) about the keyword:')
print(frequent_tweeter)
most_popular_tweet = most_popular_tweet(data)
print('The most popular tweet is:')
print(most_popular_tweet)

