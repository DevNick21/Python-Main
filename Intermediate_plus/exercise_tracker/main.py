import requests
import os
import datetime
from dotenv import load_dotenv
load_dotenv()
nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/5a510fcbe773445a1f66413c0c7b2f57/myWorkouts/workouts"
headers = {
    "x-app-id": os.getenv("nutritionix_app_id"),
    "x-app-key": os.getenv("nutritionix_api_key"),
}
query = input("Tell me which exercise you did: ")


def get_data():
    nutritionix_params = {
        "query": query,
        "gender": "female",
        "weight_kg": 72.5,
        "height_cm": 167.64,
        "age": 30
    }

    res = requests.post(url=nutritionix_endpoint,
                        headers=headers, data=nutritionix_params)
    res.raise_for_status()
    data = res.json()["exercises"][0]
    exercise = data["name"].title()
    duration = data["duration_min"]
    calories = data["nf_calories"]
    return exercise, duration, calories


dt = datetime.datetime
today = dt.now()
todays_date = today.strftime("%d/%m/%Y")
current_time = today.strftime("%X")


def send_data():
    exercise, duration, calories = get_data()
    headers_sheety = {"Content-Type": "application/json",
                      "Authorization": os.getenv("sheety_authorization"),
                      }
    sheety_params = {
        "workout": {
            "date": todays_date,
            "time": current_time,
            "exercise": exercise,
            "duration": duration,
            "calories": calories
        }
    }

    res_sheety = requests.post(
        url=sheety_endpoint, json=sheety_params, headers=headers_sheety)
    res_sheety.raise_for_status
    print(res_sheety.text)


send_data()

# print(current_time)
