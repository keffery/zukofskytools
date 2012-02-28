#!/usr/bin/env python
# -*- coding: latin-1 -*-
'''
Created on Feb 28, 2012

@author: leanother
'''

import tweepy
import cmd

#CONSTANTS
VERSION = '0.1'
AUTHOR = 'Eduardo Cruz'
auth = tweepy.OAuthHandler("hOfmzo8cdQoRD4GYkI4XCg", "LDzfw6X38jNGA5TBmHT7LZO7iEZ2qdhMJS52cYKrE")
#CONSTANTS


def get_version():
    return VERSION

def get_author():
    return AUTHOR

def get_api(verifier):
    auth.get_access_token(verifier)
    return tweepy.API(auth)

def get_url():
    return auth.get_authorization_url()

def get_me(api):
    return api.me().screen_name

def get_friends(api):
    friends = []
    for friend in tweepy.Cursor(api.friends).items():
            friends.append(friend.screen_name)
    return friends

def get_followers(api):
    followers = []
    for follower in tweepy.Cursor(api.followers).items():
            followers.append(follower.screen_name)
    return followers
        
