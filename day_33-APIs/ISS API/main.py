import requests
import smtplib
import time
from datetime import datetime

MY_LAT = 36.007568
MY_LONG = -115.302760
my_gmail = "bowatest41@gmail.com"
gmail_pw = "eciepvmumtvlsjnw"


def iss_location():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    # Your position is within +5 or -5 degrees of the ISS position.
    if (MY_LAT-5) <= iss_latitude <= (MY_LAT+5):
        if (MY_LONG-5) <= iss_longitude <= (MY_LONG+5):
            return True

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()

    if time_now.hour >= sunset or time_now.hour <= sunrise:
        return True


#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
while True:
    time.sleep(60)
    if is_night() and iss_location():
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_gmail, password=gmail_pw)
            connection.sendmail(from_addr=my_gmail,
                                to_addrs="bowa41@att.net",
                                msg=f"Subject:Look Up!\n\nThe ISS is in view!")






