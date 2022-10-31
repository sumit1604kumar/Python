# Application Programming Interface

import requests, smtplib
from datetime import datetime
MY_LAT = 9.7662
MY_LONG = -27.6553
my_email ="codergroup2021@gmail.com"
password = "nlyfbrpqc"
SENDER = ""
def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    print(iss_latitude, iss_longitude)

    if MY_LAT - 20 <= iss_latitude <= MY_LAT + 20 and MY_LONG - 20 <= iss_longitude <= MY_LONG + 20:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True




if is_iss_overhead() and is_night():
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=SENDER,
        msg=f"Subject: Look Up, \nInternational space station in the sky and crossing above Sydney at "
    )



