
# coding: utf-8

# In[3]:


import csv
import json


# In[4]:


csvfile = open('training.1600000.processed.noemoticon.csv', 'r')
jsonfile = open('twitter_parsed.json', 'w')


# In[5]:


fieldnames = ("polarity","id","date","query","user","text")
reader = csv.DictReader(csvfile, fieldnames)

for row in reader:
    if row:
        json.dump(row, jsonfile)
        jsonfile.write('\n')


# In[6]:


import pymongo
from pymongo import MongoClient
client = MongoClient()
db = client.myDB
twitter = db.twitter
print("Database created")


# In[7]:


from bson.json_util import loads

count = 0
file = open('twitter_parsed.json','r')


for y in file:
    data = json.loads(y)
    db.twitter.insert_one(data)
    count = count +1
db.twitter.count_documents({})


# In[8]:


import pprint

def pp(obj):
    pprint.pprint(obj)
    
def ppall(col):
    for p in col:
        pp( p )
        


# # How many Twitter users are in the database?

# In[9]:


db.twitter.count_documents({})


# In[10]:


pprint.pprint(twitter.count_documents({ "text": {"$regex": "^@"} }) )


# In[11]:


pprint.pprint(twitter.count_documents({ "id":{"$ne" : "null"}}))


# # Which Twitter users link the most to other Twitter users? (Provide the top ten.)

# In[12]:


ppall(db.twitter.aggregate([  
    {"$group": {"_id": {"user": "$user"},"uniqueIds": {"$addToSet": "$_id"},"count": {"$sum": 1}}},
    {"$match": { "count": {"$gt": 1}}},
    {"$sort": { "count": -1}},
    { "$limit" : 10 }
],  
    allowDiskUse=True  
))


# In[14]:


tweet = twitter.count_documents({ "text": {"$regex": "@"} })
pprint.pprint( tweet)


# In[ ]:


#for x in twitter.find({"text": {"$regex": "@"}},{ "_id": 0, "user": 1, "text": 1 }):
#    print(x)


# In[210]:


dup = []
for x in twitter.find({"text": {"$regex": "@"}},{ "_id": 0, "user": 1 }):
    dup.append(x)
    print(x)


# In[ ]:


popular = []
for x in [ele for ind, ele in enumerate(dup,1) if ele not in dup[ind:]]:
    if dup.count(x)>1:
        popular.append(dup.count(x))
        print("{} {}".format(x,dup.count(x)))


# In[186]:


test.count_documents({ "user": "tweet"})


# In[199]:


ppall(db.twitter.aggregate([  
    {"$group": {"_id": {"user": "$user"}, "uniqueIds": {"$addToSet": "$user"},"count": {"$sum": 1}}},
    {"$match": { "count": {"$gt": 1}}},
    {"$sort": { "count": -1}},
    { "$limit" : 5 }
],  
    allowDiskUse=True  
))


# In[171]:




