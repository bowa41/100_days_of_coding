# 4. Pass the data back to the main.py file, so that you can print the data from main.py
from data_manager import DataManager

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
# print(sheet_data)

#  5. In main.py check if sheet_data contains any values for the "iataCode" key.
#  If not, then the IATA Codes column is empty in the Google Sheet.
#  In this case, pass each city name in sheet_data one-by-one
#  to the FlightSearch class to get the corresponding IATA code
#  for that city using the Flight Search API.
#  You should use the code you get back to update the sheet_data dictionary.
if sheet_data[0]["iataCode"] == "":
    from flight_search import FlightSearch
    flight_search = FlightSearch()
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    print(f"sheet_data:\n {sheet_data}")

    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()



# import requests
# import os
# from datetime import datetime
#
# AMADEUS_API_KEY = "EOccAWw5aeRQvEb2XftyPOZ6ABuLsNOf"
# AMADEUS_API_SECRET = "qNq1VnEA1IuX6Slo"
#
# SHEETY_EP = "https://api.sheety.co/fdd992f9d342e4e92c96befbcf0e13ff/flightDeals/prices"
# AMADEUS_EP = "https://test.api.amadeus.com/v1/shopping/flight-destinations?"
#
# CREDENTIAL_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"
#
#
#
# auth_params = {
#     "grant_type" : "client_credentials",
#     "client_id" : AMADEUS_API_KEY,
#     "client_secret" : AMADEUS_API_SECRET,
# }
#
# auth_headers = {"Content-Type": "application/x-www-form-urlencoded"}
#
# response1 = requests.post(url=CREDENTIAL_ENDPOINT, data=auth_params, headers=auth_headers)
# ACCESS_TOKEN = (response1.json()["access_token"])
#
# user_params = {
#     "parameter": {
#             "origin": "PAR",
#         "maxPrice": "200",
#   }
# }
#
# headers = {f"Authorization": f"Bearer {ACCESS_TOKEN}"}
#
# response2 = requests.get(url="https://test.api.amadeus.com/v1/shopping/"
#                              "flight-destinations?origin=PAR&oneWay=false&nonStop=false&maxPrice=200", headers=headers)
# print(response2.json())