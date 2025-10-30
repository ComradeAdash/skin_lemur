""""

A simple script to fetch a single skin's data. 

"""


import requests
import urllib.parse

the_skin = "M4A4 | Desolate Space (Factory New)"
encoded_name = urllib.parse.quote(the_skin, safe='') # 'percent' encodes the skin name for the URL

url = (
    f"https://steamcommunity.com/market/listings/730/{encoded_name}/render"
    "?start=0"
    "&count=10"
    "&currency=1"
    "&language=english"
    "&format=json"
)

# ------------ Parsing Functions ----------------

"""     
Fetches data from the specifeid URL

Parameters:
    url - str
    params -dict (optional)
    headers - dict (optional)
    timeout - int (optional, default=10)

    returns a JSON response from the requested server / url

    *Steam Marrket API returns all the information inside the listinginfo attribute
"""

def fetch_data(url, params=None, headers=None, timeout=10):
    skin_data = None
    response = requests.get(url, params=params, headers=headers, timeout=timeout)
    if response.status_code == 200:
        skin_data = response.json() # raw JSON data
        return skin_data
    else:
        print(f"Error: Unable to fetch data, status code {response.status_code}")


skin_info = fetch_data(url)
skin_info.get("listinginfo", {})
for key, value in skin_info["listinginfo"].items():
    print(f"Listing ID: {key}")
    print(f"Skin Data: {value}")
    print("\n")