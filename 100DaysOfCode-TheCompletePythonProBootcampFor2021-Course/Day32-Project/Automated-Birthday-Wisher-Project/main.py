##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import pandas as pd
import smtplib
import datetime as dt
import random

MY_EMAIL = "dummy_email@hotmail.com"
PASSWORD = "dummypass"

############## GETTING THE DATE FROM birthdays.csv ##############
df = pd.read_csv("birthdays.csv")

############## GETTING CURRENT DATE ##############
current_year = dt.datetime.now().year
current_month = dt.datetime.now().month
current_day = dt.datetime.now().day

print(current_day,current_month)

############## SENDING EMAIL ##############
for index,row in df.iterrows():
    if row["month"] == current_month and row["day"] == current_day:
        with smtplib.SMTP("smtp.office365.com:587") as connection:
            connection.starttls()

            connection.login(user=MY_EMAIL, password=PASSWORD)

            with open("letter_templates\\letter_" + str(random.randint(1,3)) + ".txt", "rt") as data_file:
                data = data_file.read()
                data = data.replace('[NAME]', row["name"])
                print(data)

            connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=row["email"],
            msg=f"Subject:Happy Birthday, {row['name']}\n\n{data}"
            )


