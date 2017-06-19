import tweepy, random
from secrets import *

auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)
api = tweepy.API(auth)

tweets = [
	"Hello, World! Are you ready for this?",
	"Nobody expects the Spanish Inquisition!",
	"And now for something completely different.",
	"Hey, Siri, what's the weather going to be like today? Whoops. Wrong app.",
	"Goodnight, all. Yes, I know it's early, but it's really time."
	]

tweet_num = random.randint(0, len(tweets) -1 )
api.update_status(tweets[tweet_num])