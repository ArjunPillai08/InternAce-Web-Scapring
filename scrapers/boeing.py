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

def boeing_scraper(url):
    boeing_source = requests.get("https://jobs.boeing.com/category/internship-jobs/185-18469/9287/1").text
    boeing_soup = BeautifulSoup(boeing_source, "lxml")
    boeing_soup = boeing_soup.find_all("ul")[16]
    boeing_soup = boeing_soup.findChildren("li", recursive=False)
    for i in range(len(boeing_soup)):
        soup = boeing_soup[i]
        soup = soup.select("a")[0]
        href = soup["href"]
        position_soup = soup.findChildren("h3", recursive=False)
        soup = soup.findChildren("span", recursive=False)
        position = position_soup[0].text
        location = soup[1].text
        date_posted = soup[2].text
        href = "https://jobs.boeing.com" + href
        dict_2 = copy.deepcopy(new_dict)
        culminated_list.append(dict_2)
        culminated_list[-1]["position"] = position
        culminated_list[-1]["href"] = href
        culminated_list[-1]["location"] = location
        culminated_list[-1]["date_posted"] = date_posted
    return culminated_list