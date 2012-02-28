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
#CONSTANTS


def get_version():
    return VERSION

def get_author():
    return AUTHOR

def get_api(auth,verifier):
    auth.get_access_token(verifier)
    return tweepy.API(auth)

def get_url():
    auth = tweepy.OAuthHandler("hOfmzo8cdQoRD4GYkI4XCg", "LDzfw6X38jNGA5TBmHT7LZO7iEZ2qdhMJS52cYKrE")
    return auth.get_authorization_url()

def get_friends_sn(api):
    friends = []
    for friend in tweepy.Cursor(api.friends).items():
            friends.append(friend.screen_name)
    return friends

def get_followers(api):
    followers = []
    for follower in tweepy.Cursor(api.followers).items():
            followers.append(follower.screen_name)
    return follower
        
