from bs4 import BeautifulSoup
import requests
import lxml
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()
MY_GMAIL = os.getenv('MY_GMAIL')
GMAIL_PW = os.getenv('GMAIL_PW')

ACCEPT_LANG = "en-US, en;q=0.5"
USER_AGENT = ("Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) "
              "AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148")
PRODUCT_URL = ("https://www.amazon.com/Sony-Premium-Compact-Digital-DSCRX100M4/dp/B00ZDWGM34/ref=sr_1_2?crid"
               "=120Y348AJM67M&dib=eyJ2IjoiMSJ9.mEjpvXr11-PKPYf30DNtCsrDhu9C7RVEmUSRh7EXqyTLArutdKNPUFbjyKF"
               "-2LPMXL2PtIvnBefeJSUuQ8b0hP1"
               "-947q9ARJoB_H5xxV5YHMLRmfReIO5jPMoermjxyvNjIwtVEpiqonpzQ49FV1E7otInvY7QHotBml"
               "-erk5z9A5ZsASMqadnA8aHF4zWv1VSlPfGTLdhnUq4OwiSIB5q65XsuWzwYqDBwFo"
               "-MZSmandiygbIjc87_5wuzWBabCu_QMvqDPtv9OdPLnXQMzev4_ACODUvkwjAbyj8PqObA"
               ".mw9ih0iMWUdEqGwepaVnvysZawHdaCl2rvOj6kgVKZQ&dib_tag=se&keywords=Sony%2BRX100%2BIV&qid=1719337299&s"
               "=electronics&sprefix=sony%2Brx100%2Biv%2Celectronics%2C185&sr=1-2&th=1")


response = requests.get(PRODUCT_URL)
product_info = response.text

parameters = {
    "User-Agent": USER_AGENT,
    "Accept-Language": ACCEPT_LANG
}

response = requests.get(PRODUCT_URL, params=parameters)
amazon_page_info = response.text
soup = BeautifulSoup(amazon_page_info, "lxml")

try:
    price = (soup.find(name="span", class_="a-price-whole").getText().strip().
             replace('.', '').replace(',', ''))
except AttributeError:
    price = "NA"
title = soup.find(name="span", id="productTitle").getText().strip()
set_price = 1200

if int(price) < set_price:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_GMAIL, password=GMAIL_PW)
        connection.sendmail(from_addr=MY_GMAIL,
                            to_addrs="bowa41@att.net",
                            msg=f"Subject:AMAZON PRICE ALERT!\n\nThe price of {title} is {price}, and "
                                f"is below your set price of {set_price}\n"
                                f"Link to buy: {PRODUCT_URL}")
