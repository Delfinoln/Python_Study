import requests
import datetime as dt
import smtplib
import time

MY_EMAIL = "dummy_email@hotmail.com"
PASSWORD = "dummypass"

MY_LAT = -15.798085
MY_LONG = -47.923372

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}


##### Getting sunset hour to know if the sky is dark
response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()

sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0]) - 3  # Hour in UTC -3
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0]) - 3    # Hour in UTC -3

time_now = dt.datetime.now()

print(sunrise, sunset, time_now.hour)


##### Getting ISS position
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()

longitude = float(data["iss_position"]["longitude"])
latitude = float(data["iss_position"]["latitude"])

iss_position = (longitude, latitude)

print(iss_position)


##### If the ISS is close to my current position
#        and it is currently dark
#        Then send me an email to tell me to look up
#        Bonus: run teh code every 60 seconds

def is_close_n_dark():
    global iss_position, sunset, time_now

    if time_now.hour >= sunset and abs(iss_position[0] - MY_LAT) <= 5 and abs(iss_position[1] - MY_LONG) <= 5:
        return True
    else:
        return False

while True:
    if is_close_n_dark():
        with smtplib.SMTP("smtp.office365.com:587") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)

            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg=f"Subject:ISS is close!\n\nLook up!"
            )
    time.sleep(60)