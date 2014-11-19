import twitter
import os
import sys


class TwitterCmdLine(object):

    def __init__(self):

        consumer_key = os.environ.get('CONSUMER_KEY')
        consumer_secret = os.environ.get('CONSUMER_SECRET')
        access_token = os.environ.get('ACCESS_TOKEN')
        access_secret_token = os.environ.get('ACCESS_SECRET_TOKEN')
        self.api = twitter.Api(consumer_key=consumer_key,
                               consumer_secret=consumer_secret,
                               access_token_key=access_token,
                               access_token_secret=access_secret_token)

    def show_friends(self):

        friends_list = self.api.GetFriends()
        for friend in friends_list:
            print friend.name

if __name__ == '__main__':
    twitter_cmd = TwitterCmdLine()

    if sys.argv[1] == 'friends':
        twitter_cmd.show_friends()
