import requests
from flight_data import FlightData

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = YOUR FLIGHT SEARCH API KEY
AMADEUS_API_KEY = "EOccAWw5aeRQvEb2XftyPOZ6ABuLsNOf"
AMADEUS_API_SECRET = "qNq1VnEA1IuX6Slo"

AMADEUS_EP = "https://test.api.amadeus.com/v1/shopping/flight-destinations?"
CREDENTIAL_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"

class FlightSearch:

    def get_destination_code(self, city_name):
        location_endpoint = AMADEUS_EP
        auth_params = {
                    "grant_type": "client_credentials",
                    "client_id": AMADEUS_API_KEY,
                    "client_secret": AMADEUS_API_SECRET,
                }

                auth_headers = {"Content-Type": "application/x-www-form-urlencoded"}

                response1 = requests.post(url=CREDENTIAL_ENDPOINT, data=auth_params, headers=auth_headers)
                ACCESS_TOKEN = (response1.json()["access_token"])


        user_params = {
                    "parameter": {
                        "origin": "PAR",
                        "maxPrice": "200",
                    }
                }

                headers = {f"Authorization": f"Bearer {ACCESS_TOKEN}"}

                response2 = requests.get(url="https://test.api.amadeus.com/v1/shopping/"
                                             "flight-destinations?origin=PAR&oneWay=false&nonStop=false&maxPrice=200",
                                         headers=headers)
        results = response2.json()["locations"]
        code = results[0]["code"]
        return code

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        headers = {"apikey": TEQUILA_API_KEY}
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }

        response = requests.get(
            url=f"{TEQUILA_ENDPOINT}/v2/search",
            headers=headers,
            params=query,
        )

        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        print(f"{flight_data.destination_city}: £{flight_data.price}")
        return flight_data
