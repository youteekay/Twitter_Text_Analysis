from twython import TwythonStreamer
import sys
import json
import time
import os

tweets = []

class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'lang' in data and data['lang'] == 'en':
            tweets.append(data)
            print('tweet number - ', len(tweets), data['text'][:500])
        if len(sys.argv) >= 2:
            number_of_tweets = int(sys.argv[2])
        else:
            number_of_tweets = 1000
        if len(tweets) >= number_of_tweets:
            self.store_json()
            self.disconnect()

    def on_error(self, status_code, data):
        print(status_code, data)
        self.disconnect()

    def store_json(self):
        with open(os.path.join('downloaded_tweets/tweet_stream_{}_{}.json'.format(keyword, len(tweets))), 'w') as file:
            json.dump(tweets, file, indent=4)

if __name__ == '__main__':
    with open(os.path.join('credentials/twython_credentials.json'), 'r') as file:
        credentials = json.load(file)

    CONSUMER_KEY = credentials['CONSUMER_KEY']
    CONSUMER_SECRET = credentials['CONSUMER_SECRET']
    ACCESS_TOKEN = credentials['ACCESS_TOKEN']
    ACCESS_TOKEN_SECRET = credentials['ACCESS_TOKEN_SECRET']
    stream = MyStreamer(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    keyword = sys.argv[1]
    print('downloading tweets.......')
    stream.statuses.filter(track=keyword)
