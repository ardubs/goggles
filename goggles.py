import tweepy
from tweepy import OAuthHandler
import random
import time
import webbrowser

#
# this function returns a connection to the twitter API, using credentials loaded from creds.txt
#
def getAPI(creds):
	auth = OAuthHandler(creds['consumer_key'], creds['consumer_secret'])
	auth.set_access_token(creds['access_token'], creds['access_token_secret'])

	api = tweepy.API(auth)
	return api

# start by loading twitter API credentials from creds.txt
creds = {}
with open('creds.txt', 'r') as file:
	creds = eval(file.read())

file.close()

# use our credentials to get an API connection
api = getAPI(creds)

# grab our user ID
myID = creds['myID']

# grab the list of everyone we follow
current = api.friends_ids()

# find someone who also follows us back
mutual = False
while not mutual:
	candidateID = random.choice(current)

	candidate = api.get_user(candidateID)
	relationship = api.show_friendship(source_id=myID, target_id=candidateID)

	if relationship[0].followed_by:
		mutual = True

# grab their screen name
handle = candidate.screen_name

# tell us who it is already
print "creating " + handle + " goggles"

# grab the list of everyone they're following
newids = []
counter = 0

for page in tweepy.Cursor(api.friends_ids, screen_name=handle).pages():
	print "grabbing page"
	newids.extend(page)
	if counter != 0:
		time.sleep(30)
	counter += 1

# generate the list's description
desc = "following " + handle + "'s timeline"

# the name of our list. change this to make a new list!
listName = "goggles"

# create a new list called 'goggles' with the generated description
goggles = api.create_list(name=listName, mode='public', description=desc)

# populate list; twitter lists are limited to 5,000 members,
# so grab a random sampling if necessary
if len(newids) <= 5000:
	for x, pal in list(enumerate(newids)):
		print "adding " + str(x)
		api.add_list_member(slug=listName, id=pal, owner_screen_name=myID)
else:

	random.shuffle(newids)
	for x, pal in list(enumerate(newids[0:5000])):
		print "adding " + str(x)
		api.add_list_member(slug=listName, id=pal, owner_screen_name=myID)

# we did it
print "complete"

url = "https://twitter.com" + goggles.uri
print url
webbrowser.open(url, new=2)  # 2 = open in a new tab, if possible
