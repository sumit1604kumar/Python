# Email SMTP and date time Module
# Automated Birthday Wisher

import smtplib, random
import datetime as time
import pandas

data = pandas.read_csv("birthday.csv")
present_time = time.datetime.now()
present_month = present_time.month
date = present_time.day

PLACEHOLDER = "[NAME]"
today_tuple = (present_month, date)

my_email ="codergroup@gmail.com"
password = "nlyfbr"
subject = "Happy Birthday"
birthday_date = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthday_date:
    birthday_person = birthday_date[today_tuple]
    file_path = f"letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        content = letter_file.read()
        new_content = content.replace(PLACEHOLDER, birthday_person["name"])


    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthday_person["email"],
            msg=f"subject:{subject}\n\n{new_content}"
        )





