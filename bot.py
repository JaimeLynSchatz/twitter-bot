import tweepy, random, schedule, time, markovify, sys
from secrets import *
from tweepy import API

auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)
api = tweepy.API(auth)

def make_friends():
	for follower in tweepy.Cursor(api.followers).items():
		follower.follow()

def rand_edison_tweet():
	with open("edison.txt") as f:
		text = f.read()
	text_model = markovify.Text(text)
	tweet = (text_model.make_short_sentence(140))
	f.close()
	api.update_status(tweet)

def rand_subway_tweet():
	with open("subway.txt") as f:
		text = f.read()
	text_model = markovify.Text(text)
	tweet = (text_model.make_short_sentence(140))
	f.close()
	api.update_status(tweet)

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
		"Discovery",
		"DiscoverMag",
		"ScienceNews",
		"WIRED",
		"SpaceX",
		"WorldAndScience"
		]

	selected_user = random.choice(users)
	print(selected_user)
	return selected_user

def timed_tweets():
	if random.randint(0, 1) == 1:
		print("going to retweet edupunk")
		retweet_edu()
	elif random.randint(0, 1) == 1:
		print("going to randomly tweet")
		if random.randint(0, 1) == 1:
			rand_edison_tweet()
		else:
			rand_subway_tweet()
	else:
		print("going to pull a name out of a hat and retweet them")
		retweet_user(new_user())

print("Scheduled twitter bot tweets starting")
schedule.every(77).minutes.do(timed_tweets)
#schedule.every(1).minutes.do(print("yo"))

while True:
	schedule.run_pending()
	time.sleep(1)
#make_friends()

# retweet_user(new_user())

# for status in api.user_timeline('edupunkn00b'):
# 	api.retweet(status.id)
# 	break
