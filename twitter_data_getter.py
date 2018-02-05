from apscheduler.schedulers.blocking import BlockingScheduler

import tweepy, sys, json


reload(sys)
sys.setdefaultencoding("utf-8")

consumer_key = 'kSASEcTGMr44q3iyr2827OS9v'
consumer_secret = 'ncWvAjv4L49sFSDtKHGiRhJdWZ1ohdYeUeWor2rh2PMDxM11aq'
access_token_key = '834284345795964928-jT8SaAsE4sTT7W4Sb3ddZ2c9H0uMwbH'
access_token_secret = 'W8wO9VV7T2lgZNyZI4siJEGZVCdIpzxoqpbCUDeiOMPuc'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)
myApi = tweepy.API(auth)


def rest_query_ex1():
    print "hello Rajat"
    geo = "39.8282,-98.5795,2500mi"
    tweets = myApi.search(q="playstation", count=500, geocode= geo , result_type="recent")
    for tweet in tweets:
        print tweet.created_at, tweet.user.screen_name, tweet.text
        with open("Albany_AB.txt", 'a+') as files:
            files.write(tweet.text)
            files.write("\n")
        #fout.write(json.dumps(tweet) + '\n')
    print "----------------------------------------------------------"

scheduler = BlockingScheduler()
scheduler.add_job(rest_query_ex1, 'interval', seconds=360)
scheduler.start()