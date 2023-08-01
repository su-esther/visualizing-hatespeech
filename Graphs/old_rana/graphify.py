'''Opening each of Rana Ayyub's tweets and all its replies
    Turning into graph nodes/edges'''

import json

import tweepy

AUTH_TOKEN = "AAAAAAAAAAAAAAAAAAAAAM%2FHhQEAAAAAYtePkvm5CPhL8lTG3xv%2FynVG8PM%3DAxmXQT4oqu4qGm91mVq8i24mdpTZMjvaaHpwkC4lAhzigXeU8V"
client = tweepy.Client(AUTH_TOKEN)
# Rana Ayyub's user_id is 268676434

try:
    existing_graph = json.load(open('sample.json'))
    print(existing_graph)
except ValueError:
    existing_graph = {
        "nodes": [
        ],
        "links": [
        ]
    }

dictionary = {}
target_tweet_nodes = {}
tweet_count = 20

for i in range(1,tweet_count + 1):
    f = open('reply{}.json'.format(i))
    print("currently checking reply", i)
    data = json.load(f)

    first_tweet = data['data'][0]
    print(first_tweet)

    current_target = first_tweet['conversation_id'] #check if conversation is a duplicate
    if current_target not in target_tweet_nodes:
        target_tweet_nodes[current_target] = first_tweet['created_at'] #TARGET_TWEET_NODES {conversation_id : timestamp}

        for tweet in data['data']: #DICTIONARY {user# : weight, conversation_id, tweet_count}
            user = tweet['author_id']
            target = tweet['conversation_id']
            time = tweet['created_at']
            if user in dictionary:
                dictionary[user][0] = dictionary[user][0] + 1 #+1 weight/prsence of perp
                # TO-DO: need to consider perps that attack multiple tweets
            else:
                dictionary[user] = [1]
                #dictionary[user].append([target])
                dictionary[user].append(target)
                # dictionary[user].append(tweet_count)
                print(dictionary[user])
        tweet_count += 1

# Use dictionary to update graph nodes/links for all replies to that 1 tweet

# MAIN TWEETS
# nodes : [{"author_id": 12408712, "value": 10, "tweet_count": 1, "is_main_tweet": True},]
# sort by time, oldest to most recent
sorted_by_time = dict(sorted(target_tweet_nodes.items(), key=lambda item:item[1]))

tweet_count=0 # determines x position for the node to be centered at
tweetID_to_nodeNumber = {}
for node in sorted_by_time.keys():
    existing_graph["nodes"].append({"author_id": node, "value": 10, "is_main_tweet": True, "timestamp": sorted_by_time[node], "tweet_count": tweet_count})
    tweetID_to_nodeNumber[node] = tweet_count
    print(sorted_by_time[node], tweet_count)
    tweet_count += 1

# REPLY TWEETS
# nodes : [{"author_id": 12408712, "value": 2, "tweet_count": 1, "is_main_tweet": False},]
for user in dictionary.keys():
    existing_graph["nodes"].append(
        {"author_id": user, "value": dictionary[user][0], "tweet_count": tweetID_to_nodeNumber[dictionary[user][1]], "is_main_tweet": False})
    existing_graph["links"].append(
        #{"source": user, "value": dictionary[user][0], "target": dictionary[user][1][0]})
        {"source": user, "value": dictionary[user][0], "target": dictionary[user][1]})



# Writing to sample.json
with open("sample.json", "w") as outfile:
    json.dump(existing_graph, outfile)
