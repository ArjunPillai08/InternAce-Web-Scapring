import json, os
import datetime

from db_auth import connect_to_db
from scrapers.disney import disney_scraper
from scrapers.target import target_scraper
from scrapers.warnerbros import warnerbros_scraper

collection = connect_to_db()
culminated_list = list()
  
# Opening JSON file
f = open('urls.json',)
urls = json.load(f)

# Read JSON file
for item in urls:
    if item['module'] == "disney":
        culminated_list.extend(disney_scraper(item['url']))
    elif item['module'] == "warnerbros":
        culminated_list.extend(warnerbros_scraper(item['url']))
    elif item['module'] == "target":
        culminated_list.extend(target_scraper(item['url']))

print(culminated_list)
# UNCOMMENT BELOW SECTION WHEN YOU NEED TO INSERT STUFF!

# for i in culminated_list:
#     if collection.find_one({"href": i["href"]}):
#         pass
#     else:
#         collection.insert_one(i)
