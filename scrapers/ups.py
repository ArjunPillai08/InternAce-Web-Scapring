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

def ups_scraper(url):
    ups_source = requests.get("https://www.jobs-ups.com/category/internship-and-co-op-jobs/1187/4662/1").text
    ups_soup = BeautifulSoup(ups_source, "lxml")
    ups_soup = ups_soup.select("main", {"id":"content"})
    ups_soup = ups_soup[0].findChildren("div", recursive=False)[2]
    ups_soup = ups_soup.findChildren("section", recursive=False)[0]
    ups_soup = ups_soup.findChildren("section", recursive=False)[0]
    ups_soup = ups_soup.findChildren("ul", recursive=False)[0]
    ups_soup = ups_soup.findChildren("li", recursive=False)
    for i in range(len(ups_soup)):
        soup = ups_soup[i]
        soup = soup.findChildren("a", recursive=False)[0]
        position = soup.select("h2")[0].text
        location = soup.findChildren("span", recursive=False)[1].text
        href = "https://www.jobs-ups.com" + soup["href"]
        dict_2 = copy.deepcopy(new_dict)
        culminated_list.append(dict_2)
        culminated_list[-1]["position"] = position
        culminated_list[-1]["location"] = location
        culminated_list[-1]["href"] = href
    return culminated_list