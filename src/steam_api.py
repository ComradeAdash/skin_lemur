"""

A simple script to fetch a single skin's data. 

"""

import requests
import urllib.parse
import math
import time
import re

the_skin = " " 
url = f"https://steamcommunity.com/market/priceoverview/?appid=730&market_hash_name={the_skin}"
skin_names_url = "https://raw.githubusercontent.com/ByMykel/CSGO-API/main/public/api/en/skins_not_grouped.json"
parameters = { 
    "appid": 730,
    "currency" : 20, # code for CAD, USD is 1
    "language" : "english",
    "format" : "json"
}

# ------------ Parsing Functions ----------------


def fetch_request(url, params=None, headers=None, timeout=10):
    skin_data = None
    response = requests.get(url, params=params, headers=headers, timeout=timeout)
    if response.status_code == 200:
        skin_data = response.json() # raw JSON data
        return skin_data
    else:
        print(f"Error: Unable to fetch data, status code {response.status_code}")

def get_all_skin_names(url, params=None, headers=None, timeout=10):
    skin_names = []
    data = fetch_request(url)
    for it in data:
        hash_name =  it.get("market_hash_name")
        skin_names.append(hash_name)
    return skin_names

# ------------ Testing ----------------     

info = fetch_request(url, parameters)
print(info)
