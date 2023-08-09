import requests
import os
from twilio.rest import Client
from dotenv import load_dotenv
load_dotenv()
OWM_URL = "https://api.openweathermap.org/data/2.8/onecall"
api_key = os.getenv("open_weather_api_key")
account_sid = os.getenv("twilio_account_sid")
auth_token = os.getenv("twilio_auth_token")
twilio_phone = os.getenv("twilio_phone")


LAT = os.getenv("MY_LAT")
LON = os.getenv("MY_LONG")
TOKEN = os.getenv("telegram_api_key")
CHAT_ID = os.getenv("my_telegram_chat_id")


def send_message(message):
    token = TOKEN
    chat_id = CHAT_ID
    url_req = "https://api.telegram.org/bot" + token + \
        "/sendMessage" + "?chat_id=" + chat_id + "&text=" + message
    res = requests.get(url_req)
    res.raise_for_status()
    print(res.text)


params = {
    "lat": LAT,
    "lon": LON,
    "appid": api_key,
    "exclude": "current,minutely,daily",
}

res = requests.get(OWM_URL, params=params)
res.raise_for_status()
data = res.json()

# print(data["hourly"][1]["weather"][0]["id"])

weather_codes = ["Rain" for code in range(
    12) if data["hourly"][code]["weather"][0]["id"] < 700]


if "Rain" in weather_codes:
    print(weather_codes)
    send_message("It is going to rain today Bring and umbrella ☔")
    # client = Client(account_sid, auth_token)

    # message = client.messages \
    #                 .create(
    #                     body="It is going to rain today Bring and umbrella ☔",
    #                     from_=twilio_phone,
    #                     to='+2348100839367'
    #                 )

    # print(message.status)
