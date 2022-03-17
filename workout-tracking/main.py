import os
import requests
from datetime import datetime

from keys import *

natural_exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

header = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json",
}

params = {
    "query": "",
    "gender": "male",
    "weight_kg": 100,
    "height_cm": 185,
    "age": 26,
}

params["query"] = input("Write what you did in your workout session: ")

response = requests.post(natural_exercise_endpoint, json=params, headers=header)
response.raise_for_status()
print(response.text)

sheety_endpoint = SHEET_ENDPOINT

body = {
    "workout": {
        "date": "",
        "time": "",
        "exercise": "",
        "duration": "",
        "calories": "",
    },
}

header = {
    "Authorization": f"Bearer {TOKEN}"
}

today = datetime.now()
# Obtain date
body["workout"]["date"] = today.strftime("%x")

# Obtain time
body["workout"]["time"] = today.strftime("%X")

for exercise in response.json()["exercises"]:
    # Obtain Exercise
    body["workout"]["exercise"] = exercise["name"].title()
    print(f"exercise: {exercise['name']}")
    # Obtain Duration
    body["workout"]["duration"] = exercise["duration_min"]
    print(f"duration: {exercise['duration_min']}")
    # Obtain Calories
    body["workout"]["calories"] = exercise["nf_calories"]
    print(f"calories: {exercise['nf_calories']}")



    # Fill google sheet row
    # response = requests.post(sheety_endpoint, json=body, headers=header)
    response = requests.post(sheety_endpoint, json=body, auth=(USERNAME, PASSWORD))
    response.raise_for_status()
    print(response.text)
