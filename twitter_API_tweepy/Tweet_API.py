__author__ = "Dongjie Fan"

import tweepy
import cPickle as pickle

class tweets(object):
	"""docstring for ClassName"""
	def __init__(self):
		self.api_key = None
		self.api_secret = None
		self.access_token = None
		self.access_secret = None
		
		self.api = None

		self.Exclude_replies = True
		self.Include_rts = True
		self.Contributor_details = False
		self.Count = 200

		self.userList = []
		self.data = {}

	def get_api(self, API_KEY, API_SECRET):
		self.api_key = API_KEY
		self.api_secret = API_SECRET
		print self.api_key, self.api_secret

	def get_access(self, ACCESS_TOKEN, ACCESS_SECRET):
		self.access_token = ACCESS_TOKEN
		self.access_secret = ACCESS_SECRET

	def connect(self):
		if self.api_key and self.api_secret:
			auth = tweepy.OAuthHandler(self.api_key, self.api_secret)
			if self.access_token and self.access_secret:
				auth.set_access_token(self.access_token, self.access_secret)
			self.api = tweepy.API(auth)
			print "Sucsess"
		else:
			print "Fail"

	def get_userList(self, users):
		for user in users:
			self.userList.append(user)

	def covert_ID(self, userName):
		return self.api.get_user(userName).id

	def fetch_setting(self, Exclude_replies = True, Include_rts= True, Contributor_details = False, Count = 200):
		self.Exclude_replies = Exclude_replies
		self.Include_rts= Include_rts
		self.Contributor_details = Contributor_details
		self.Count = Count

	def fetch(self, userName):
		try:
			data = self.api.user_timeline(userName, count = 200, 
							exclude_replies = True, 
							include_rts= True, 
							contributor_details = False)
			print "{}: {}".format(userName, len(data))
			return data
		except:
			return []
			print "{}: {}".format(userName, len(data))

	def count(self):
		for user, data in self.data.iteritems():
			n = 0
			for i in xrange(len(data)):
				if data[i].coordinates:
					n += 1
			print "{}: {} -> {}".format(user, len(data), n)
	

	def fetch_all(self):
		for i in xrange(len(self.userList)):
			user = self.userList[i]
			self.data[user] = self.fetch(user)
			#print ("\r{}%".format(100.0*(i+1)/len(self.userList))),
		self.count()

	
	def save(self, fname="./data.p"):
		with open(fname, 'wb') as f:
			pickle.dump(self.data, f)
		print "Save"

if __name__ == '__main__':
    main() 









