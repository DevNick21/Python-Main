import math
import requests
import os
import datetime as dt
from twilio.rest import Client
from dotenv import load_dotenv
load_dotenv()

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
ALPHA_VANTAGE_URL = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY"
NEWS_API_URL = "https://newsapi.org/v2/everything"
params_av = {
    "symbol": STOCK,
    "apikey": os.getenv("alphavantage_api_key")
}
params_news = {
    "language": "en",
    "q": COMPANY_NAME,
    "apiKey": os.getenv("news_api_api_key"),
}
account_sid = os.getenv("twilio_account_sid")
auth_token = os.getenv("twilio_auth_token")
twilio_phone = os.getenv("twilio_phone")
# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

# STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

res = requests.get(url=ALPHA_VANTAGE_URL, params=params_av)
res.raise_for_status()
data = res.json()
required_days = list(data["Time Series (Daily)"])[:2]

required_data = [data["Time Series (Daily)"][day] for day in required_days]
yesterday_data = float(required_data[0]["4. close"])
before_yesterday_data = float(required_data[1]["4. close"])


def percentage_change():
    percentage = math.floor((before_yesterday_data -
                             yesterday_data) / yesterday_data * 100)
    if percentage > 2 or percentage < -2:
        if percentage > 0:
            return f"🔺" + f"   {str(percentage)}"
        else:
            return f"🔻" + f"   {str(percentage)}"


def send_news(news):
    # ! Twilio API no longer available, free trial exhausted
    # client = Client(account_sid, auth_token)

    # message = client.messages \
    #                 .create(
    #                     body=news,
    #                     from_=twilio_phone,
    #                     to='+2348100839367'
    #                 )

    # print(message.status)
    token = os.getenv("telegram_api_key")
    chat_id = os.getenv("my_telegram_chat_id")
    url_req = "https://api.telegram.org/bot" + token + \
        "/sendMessage" + "?chat_id=" + chat_id + "&text=" + news
    results = requests.get(url_req)
    print(results.status_code)


now = dt.datetime.now()
if now.weekday() == 5 or now.weekday() == 6:
    pass
else:
    if percentage_change() == None:
        pass
    else:
        percentage = percentage_change()
        r = requests.get(url=NEWS_API_URL, params=params_news)
        r.raise_for_status()
        data = r.json()
        try:
            articles = data["articles"][:3]
        except IndexError:
            pass
        else:
            main_message = [
                f"{STOCK}: {percentage}\nHeadline: {article['title']}\nBrief: {article['description']}\n" for article in articles]
            for message in main_message:
                send_news(message)
