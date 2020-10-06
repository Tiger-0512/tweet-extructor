from requests_oauthlib import OAuth1Session
import json
import sys


def getTweets(tweetIds):
    tweetIds = ','.join(list(map(str,tweetIds)))
    res = session.get(url, params = {'id':tweetIds})

    if res.status_code != 200:
        print ("Twitter API Error: %d" % res.status_code)
        sys.exit(1)

    resText = json.loads(res.text)
    data = {rt['id']:rt['text'] for rt in resText}
    return data


# example
CK = 'qLkAe6ah4y7SmAMZ52cypxjRd' # Consumer Key
CS = '6yOLEKQjbgwYLymxQjUs5po7TIl1NFwf1fPl7ViI78qUy5UTjV' # Consumer Secret
AT = '1310841057031016450-cQmvDuYFsQnqBPfYi9WISA9O4C9DD7' # Access Token
AS = 'uife0pioYknbHGRnpuPVljVjfLms1M6JlYw9fdvu3TSax' # Access Token Secert

session = OAuth1Session(CK, CS, AT, AS)

url = 'https://api.twitter.com/1.1/statuses/lookup.json'

tweet = getTweets('522413901439176704')
print(tweet)