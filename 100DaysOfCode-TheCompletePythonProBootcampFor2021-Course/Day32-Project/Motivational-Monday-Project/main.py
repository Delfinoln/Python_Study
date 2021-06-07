# import smtplib

# my_email = "dummy_email@hotmail.com"
# password = "dummy_pass"

# with smtplib.SMTP("smtp.office365.com:587") as connection:
#     # Encrypt the message
#     connection.starttls()

#     connection.login(user=my_email, password=password)

#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs=my_email,
#         msg="Subject:Hello\n\nThis is the body of my email"
#     )

#     connection.close()

# import datetime as dt

# now = dt.datetime.now()
# now = now.year

# print(now)

import pandas as pd
import smtplib
import datetime as dt
import random

MY_EMAIL = "dummy_email@hotmail.com"
PASSWORD = "dummy_pass"


df = pd.read_csv("quotes.txt", sep="\n")
#motivational_list = df.values.tolist()
motivational_list = [row[0] for index,row in df.iterrows()]

quote = random.choice(motivational_list)

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 0:
    with smtplib.SMTP("smtp.office365.com:587") as connection:
        connection.starttls()

        connection.login(user=MY_EMAIL, password=PASSWORD)

        connection.sendmail(
         from_addr=MY_EMAIL,
         to_addrs=MY_EMAIL,
         msg=f"Subject:Monday Motivation\n\n{quote}"
        )

print(quote)

