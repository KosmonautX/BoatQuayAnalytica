import tweepy
from textblob import TextBlob
key = 'baui93JzNSGkKQytDsYivLSlb'
secret = '66cy90H5v3iCWVPYSQkELIAVS1SU8ogNuLmuMRYkk1R7G307vs'

access_token = '3284166475-tIwgFGIbVjVHMcZxHrJsIlFImWLVtOBD2iTIfkY'
access_secret = 'B5wDTc7ZO6lKzIUKJ5yQmeOd5Jn86b1m1oOKjKf3Jijlb'
auth = tweepy.OAuthHandler(key, secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)
public_tweets = api.search('lee kuan yew')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
# polarity --> negativity vs positivity while subjectivity is factual vs opinion
