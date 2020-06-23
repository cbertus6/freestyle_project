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



parameters= {'term':'coffee',
            'location': 'San Diego',
            'limit': 50,
            'radius': 10000,
            'offset': 50,
            'sort_by': 'best_match',
            'price': '1'}

response = requests.get(request_url, params=parameters, headers=HEADERS)
parsed_response = json.loads(response.text)

# OUTPUT

for b in parsed_response['businesses']:
    print(b['name'])


