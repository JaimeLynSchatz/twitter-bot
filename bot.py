import tweepy, random, schedule, time, markovify, sys, datetime
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
	tweet = (text_model.make_short_sentence(125))
	f.close()
	api.update_status(tweet + " #iHeartMars")

def rand_subway_tweet():
	with open("subway.txt") as f:
		text = f.read()
	text_model = markovify.Text(text)
	tweet = (text_model.make_short_sentence(120))
	f.close()
	api.update_status(tweet + " #iHeartNYCSubways")

def retweet_edu():
	print("About to retweet edupunk")
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
		"WorldAndScience",
		"montypython",
		"Python_Agent",
		"EduPunkN00b",
		"OpenSource4U",
		"WriteSpeakCode"
		]
	print("going to pull a name out of a hat and retweet them")
	selected_user = random.choice(users)
	print(selected_user)
	return selected_user

def rand_tweet():
	print("going to randomly tweet")
	if random.randint(0,1) == 1:
		rand_edison_tweet()
	else:
		rand_subway_tweet()

def timed_tweets():
	if random.randint(0, 1) == 1:
		retweet_edu()
	elif random.randint(0, 1) == 1:
		rand_tweet()
	else:
		retweet_user(new_user())

retweet_edu()

# rand_tweet()

print("Scheduled twitter bot tweets starting at " + str(datetime.datetime.now()))
schedule.every(47).minutes.do(timed_tweets)
schedule.every(58).minutes.do(rand_tweet)
#schedule.every(1).minutes.do(print("yo"))

while True:
	schedule.run_pending()
	time.sleep(1)
#make_friends()

# retweet_user(new_user())

# for status in api.user_timeline('edupunkn00b'):
# 	api.retweet(status.id)
# 	break
