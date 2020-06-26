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

request_url = "https://api.yelp.com/v3/businesses/search"
HEADERS = {'Authorization': 'bearer %s' % OPEN_YELP_API_KEY} 

# INPUT
print("THANKS FOR USING YELP BUSINESS SEARCH")
print("TO BEGIN, PLEASE ENTER THE FOLLOWING CRITERIA TO HELP WITH YOUR SEARCH:")

location = input("Location: ")
search_term = input("Food type (Italian, tacos, Thai, etc...): ")
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
print("got the response")

if 'error' in response.text:
    print("Invalid search term. Please try again.")
    exit()

parsed_response = json.loads(response.text)


# OUTPUT
latitude = []
longitude = []
name = []


print("--------------------")
print("Thank you for choosing Yelp! Your recommendations are below:")
for b in parsed_response['businesses']:
    print(b['name'] + " " + str(b['rating']) + " stars")
    latitude.append(float(b['coordinates']['latitude']))
    longitude.append(float(b['coordinates']['longitude']))
    name.append(b['name'])
print("--------------------")
print("Enjoy!")


# MAP INFO

OPEN_MAPBOX_ACCESS_TOKEN = os.getenv("MAPBOX_ACCESS_TOKEN")

fig = go.Figure(go.Scattermapbox(
        lat=latitude,
        lon=longitude,
        mode='markers',
        marker=go.scattermapbox.Marker(
            size=9
        ),
        text=name,
    ))

fig.update_layout(
    autosize=True,
    hovermode='closest',
    mapbox=dict(
        accesstoken=OPEN_MAPBOX_ACCESS_TOKEN,
        bearing=0,
        center=dict(
            lat=parsed_response['region']['center']['latitude'],
            lon=parsed_response['region']['center']['longitude']
        ),
        pitch=0,
        zoom=10
    ),
)

fig.show()


 
# SOURCES
# https://github.com/prof-rossetti/intro-to-python
# https://www.yelp.com/developers/documentation/v3/business_search
# https://www.youtube.com/watch?v=GJf7ccRIK4U
# https://plotly.com/python/scattermapbox/

