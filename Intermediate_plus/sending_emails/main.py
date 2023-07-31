import smtplib
from email.message import EmailMessage
import datetime as dt
import random

# Sender and Receiver Details
my_email = "iheanachoaustin07@gmail.com"
other_email = "iheanacho.ekene@hotmail.com"
password = "qgohhkcxjcbiyqxk"


# Reading Files
with open("birthday_wisher/quotes.txt", "r") as quote:
    list_of_quotes = quote.readlines()


# Random Quote Generator
new_quote = random.choice(list_of_quotes)

# Day
now = dt.datetime.now()
sunday_quote = now.weekday()


# Mail Sender
def send_mail():
    msg = EmailMessage()
    msg.set_content(new_quote)

    msg['Subject'] = 'Motivational Quote'
    msg['From'] = my_email
    msg['To'] = other_email

    # Send the message via our own SMTP server.
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(my_email, password=password)
        server.send_message(msg)


# Sending Mail
if sunday_quote == 6:
    send_mail()
