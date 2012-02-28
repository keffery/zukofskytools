#!/usr/bin/env python
# -*- coding: latin-1 -*-
'''
Created on Feb 28, 2012

@author: leanother
'''

import tweepy
import cmd

class ZukofskyTwitterTools(object):
    '''
    classdocs
    '''


    def __init__(self):
        print("Zukofsky Twitter Tools")
        print("-----------------------")
        auth = tweepy.OAuthHandler("hOfmzo8cdQoRD4GYkI4XCg", "LDzfw6X38jNGA5TBmHT7LZO7iEZ2qdhMJS52cYKrE")
        print("URL: ",auth.get_authorization_url())
        auth.get_access_token(input("Verifier: "))
        
        self.api = tweepy.API(auth)

class Console(cmd.Cmd):
    
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.twitter = ZukofskyTwitterTools()
        self.friends = []
        self.followers = []
        for friend in tweepy.Cursor(self.twitter.api.friends).items():
            self.friends.append(friend.screen_name)
        for follower in tweepy.Cursor(self.twitter.api.followers).items():
            self.followers.append(follower.screen_name)
        
    
    def do_tweet(self,tweet):
        self.twitter.api.update_status(tweet)       
    def do_mentions(self,arg):
        mentions = self.twitter.api.mentions()
        for mention in mentions:
            print(mention.user.name,ascii(mention.text))
    def do_dontfollowme(self,arg):
        ct = 0
        for friend in self.friends:
            if self.followers.count(friend) == 0:
                ct += 1
                print(friend)
        print(ct)
        print("----")
        
    def do_idontfollow(self,arg):
        ct = 0
        for follower in self.followers:
            if self.friends.count(follower) == 0:
                ct +=1
                print(follower)  
                        
        print(ct)
        print("----")  
    def do_me(self,arg):
        print(self.twitter.api.me().name) 
        print("----")
          
interpreter= Console()
interpreter.cmdloop()
    
        