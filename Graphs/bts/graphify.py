'''Opening each of Emma's tweets and all its replies
    Turning into graph nodes/edges
    Nodes: { User 1 ID : # of times }
    Links: { User1#ID : User5#ID, # of times?  }'''

import json
import tweepy
AUTH_TOKEN = "AAAAAAAAAAAAAAAAAAAAAM%2FHhQEAAAAAYtePkvm5CPhL8lTG3xv%2FynVG8PM%3DAxmXQT4oqu4qGm91mVq8i24mdpTZMjvaaHpwkC4lAhzigXeU8V"
client = tweepy.Client(AUTH_TOKEN)

try:
    existing_graph = json.load(open('graph.json'))
    print(existing_graph)
except ValueError:
    existing_graph = {
        "nodes": [
        ],
        "links": [
        ]
    }

num_tweets = 8
user_nodes = {}
user_links = {}
checked_tweets = {}


for i in range(1,num_tweets + 1):
    f = open('data/reply{}.json'.format(i))
    print("currently checking reply", i)
    data = json.load(f)

    first_tweet = data['data'][0]
    print(first_tweet)

    current_target = first_tweet['conversation_id'] #check if conversation is a duplicate
    if current_target not in checked_tweets:
        checked_tweets[current_target] = first_tweet['created_at']

        # Creating Nodes/Links
        for tweet in data['data']:
            user = tweet['author_id']
            target = tweet['in_reply_to_user_id']

            # node
            if user in user_nodes:
                user_nodes[user] = user_nodes[user] + 1
            else:
                user_nodes[user] = 1
                print(user_nodes[user])
            if target not in user_nodes:
                user_nodes[target] = 1

            # link
            if user in user_links:
                user_links[user].append(target)
            else:
                user_links[user] = [target]

# Convert to JSON
for user, weight in user_nodes.items():
    existing_graph["nodes"].append(
        {"author_id": user, "value": weight})
for source, targets in user_links.items():
    for target in targets:
        existing_graph["links"].append(
            {"source": source, "target": target})

# Write to graph.json
with open("graph.json", "w") as outfile:
    json.dump(existing_graph, outfile)
