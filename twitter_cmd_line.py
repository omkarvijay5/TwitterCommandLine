import twitter
import os
import sys
import re

class TwitterCmdLine(object):
    
    #Twitter Api initialization
    def __init__(self):
        consumer_key = os.environ.get('CONSUMER_KEY')
        consumer_secret = os.environ.get('CONSUMER_SECRET')
        access_token = os.environ.get('ACCESS_TOKEN')
        access_secret_token = os.environ.get('ACCESS_SECRET_TOKEN')
        
        #Enter the access tokens if no token exists
        if not consumer_key or not consumer_secret or \
           not access_token or not access_secret_token:
            consumer_key = raw_input("please enter your twitter consumer key")
            consumer_secret = raw_input("Please enter your twitter consumer secret")
            access_token = raw_input("Please enter your twitter access token")
            access_secret_token = raw_input("Please enter your twitter secret token")
        self.api = twitter.Api(consumer_key=consumer_key,
                               consumer_secret=consumer_secret,
                               access_token_key=access_token,
                               access_token_secret=access_secret_token)

    #Displays all the friends list
    def show_friends(self):
        friends_list = self.api.GetFriends()
        for friend in friends_list:
            print friend.name
    
    def show_timeline_tweets(self, tweet_number):
        pass

if __name__ == '__main__':
    twitter_cmd = TwitterCmdLine()
    try:
        twitter_cmd.api.VerifyCredentials()
        
        tweet_number = re.match('\d+', sys.argv[1])

        if tweet_number:
            tweet_number = tweet_number.group(0)
            twitter_cmd.show_timeline_tweets(tweet_number)

        #python twitter_cmd_line.py friends will display friends
        if sys.argv[1] == 'friends':
            twitter_cmd.show_friends()


    except twitter.TwitterError as errors:
        print errors.message[0]['message']
