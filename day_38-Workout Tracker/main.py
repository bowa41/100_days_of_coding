import requests
import os
from datetime import datetime


APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")
ENDPOINT = os.environ.get("ENDPOINT")
SHEET_ENDPOINT = os.environ.get("SHEET_ENDPOINT")
TOKEN = os.environ.get("TOKEN")

GENDER = "male"
WEIGHT_KG = "65.7709"
HEIGHT_CM = "167.64"
AGE = "42"

user_params = {
  "query": input("What exercises did you do today?"),
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
  }

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}


response = requests.post(url=ENDPOINT, json=user_params, headers=headers)
exercise_data = response.json()

sheet_headers = {f"Authorization": f"Basic {TOKEN}"}

for n in range(0,(len(exercise_data["exercises"]))):
    exercise_date = (datetime.now().strftime("%Y-%m-%d"))
    exercise_time = (datetime.now().strftime("%H:%M:%S"))
    exercise = (exercise_data["exercises"][n]["name"].title())
    duration = (exercise_data["exercises"][n]["duration_min"])
    calories = (exercise_data["exercises"][n]["nf_calories"])

    sheet_params = {
      "workout": {
        "date": exercise_date,
        "time": exercise_time,
        "exercise": exercise,
        "duration": duration,
        "calories": calories,
        }
    }
    response = requests.post(url=SHEET_ENDPOINT, json=sheet_params, headers=sheet_headers)
    print(response.text)

