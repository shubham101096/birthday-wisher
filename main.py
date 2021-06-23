import smtplib
import datetime as dt
import pandas
import random
import os

EMAIL = os.environ.get('EMAIL')
PASSWORD = os.environ.get('PASSWORD')

print(EMAIL, PASSWORD)

data = pandas.read_csv("birthdays.csv")
data_dict = data.to_dict(orient="records")
print(data_dict)


for data in data_dict:
    if int(data["month"]) == dt.datetime.now().month and int(data["day"]) == dt.datetime.now().day:
        letter_no = random.randint(1,3)
        with open(f"letter_templates/letter_{letter_no}.txt") as file:
            letter = file.read()

        new_letter = letter.replace("[NAME]", data["name"])
        print(new_letter)

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(EMAIL, PASSWORD)
            connection.sendmail(EMAIL, data["email"],
                                f"Subject: Happy Birthday !! \n\n {new_letter}")




