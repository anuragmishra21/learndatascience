import tweepy
from textblob import TextBlob
consumer_key='HPrpicOGBiWUNKUE8iI5m3zmF'
consumer_secret='j9EMIV1LQzEMZTayxRLlzcoL9C3Df9oIhl6OGamx8ecKz6UKUT'

access_token='15026688-vt79S6sTaG8dHHGpnFGfhHubMIRUawKL2BDjz1CN4'
access_token_secret='zE3yIvxqTRJRqVOLxJYqmlr4vYYzTUt9n1fVis0NKRTTY'
auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api=tweepy.API(auth)
public_tweets=api.search('digvijai singh')
for tweet in public_tweets:
	print(tweet.text.encode("utf-8"))
	analysis=TextBlob(tweet.text)
	print(analysis.sentiment)