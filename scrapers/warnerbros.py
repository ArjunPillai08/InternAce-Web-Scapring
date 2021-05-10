from bs4 import BeautifulSoup
import requests
import lxml
import numpy as np
import csv
import json
import numpy
import copy

culminated_list = []
new_dict = {"href": None, "position": None, "company": None, "industry": None, "position_type": None, "location": None, "date_posted": None, "is_remote": None, "is_paid": None, "payment_amount": None}

def warnerbros_scraper(url):
    warner_source = requests.get(url).text
    warner_soup = BeautifulSoup(warner_source, 'lxml')
    warner_soup = warner_soup.select("article", {"id": "post-40"})[0].select("div", {"class": "container-fluid"})[0].findChildren('div', recursive=False)[0]
    warner_soup = warner_soup.findChildren('div', recursive=False)
    for i in range(1, len(warner_soup)):
        block = warner_soup[i]
        block = block.findChildren('div', recursive=False)[0]
        block = block.select("div", {"class": "row no-gutter"})[0].findChildren('div', recursive=False)
        child_block = (block[0].findChildren("a"))
        href = "https://www.warnerbroscareers.com/find-jobs/" + child_block[0]["href"]
        Position = block[0].select('a')[0].text
        Company = block[1].text
        Type = block[2].text
        Requirements = block[3].text
        Location = block[4].text
        Date_Posted = block[5].text
        dict_2 = copy.deepcopy(new_dict)
        culminated_list.append(dict_2)
        culminated_list[-1]["href"] = href
        culminated_list[-1]["position"] = Position.replace("\n", "")
        culminated_list[-1]["date_posted"] = Date_Posted.replace("\n", "")
        culminated_list[-1]["company"] = Company.replace("\n", "")
        culminated_list[-1]["location"] = Location.replace("\n", "")
        culminated_list[-1]["position_type"] = Type.replace("\n", "")
    return culminated_list