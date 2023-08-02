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


# LAT = 6.501240
LAT = os.getenv("MY_LAT")
LON = os.getenv("MY_LONG")
# LON = 3.349788
params = {
    "lat": LAT,
    "lon": LON,
    "appid": api_key,
    "exclude": "current,minutely,daily",
}

res = requests.get(OWM_URL, params=params)
res.raise_for_status()
data = res.json()


weather_codes = ["Rain" for code in range(
    12) if data["hourly"][code]["weather"][0]["id"] < 700]

if "Rain" in weather_codes:
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body="It is going to rain today Bring and umbrella ☔",
                        from_=twilio_phone,
                        to='+2348100839367'
                    )

    print(message.status)
