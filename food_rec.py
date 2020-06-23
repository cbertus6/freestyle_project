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
#COUNTRY_CODE = os.getenv("COUNTRY_CODE", default="US")

#id = input("Please enter city name or zip: ")

request_url = "https://api.yelp.com/v3/businesses/search"
HEADERS = {'Authorization': 'bearer %s' % OPEN_YELP_API_KEY} 



# business_response = client.business.get_by_id('yelp-san-francisco')

# business_response
# Business(alias='yelp-san-francisco', attributes=None, categories=[Category(alias='massmedia', title='Mass Media')], coordinates=Coordinates(latitude=37.7867703362929, longitude=-122.399958372115), display_phone='(415) 908-3801', hours=[Hours(hours_type='REGULAR', is_open_now=True, open=[DayHours(day=0, end='1800', is_overnight=False, start='0800'), DayHours(day=1, end='1800', is_overnight=False, start='0800'), DayHours(day=2, end='1800', is_overnight=False, start='0800'), DayHours(day=3, end='1800', is_overnight=False, start='0800'), DayHours(day=4, end='1800', is_overnight=False, start='0800')])], id='4kMBvIEWPxWkWKFN__8SxQ', image_url='https://s3-media2.fl.yelpcdn.com/bphoto/nQK-6_vZMt5n88zsAS94ew/o.jpg', is_claimed=True, is_closed=False, location=Location(address1='140 New Montgomery St', address2='', address3='', city='San Francisco', country='US', cross_streets='Natoma St & Minna St', display_address=['140 New Montgomery St', 'San Francisco, CA 94105'], state='CA', zip_code='94105'), name='Yelp', phone='+14159083801', photos=['https://s3-media2.fl.yelpcdn.com/bphoto/nQK-6_vZMt5n88zsAS94ew/o.jpg', 'https://s3-media2.fl.yelpcdn.com/bphoto/yFHIb9gob4TzhKUemMOPww/o.jpg', 'https://s3-media1.fl.yelpcdn.com/bphoto/EHCfkEpZraIfPl8gvCo1tg/o.jpg'], rating=2.0, review_count=8421, transactions=[], url='https://www.yelp.com/biz/yelp-san-francisco?adjust_creative=wpr6gw4FnptTrk1CeT8POg&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_lookup&utm_source=wpr6gw4FnptTrk1CeT8POg')
parameters= {'term':'coffee',
            'limit':50,
            'radius':10000,
            'location': 'San Diego'}

response = requests.get(request_url, params=parameters, headers=HEADERS)
parsed_response = json.loads(response.text)

print(parsed_response)
# OUTPUT

print("-------------------------")
print("NAME: {business_name}") 
print("-------------------------")
print("TOP 5 BUSINESS NAMES: ")


# def get_food_rec(zip_code=MY_ZIP, country_code=COUNTRY_CODE):
#     #print(parsed_response.keys()) #> dict_keys(['cod', 'message', 'cnt', 'list', 'city'])
#     result = {
#         "city_name": parsed_response["city"]["name"],
#         "hourly_forecasts": []
#     }
#     for forecast in parsed_response["list"][0:9]:
#         #print(forecast.keys()) #> dict_keys(['dt', 'main', 'weather', 'clouds', 'wind', 'sys', 'dt_txt'])
#         result["hourly_forecasts"].append({
#             "timestamp": forecast["dt_txt"],
#             "temp": human_friendly_temp(forecast["main"]["feels_like"]),
#             "conditions": forecast["weather"][0]["description"]
#         })
#     return result

# if __name__ == "__main__":

#     if APP_ENV == "development":
#         zip_code = input("PLEASE INPUT A ZIP CODE (e.g. 06510): ")
#         results = get_hourly_forecasts(zip_code=zip_code) # invoke with custom params
#     else:
#         results = get_hourly_forecasts() # invoke with default params

#     print("-----------------")
#     print(f"TODAY'S WEATHER FORECAST FOR {results['city_name'].upper()}...")
#     print("-----------------")

#     for hourly in results["hourly_forecasts"]:
#         print(hourly["timestamp"], "|", hourly["temp"], "|", hourly["conditions"])
