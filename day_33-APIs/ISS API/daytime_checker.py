import requests
from datetime import datetime

MY_LAT = "36.007568"
MY_LONG = "-115.302760"

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# data = response.json()
# long = data["iss_position"]['longitude']
# lat = data["iss_position"]['latitude']
# iss_position = (long, lat)
# print(iss_position)

params = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}


response = requests.get(url="https://api.sunrise-sunset.org/json", params=params)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
print(sunrise)
print(sunset)

time_now = datetime.now()
print(time_now.hour)