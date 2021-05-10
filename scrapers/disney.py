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

def disney_scraper(url):
    disney_source = requests.get(url).text
    disney_soup = BeautifulSoup(disney_source, 'lxml')
    disney_soup = disney_soup.find_all('table')[0]
    disney_soup = disney_soup.findChildren('tbody', recursive=False)[0].findChildren('tr', recursive=False)
    for i in range(len(disney_soup)):
        soup = disney_soup[i]
        soup = soup.findChildren('td')
        child = soup[0].findChildren('a')
        href= "https://jobs.disneycareers.com/job/" + child[0]["href"]
        position = soup[0].text
        date_posted = soup[1].text
        company = soup[2].text
        location = soup[3].text
        dict_2 = copy.deepcopy(new_dict)
        culminated_list.append(dict_2)
        culminated_list[-1]["href"] = href
        culminated_list[-1]["position"] = position.replace("\n", "")
        culminated_list[-1]["date_posted"] = date_posted.replace("\n", "")
        culminated_list[-1]["company"] = company.replace("\n", "")
        culminated_list[-1]["location"] = location.replace("\n", "")
        culminated_list[-1]["industry"] = 'Entertainment'
    return culminated_list