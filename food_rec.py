import os
import json
from pprint import pprint

import requests
from dotenv import load_dotenv


from yelp.client import Client


load_dotenv()

OPEN_YELP_API_KEY = os.getenv("YELP_API_KEY")
client = Client(OPEN_YELP_API_KEY)
MY_ZIP = os.getenv("MY_ZIP", default="73103") 


request_url = "https://api.yelp.com/v3/businesses/search"
HEADERS = {'Authorization': 'bearer %s' % OPEN_YELP_API_KEY} 

# INPUT
print("THANKS FOR USING YELP BUSINESS SEARCH")
print("TO BEGIN, PLEASE ENTER THE FOLLOWING CRITERIA TO HELP WITH YOUR SEARCH:")

location = input("Location: ")
search_term = input("Search term: ")
price_range = input("Price range 1($) - 4($$$$): ")
limit_results = input("Number of business results to return: ")



parameters= {'term':search_term,
            'location': location,
            'limit': limit_results,
            'radius': 10000,
            'offset': 50,
            'sort_by': 'best_match',
            'price': price_range}

response = requests.get(request_url, params=parameters, headers=HEADERS)
parsed_response = json.loads(response.text)

# OUTPUT


for b in parsed_response['businesses']:
    print(b['name'])
  



#TODO
# Readme
# resolve errors
# add any additional inputs
# make output prettier and add results
# maybe send email or graph of locations?


# SOURCES
# https://www.yelp.com/developers/documentation/v3/business_search
# https://www.youtube.com/watch?v=GJf7ccRIK4U

