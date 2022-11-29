import pymongo
client=pymongo.MongoClient("mongodb+srv://rajamohanreddy:Raja3c4@cluster1.ipjaewy.mongodb.net/?retryWrites=true&w=majority")
db=client.test
print(db)

d= {
    "name" :"rajamohan",
    "edu" : "btech",
    "location":"kadapa"
}

db1= client['mongo1']
coll = db1['test']
coll.insert_one(d )

import pymongo
client=pymongo.MongoClient("mongodb+srv://rajamohanreddy:Raja3c4@cluster1.ipjaewy.mongodb.net/?retryWrites=true&w=majority")
db=client.test
print(db)

d= {
    "name" :"rajamohan",
    "edu" : "btech",
    "location":"kadapa"
}

db1= client['mongo1']
coll = db1['test']
coll.insert_one(d )