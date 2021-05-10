import json, os
import datetime
import pymongo, ssl, os
from dotenv import load_dotenv

from db_auth import connect_to_db
from scrapers.disney import disney_scraper
from scrapers.target import target_scraper
from scrapers.warnerbros import warnerbros_scraper
from scrapers.ups import ups_scraper
from scrapers.boeing import boeing_scraper
import datetime

collection = connect_to_db()
culminated_list = list()
  
f = open('urls.json',)
urls = json.load(f)

for item in urls:
    if item['module'] == "disney":
        culminated_list.extend(disney_scraper(item['url']))
    elif item['module'] == "warnerbros":
        culminated_list.extend(warnerbros_scraper(item['url']))
    elif item['module'] == "target":
        culminated_list.extend(target_scraper(item['url']))
    elif item['module'] == "boeing":
        culminated_list.extend(boeing_scraper(1))
    elif item['module'] == "ups":
        culminated_list.extend(ups_scraper(1))

print(culminated_list)

for i in culminated_list:
    if collection.find_one({"href": i["href"]}):
        pass
    else:
        collection.insert_one(i)

