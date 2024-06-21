class FlightSearch:

    def get_destination_code(self, city_name):
        # Return "TESTING" for now to make sure Sheety is working. Get TEQUILA API data later.
        code = "TESTING"
        return code



# import requests
#
# AMADEUS_API_KEY = "EOccAWw5aeRQvEb2XftyPOZ6ABuLsNOf"
# AMADEUS_API_SECRET = "qNq1VnEA1IuX6Slo"
#
# AMADEUS_EP = "https://test.api.amadeus.com/v1/shopping/flight-destinations?"
# CREDENTIAL_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"
# class FlightSearch:
#     #This class is responsible for talking to the Flight Search API.
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
#         "parameter": {
#             "origin": "PAR",
#             "maxPrice": "200",
#         }
#     }
#
#     headers = {f"Authorization": f"Bearer {ACCESS_TOKEN}"}
#
#     response2 = requests.get(url="https://test.api.amadeus.com/v1/shopping/"
#                                  "flight-destinations?origin=PAR&oneWay=false&nonStop=false&maxPrice=200",
#                              headers=headers)
#     print(response2.json())