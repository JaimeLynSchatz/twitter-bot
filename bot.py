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
		"Goodnight, all. Yes, I know it's early, but it's really time.",
		"Sometimes, I just don't know what to say anymore.",
		"Wow, taking a deep dive into some tutorials. Need to come up for air!"
		]

	tweet_num = random.randint(0, len(tweets) -1 )
	api.update_status(tweets[tweet_num])

def retweet_edu():
	statuses = api.user_timeline('edupunkn00b')
	status = random.choice(statuses)
	print(status.id_str)
	api.retweet(status.id_str)

def retweet_user(user):
	#api.retweet(random.choice(api.user_timeline(user)).id)
	for status in api.user_timeline(user):
		api.retweet(status.id)
		break

def new_user():
	users = [
		"PopSci",
		"NASA_Technology",
		"SPACEdotcom",
		"WIREDScience",
		"NatGeo",
		"neiltyson",
		"JohnClease",
		"BarackObama",
		"CassiniSaturn",
		"MarsCuriosity",
		"stephenfry",
		"newscientist",
		"sciencemagazine",
		"Discovery"
		]

	selected_user = random.choice(users)
	print(selected_user)
	return selected_user



if random.randint(0, 1) == 1:
	print("going to retweet edupunk")
	retweet_edu()
elif random.randint(0, 1) == 1:
	print("going to randomly tweet")
	rand_tweet()
else:
	print("going to pull a name out of a hat and retweet them")
	retweet_user(new_user())

#make_friends()

# retweet_user(new_user())

# for status in api.user_timeline('edupunkn00b'):
# 	api.retweet(status.id)
# 	break
