import tweepy, random
from secrets import *
from tweepy import API

auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)
api = tweepy.API(auth)

def make_friends():
	for follower in tweepy.Cursor(api.followers).items():
		follower.follow()

def rand_tweet():
	tweets = [
		"Hello, World! Are you ready for this?",
		"Nobody expects the Spanish Inquisition!",
		"And now for something completely different.",
		"Hey, Siri, what's the weather going to be like today? Whoops. Wrong app.",
		"Goodnight, all. Yes, I know it's early, but it's really time."
		]

	tweet_num = random.randint(0, len(tweets) -1 )
	api.update_status(tweets[tweet_num])

def retweet_edu():
	statuses = api.user_timeline('edupunkn00b')
	tweet_id = random.randint(0, len(statuses) - 1)
	api.retweet(statuses[tweet_id].id_str)

#make_friends()

retweet_edu()

# for status in api.user_timeline('edupunkn00b'):
# 	api.retweet(status.id)
# 	break
