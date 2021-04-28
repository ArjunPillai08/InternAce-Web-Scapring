from bs4 import BeautifulSoup
import requests
import lxml
import numpy as np
import csv
import json
import numpy
import copy
import datetime
import pymongo
import os
import ssl
from disney import disney_scraper
from target import target_scraper
from warnerbros import warnerbros_scraper

ssl._create_default_https_context = ssl._create_unverified_context
client = pymongo.MongoClient("mongodb+srv://ArjunPillai08:Adrith1234567@database.8j5xq.mongodb.net/InternAce?retryWrites=true&w=majority", ssl_cert_reqs=ssl.CERT_NONE)
db = client['InternAce']
collection = db['internships']

culminated_list = []
new_dict = {"href": None, "position": None, "company": None, "industry": None, "position_type": None, "location": None, "date_posted": None, "is_remote": None, "is_paid": None, "payment_amount": None}

urls = {"https://jobs.disneycareers.com/search-jobs/internship/391-28648/1?glat=40.96788024902344&glon=-72.16480255126953": "disney", "https://www.warnerbroscareers.com/find-jobs/?type=Intern": "warnerbros", "https://jobs.target.com/search-jobs/intern/1118/1?fl=6252001,1269750&glat=41.53696823120117&glon=-88.58341217041016": "target"}

for url in urls:
    if urls[url] == "disney":
        culminated_list.extend(disney_scraper(url))
    elif urls[url] == "warnerbros":
        culminated_list.extend(warnerbros_scraper(url))
    elif urls[url] == "target":
        culminated_list.extend(target_scraper(url))

for i in culminated_list:
    if collection.find_one({"href": i["href"]}):
        pass
    else:
        collection.insert_one(i)
