'''Opening each of Rana Ayyub's tweets and all its replies
    Turning into graph nodes/edges'''

import json
import pickle

network_graph = {
    "nodes": [
    ],
    "links": [
    ]
}

# RanaAyyub_2 = [json.loads(line) for line in open('AllData/RanaAyyub_2.pickle', 'r', encoding='utf-8')]
unique_nodes = set()

with open('AllData/RanaAyyub_2.pickle', 'rb') as f1:
    data = pickle.load(f1)
    for i in range(10):
        conversation_thread = data[i]["data"]
        for tweet in conversation_thread:
            user = tweet['author_id']
            target = tweet['in_reply_to_user_id']
            time = tweet['created_at']
            unique_nodes.add(user)
            unique_nodes.add(target)
            network_graph["links"].append({"source": user, "value": 1, "target": target})
for node in unique_nodes:
    network_graph["nodes"].append({"author_id": node, "value": 10, "is_main_tweet": False, "tweet_count": 0, "timestamp": "2021-01-01T00:00:00.000Z"})
    
# # Writing to sample.json
with open("Graphs/big_data_rana/graphify.json", "w") as outfile:
    json.dump(network_graph, outfile)
    
