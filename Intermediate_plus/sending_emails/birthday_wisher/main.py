##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
import datetime as dt
import pandas
import random
import smtplib
import os
from email.message import EmailMessage
from dotenv import load_dotenv
load_dotenv()

MY_EMAIL = os.getenv("MY_EMAIL")
PASSWORD = os.getenv("EMAIL_PASSWORD")


birthday_df = pandas.read_csv("sending_emails/birthday_wisher/birthdays.csv")
birthday_data = birthday_df.to_dict(orient="records")

now = dt.datetime.now()

todays_date = (now.year, now.month, now.day)
random_number = random.randint(1, 3)


def send_mail(quote, email, name):
    msg = EmailMessage()
    msg.set_content(quote)

    msg['Subject'] = f'Happy Birthday {name}'
    msg['From'] = MY_EMAIL
    msg['To'] = email

    # Send the message via our own SMTP server.
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(MY_EMAIL, password=PASSWORD)
        server.send_message(msg)


for data in birthday_data:
    if (data["year"], data["month"], data["day"]) == todays_date:
        # print(data["name"])
        with open(f"sending_emails/birthday_wisher/letter_templates/letter_{random_number}.txt") as letter:
            template = letter.read()
            new_letter = template.replace("[NAME]", data['name'])
            send_mail(new_letter, data["email"], data["name"])
