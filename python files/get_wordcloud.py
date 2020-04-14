import os
import matplotlib.pyplot as plt
import wordcloud
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
import sys
import string
import json
import re
from wordcloud import WordCloud
import matplotlib.pyplot as plt

p = string.punctuation
d = string.digits

def clean_text(unclean_text):
    table_p = str.maketrans(p, len(p) * " ")
    table_d = str.maketrans(d, len(d) * " ")
    text_without_punctuation = unclean_text.translate(table_p)
    text_without_punctuation_numbers = text_without_punctuation.translate(table_d)
    return text_without_punctuation_numbers

stopwords = nltk.corpus.stopwords.words('english')
stopwords.append('might')
with open(os.path.join('downloaded_tweets/tweet_stream_{}_{}.json'.format(sys.argv[1], sys.argv[2])), 'r') as file:
    tweets = json.load(file)

excude_punctuation = set(string.punctuation)
exclude_digits = set(string.digits)
tweet_words_set = [ ]
for tweet in tweets:
    tweet_text = tweet['text']
    clean_tweet = clean_text(tweet_text)
    clean_tweet = re.sub(' +', ' ', clean_tweet)
    stopwords = nltk.corpus.stopwords.words('english')
    stopwords.append("RT")
    #print(stopwords)
    tweet_words = word_tokenize(clean_tweet)

text2 = ''
for word in tweet_words:
    if len(word) == 1 or word in stopwords:
        continue
    text2 += ' {}'.format(word)
wordcloud2 = WordCloud(max_font_size=40).generate(text2)
plt.figure()
plt.imshow(wordcloud2)
plt.axis('off')
plt.show()