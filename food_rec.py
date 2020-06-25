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
    print(b['name'])
    latitude.append(b['coordinates']['latitude'])
    longitude.append(b['coordinates']['longitude'])
    name.append(b['name'])
print("--------------------")
print("Enjoy!")


MAPBOX_ACCESS_TOKEN="pk.eyJ1IjoiczJ0MiIsImEiOiJja2J2ZHdxenowNTJwMndxZjdyY3ZhNTV3In0.nqev9fVN8FEibo3cr81YAA"


fig = go.Figure(go.Scattermapbox(
        lat=['38.91427','38.91538','38.91458',
             '38.92239','38.93222','38.90842',
             '38.91931','38.93260','38.91368',
             '38.88516','38.921894','38.93206',
             '38.91275'],
        lon=['-77.02827','-77.02013','-77.03155',
             '-77.04227','-77.02854','-77.02419',
             '-77.02518','-77.03304','-77.04509',
             '-76.99656','-77.042438','-77.02821',
             '-77.01239'],
        mode='markers',
        marker=go.scattermapbox.Marker(
            size=9
        ),
        text=["The coffee bar","Bistro Bohem","Black Cat",
             "Snap","Columbia Heights Coffee","Azi's Cafe",
             "Blind Dog Cafe","Le Caprice","Filter",
             "Peregrine","Tryst","The Coupe",
             "Big Bear Cafe"],
    ))

fig.update_layout(
    autosize=True,
    hovermode='closest',
    mapbox=dict(
        accesstoken=MAPBOX_ACCESS_TOKEN,
        bearing=0,
        center=dict(
            lat=38.92,
            lon=-77.07
        ),
        pitch=0,
        zoom=10
    ),
)

fig.show()

# mapbox_access_token = open(parsed_response).read()

# fig = go.Figure(go.Scattermapbox(
#         lat=['latitude'],
#         lon=['longitude'],
#         mode='markers',
#         marker=go.scattermapbox.Marker(
#             size=9
#         ),
#         text=['name'],
#     ))

# fig.update_layout(
#     autosize=True,
#     hovermode='closest',
#     mapbox=dict(
#         accesstoken=mapbox_access_token,
#         bearing=0,
#         center=dict(
#             lat=parsed_response['region']['center']['latitude'],
#             lon=parsed_response['region']['center']['longitude']
#         ),
#         pitch=0,
#         zoom=10
#     ),
# )

# fig.show()


 



#TODO
# graph of locations
# licences?


# SOURCES
# https://www.yelp.com/developers/documentation/v3/business_search
# https://www.youtube.com/watch?v=GJf7ccRIK4U

