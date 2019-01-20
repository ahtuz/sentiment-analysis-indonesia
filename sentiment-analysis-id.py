import tweepy
from textblob import TextBlob

# Step 1 - Authenticate
consumer_key= 'CONSUMER_KEY'
consumer_secret= 'CONSUMER_SECRET'

access_token='ACCESS_TOKEN'
access_token_secret='ACCESS_TOKEN_SECRET'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Step 2 - Retrieve Tweets
public_tweets = api.search(q=['CANDIDATE_NAME', 'DebatCapres2019'], count=100)

all_polarity = 0
for tweet in public_tweets:
    print(tweet.text)
#Step 3 - Perform Sentiment Analysis on Tweets
    analysis = TextBlob(tweet.text)
    an = analysis.translate(from_lang='id', to='en')
    print(an.sentiment)
    all_polarity += an.polarity

    print("")

#Step 4 - To Check Positive or Negative Sentiment from Overall Tweets
if (all_polarity/100 > 0):
    print(all_polarity/100)
    print("")
    print('Positive')
else:
    print(all_polarity/100)
    print("")
    print("Negative")