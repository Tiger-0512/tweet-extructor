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
CK = 'xxx' # Consumer Key
CS = 'xxx' # Consumer Secret
AT = 'xxx' # Access Token
AS = 'xxx' # Access Token Secert

session = OAuth1Session(CK, CS, AT, AS)

url = 'https://api.twitter.com/1.1/statuses/lookup.json'

tweet = getTweets('522413901439176704')
print(tweet)