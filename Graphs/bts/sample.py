'''Scrapes tweets from Emma Watson's timeline using conversation_id'''
import os
import json
import tweepy

client = tweepy.Client("AAAAAAAAAAAAAAAAAAAAAM%2FHhQEAAAAAYtePkvm5CPhL8lTG3xv%2FynVG8PM%3DAxmXQT4oqu4qGm91mVq8i24mdpTZMjvaaHpwkC4lAhzigXeU8V")

count = 1
reply_count = 1

hundred_tweets = client.get_users_tweets(id=166739404, tweet_fields=['conversation_id','created_at'], max_results=100)

conversation_ids = []
for tweet in hundred_tweets.data:
    conversation_ids.append(tweet.conversation_id)

for first_id in conversation_ids:
    os.system("twarc2 conversation --tweet-fields author_id,conversation_id,created_at {} > /Users/sulee/Desktop/network_graph/bts/data/reply{}.json".format(first_id,count))
    f = open('data/reply{}.json'.format(count))
    try:
        replies_json = json.load(f) # Only adds tweets with comments
        print(count)
        # # Grab 2nd Layer of Replies
        # for reply in replies_json['data']:
        #     os.system("twarc2 conversation --tweet-fields author_id,conversation_id,created_at {} > /Users/sulee/Desktop/network_graph/emma/data/reply{}.json".format(id,reply_count))
        #     reply_count += 1
        #     print(reply)
        count += 1
        print("grabbing replies")
    except ValueError:
        print("Empty File")
