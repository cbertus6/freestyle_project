import os
import json
from pprint import pprint

import requests
from dotenv import load_dotenv


from yelp.client import Client
import plotly.express as px 
import plotly.graph_objects as go


load_dotenv()

OPEN_YELP_API_KEY = os.getenv("YELP_API_KEY")
client = Client(OPEN_YELP_API_KEY)
# MY_ZIP = os.getenv("MY_ZIP", default="73103") 


request_url = "https://api.yelp.com/v3/businesses/search"
HEADERS = {'Authorization': 'bearer %s' % OPEN_YELP_API_KEY} 

# INPUT
print("THANKS FOR USING YELP BUSINESS SEARCH")
print("TO BEGIN, PLEASE ENTER THE FOLLOWING CRITERIA TO HELP WITH YOUR SEARCH:")

location = input("Location: ")
search_term = input("Food type: ")
price_range = input("Price range 1($) - 4($$$$): ")
limit_results = input("Number of business results to return: ")



parameters= {'term':search_term,
            'location': location,
            'limit': limit_results,
            'radius': 10000,
            'offset': 50,
            'sort_by': 'best_match',
            'price': price_range,}

response = requests.get(request_url, params=parameters, headers=HEADERS)



parsed_response = json.loads(response.text)

# if 'Error' in parsed_response:
#     print("Invalid search term. Please try again.")
#     exit()

# OUTPUT

latitude = []
longitude = []
name = []

for b in parsed_response['businesses']:
    print(b['name'])
    latitude.append(b['coordinates']['latitude'])
    longitude.append(b['coordinates']['longitude'])
    name.append(b['name'])





mapbox_access_token = open(parsed_response).read()

fig = go.Figure(go.Scattermapbox(
        lat=['latitude'],
        lon=['longitude'],
        mode='markers',
        marker=go.scattermapbox.Marker(
            size=9
        ),
        text=['name'],
    ))

fig.update_layout(
    autosize=True,
    hovermode='closest',
    mapbox=dict(
        accesstoken=mapbox_access_token,
        bearing=0,
        center=dict(
            lat=['latitude'],
            lon=['longitude']
        ),
        pitch=0,
        zoom=10
    ),
)

fig.show()

print("--------------------")
# we have the coordinates, can it print on a graph with the restaurant name? 
  



#TODO
# Readme
# resolve errors
# add any additional inputs
# make output prettier and add results
# maybe send email or graph of locations?


# SOURCES
# https://www.yelp.com/developers/documentation/v3/business_search
# https://www.youtube.com/watch?v=GJf7ccRIK4U

