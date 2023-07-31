import requests
from datetime import datetime
from email.message import EmailMessage
import smtplib
import time


MY_EMAIL = "iheanachoaustin07@gmail.com"
PASSWORD = ""

MY_LAT = 6.501240  # Your latitude
MY_LONG = 3.349788  # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

# Your position is within +5 or -5 degrees of the ISS position.


def position_check():
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True


def send_mail(email):
    msg = EmailMessage()
    msg.set_content("LOOK UP MY GUY")

    msg['Subject'] = f'ISS IS OVERHEAD'
    msg['From'] = MY_EMAIL
    msg['To'] = email

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(MY_EMAIL, password=PASSWORD)
        server.send_message(msg)


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get(
        "https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now()
    current_hour = time_now.hour
    if current_hour >= sunset or current_hour <= sunrise:
        return True

# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.


while True:
    time.sleep(60)
    if position_check() and is_night():
        send_mail("iheanacho.ekene@hotmail.com")
