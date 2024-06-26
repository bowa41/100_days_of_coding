import requests
import os

from twilio.rest import Client

#   JSON Online Viewer: https://jsonviewer.stack.hu/
#   Twilio SMS: https://console.twilio.com/
#
#   get twilio to work with free accounts in python anywhere
#   https://help.pythonanywhere.com/pages/TwilioBehindTheProxy/

api_key = os.environ["OWM_API_KEY"]
# MY_LAT = 36.007568
# MY_LONG = -115.302760
MY_LAT = 26.122438
MY_LONG = -80.137314
forecast_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
current_endpoint = "https://api.openweathermap.org/data/2.5/weather"

parameters = {
        "lat": MY_LAT,
        "lon": MY_LONG,
        "appid": api_key,
        "cnt": 4,
    }

response = requests.get(forecast_endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()

is_rain = False

for n in range(0,4):
    if weather_data["list"][n]["weather"][0]["id"] < 700:
        is_rain = True

if is_rain:
    account_sid = "AC7ca3204f75d05946ac69acc47d73794a"
    auth_token = os.environ['TWILIO_AUTH_KEY']
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_="+18556773383",
        body="It's going to rain today, better bring an ☂️",
        to="+18777804236"
    )

    print(message.status)