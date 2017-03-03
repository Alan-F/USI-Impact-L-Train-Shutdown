__author__ = "Dongjie Fan"

import Tweet_API as tw 
import pandas as pd
import cPickle as pickle 

with open("./twitter_api.p", 'rw') as f:
	myAPI = pickle.load(f)

df = pd.read_pickle("./userInfo")
users= df.index.values[:23]

test = tw.tweets()
test.get_userList(users)
test.get_api(myAPI['API_KEY'], myAPI['API_SECRET'])
test.connect()
test.fetch_all()
test.save()

# Example Response: 
# https://dev.twitter.com/rest/reference/get/statuses/user_timeline




