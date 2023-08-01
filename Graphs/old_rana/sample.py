'''Scrapes tweets from Rana Ayyub's timeline using conversation_id'''
import os
import json
import tweepy

client = tweepy.Client("AAAAAAAAAAAAAAAAAAAAAM%2FHhQEAAAAAYtePkvm5CPhL8lTG3xv%2FynVG8PM%3DAxmXQT4oqu4qGm91mVq8i24mdpTZMjvaaHpwkC4lAhzigXeU8V")

hundred_tweets = client.get_users_tweets(id=268676434, tweet_fields=['conversation_id','created_at'], max_results=100)

count = 1
for tweet in hundred_tweets.data:
    print(count)
    os.system("twarc2 conversation --tweet-fields author_id,conversation_id,created_at {} > /Users/sulee/Desktop/network_graph/reply{}.json".format(tweet.conversation_id,count))
    f = open('reply{}.json'.format(count))
    try:
        data = json.load(f) # Only adds tweets with comments
        count += 1
        with open("rana_tweets.json", "w") as outfile:
            outfile.write(tweet['data']['created_at'])
            outfile.close()
    except ValueError:
        print("Empty File")
