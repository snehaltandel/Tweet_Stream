import tweepy
from tweepy import StreamListener
import twitter_credentials
from tweepy import OAuthHandler
from tweepy import Stream
import json
auth = OAuthHandler(twitter_credentials.CONSUMER_KEY,twitter_credentials.CONSUMER_SECRET)
auth.set_access_token(twitter_credentials.ACCESS_TOKEN,twitter_credentials.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
class MyStreamListener(StreamListener):
	def on_status(self, status):
		pass
	def on_data(self, data):
		response = json.loads(data)
		entities = response['entities']['hashtags']
		hash_tags = []
		for i in entities:
			j = i['text']
			hash_tags.append(j)
			print(j)
		pass
stream_listener = MyStreamListener()
stream = Stream(auth=api.auth, listener=stream_listener)
hashtags = stream.filter(track=['#'])