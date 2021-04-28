
import datetime
import pymongo
import os
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
"""
usr = os.environ['MONGO_DB_USER']
pwd = os.environ['MONGO_DB_PASS']
"""
# connection string
client = pymongo.MongoClient("mongodb+srv://ArjunPillai08:Aditi1234567@database.8j5xq.mongodb.net/InternAce?retryWrites=true&w=majority", ssl_cert_reqs=ssl.CERT_NONE)

# test
db = client['InternAce']
# define collection
collection = db['internships']
# sample data
document = {"company":"Capital One",
	"city":"McLean",
	"state":"VA",
	"country":"US"}
# insert document into collection
id = collection.insert_one(document).inserted_id
print("id")
print(id)