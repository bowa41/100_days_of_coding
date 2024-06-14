import requests
import os
from twilio.rest import Client
from datetime import datetime, timedelta

STOCK = "TSLA"
COMPANY_NAME = "Tesla"
ACCOUNT_SID = "AC7ca3204f75d05946ac69acc47d73794a"
AV_API_KEY = os.environ["AV_API_KEY"]
TWILIO_API_KEY = os.environ["OWM_API_KEY"]
NEWSAPI_API_KEY = os.environ["NEWSAPI_API_KEY"]
AV_ENDPOINT = "https://www.alphavantage.co/query"
NEWSAPI_ENDPOINT = "https://newsapi.org/v2/top-headlines"


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

today = (datetime.today().strftime('%Y-%m-%d'))
yesterday = (datetime.today() - timedelta(days=1)).strftime('%Y-%m-%d')
yyesterday = (datetime.today() - timedelta(days=2)).strftime('%Y-%m-%d')

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": {STOCK},
    "apikey": {AV_API_KEY},
    }


response = requests.get(AV_ENDPOINT, params=stock_params)
response.raise_for_status()
stock_data = response.json()

# stock_today = stock_data["Time Series (Daily)"][today]["4. close"]
stock_yesterday = stock_data["Time Series (Daily)"][yesterday]["4. close"]
stock_yyesterday = stock_data["Time Series (Daily)"][yyesterday]["4. close"]


difference = ((float(stock_yesterday) - float(stock_yyesterday)))
change_in_price = (abs(difference) / float(stock_yesterday)) * 100

if change_in_price > 5:

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

    news_params = {
        "q": {COMPANY_NAME},
        "pageSize": 3,
        "apiKey": {NEWSAPI_API_KEY},
        }

    response2 = requests.get(NEWSAPI_ENDPOINT, params=news_params)
    response2.raise_for_status()
    news_data = response2.json()
    delta = ""

    if difference < 0:
        delta = "🔻"
    else:
        delta = "🔺"

    body = []
    for n in range(0,3):
        body.append(f"{STOCK}: {delta}{round(change_in_price,2)}\n"
                    f"Headline: {news_data['articles'][n]['title']}\n"
                    f"Brief: {news_data['articles'][n]['description']}\n\n"
                    )



    ## STEP 3: Use https://www.twilio.com
    # Send a seperate message with the percentage change and each article's title and description to your phone number.


    client = Client("AC7ca3204f75d05946ac69acc47d73794a", "1487c4df2ced08a8905754dad6d82a90")

    message = client.messages.create(
        from_="+18556773383",
        body=f"{body[0]}{body[1]}{body[2]}",
        to="+18777804236"
    )

    print(message.status)

    # #Optional: Format the SMS message like this:
    # """
    # TSLA: 🔺2%
    # Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
    # Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to
    # file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height
    # of the coronavirus market crash.
    # or
    # "TSLA: 🔻5%
    # Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
    # Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to
    # file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height
    # of the coronavirus market crash.
    # """
    # #
