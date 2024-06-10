import smtplib
import datetime as dt
import random

my_gmail = "bowatest41@gmail.com"
gmail_pw = "eciepvmumtvlsjnw"
#
my_att = "bowatest41@att.net"
# att_pw = "iariwcabpghnebjb"
#


now = dt.datetime.now()
# year = now.year
# month = now.month
# day = now.day
day_of_week = now.weekday()

if day_of_week == 4:
    with open("quotes.txt", "r") as file:
        quotes = file.readlines()
    quote_of_day = (random.choice(quotes))

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    # with smtplib.SMTP("smtp.mail.att.net", port=587) as connection:

        connection.starttls()
        connection.login(user=my_gmail, password=gmail_pw)
        # connection.login(user=my_att, password=att_pw)
        connection.sendmail(from_addr=my_gmail,
                            to_addrs=my_att,
                            msg=f"Subject:Quote of the day\n\n{quote_of_day}")