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

def target_scraper(url):
    target_source = requests.get(url).text
    target_soup = BeautifulSoup(target_source, 'lxml')
    target_soup = target_soup.select('main', {'id': 'content'})
    target_soup = target_soup[0].findChildren('section', recursive=False)[0].findChildren('div', recusrive=False)[0]
    target_soup = target_soup.findChildren('section', recursive=False)[0].findChildren('section', recursive=False)[0]
    target_soup = target_soup.findChildren('ul', recursive=False)[0].findChildren('li', recusrive=False)
    for i in range(len(target_soup)):
        block = target_soup[i]
        block = block.findChildren('a', recursive=False)[0]
        href = (block["href"])
        position = block.findChildren('h2', recursive=False)[0].text
        location = block.findChildren('span', recursive=False)[0].text
        dict_2 = copy.deepcopy(new_dict)
        culminated_list.append(dict_2)
        culminated_list[-1]["href"] = href
        culminated_list[-1]["position"] = position.replace("\n", "")
        culminated_list[-1]["locaton"] = location.replace("\n", "")
        culminated_list[-1]["company"] = "Target"
        culminated_list[-1]["industry"] = "Retail"
        culminated_list[-1]["position_type"] = "Intern"
        culminated_list[-1]["is_remote"] = False
        culminated_list[-1]["is_paid"] = False
    return culminated_list
