#!/usr/bin/env python3

import yaml, os
import choochoogen
from twython import Twython

fullpath = os.path.dirname(os.path.realpath(__file__))

config = yaml.load(open(fullpath + "/config.yaml"))

twitter_app_key = config['TEST_twitter_app_key']
twitter_app_secret = config['TEST_twitter_app_secret']
twitter_oauth_token = config['TEST_twitter_oauth_token']
twitter_oauth_token_secret = config['TEST_twitter_oauth_token_secret']

twitter = Twython(twitter_app_key, twitter_app_secret, twitter_oauth_token, twitter_oauth_token_secret)

tweet = choochoogen.maketrain()

twitter.update_status(status=tweet)
