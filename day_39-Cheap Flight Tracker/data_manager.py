import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

SHETTY_TOKEN="Ym93YTQxOmxrYTtoajM0MHA4eXJwaGlrYmo0LzQyMzQ1Ng=="
SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/fdd992f9d342e4e92c96befbcf0e13ff/flightDeals/prices"

class DataManager:

    def __init__(self):
        self.sheet_headers = {f"Authorization": f"Basic {SHETTY_TOKEN}"}
        self.destination_data = {}

    def get_destination_data(self):
        # 2. Use the Sheety API to GET all the data in that sheet and print it out.
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=self.sheet_headers)
        data = response.json()
        self.destination_data = data["prices"]
        # 3. Try importing pretty print and printing the data out again using pprint() to see it formatted.
        # pprint(data)
        return self.destination_data

    # 6. In the DataManager Class make a PUT request and use the row id from sheet_data
    # to update the Google Sheet with the IATA codes. (Do this using code).
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)



# import requests
#
# SHEETY_EP = "https://api.sheety.co/fdd992f9d342e4e92c96befbcf0e13ff/flightDeals/prices"
# TOKEN = "Ym93YTQxOmxrYTtoajM0MHA4eXJwaGlrYmo0LzQyMzQ1Ng=="
# AMADEUS_API_KEY = "EOccAWw5aeRQvEb2XftyPOZ6ABuLsNOf"
# AMADEUS_API_SECRET = "qNq1VnEA1IuX6Slo"
#
# AMADEUS_EP = "https://test.api.amadeus.com/v1/reference-data/locations"
# CREDENTIAL_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"
#
# class DataManager:
#     #This class is responsible for talking to the Google Sheet.
#
#     sheet_headers = {f"Authorization": f"Basic {TOKEN}"}
#
#     sheety_response = requests.get(url=SHEETY_EP, headers=sheet_headers)
#     data_str = sheety_response.json().get("prices")
#
#     auth_params = {
#         "grant_type": "client_credentials",
#         "client_id": AMADEUS_API_KEY,
#         "client_secret": AMADEUS_API_SECRET,
#     }
#
#     auth_headers = {"Content-Type": "application/x-www-form-urlencoded"}
#
#     response1 = requests.post(url=CREDENTIAL_ENDPOINT, data=auth_params, headers=auth_headers)
#     ACCESS_TOKEN = (response1.json()["access_token"])
#
#     user_params = {
#         "subType": "CITY",
#         "keyword": "Paris",
#         }
#
#
#     headers = {f"Authorization": f"Bearer {ACCESS_TOKEN}"}
#
#     response2 = requests.get(url=AMADEUS_EP, json=user_params, headers=headers)
#     print(response2.json())
#
#
#
#
#
#     flights = {}
#     i = 0
#     for _ in data_str[i]:
#         flights[data_str[i]["city"]] = data_str[i]["lowestPrice"]
#         i += 1
#     print(flights)