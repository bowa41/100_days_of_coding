import smtplib
import datetime as dt
import random
import pandas

my_gmail = "bowatest41@gmail.com"
gmail_pw = "eciepvmumtvlsjnw"
PLACEHOLDER = "[NAME]"
COUNTER = 0

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
day = now.day
month = now.month

####Read CSV, create dictionary from dataframe##########
data = pandas.read_csv("birthdays.csv")
df = pandas.DataFrame(data)
today_bday = df[(df["month"] == month) & (df["day"] == day)]



# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

for name in today_bday["name"]:
    letter_num = random.randint(1,3)
    with open(f"./letter_templates/letter_{letter_num}.txt") as letter_file:
        letter = letter_file.read()
        new_letter = letter.replace(PLACEHOLDER, name)
    email = today_bday.loc[COUNTER,"email"]
    COUNTER += 1

    # 4. Send the letter generated in step 3 to that person's email address.
    ###########################Send Email to birthday recipient############

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_gmail, password=gmail_pw)
        connection.sendmail(from_addr=my_gmail,
                            to_addrs=email,
                            msg=f"Subject:Happy Birthday!\n\n{new_letter}")



