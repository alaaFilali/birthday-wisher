import pandas
import datetime as dt
import smtplib
import random

email_addrs = "email of sender"
password = "pass of sender"


# 1. Update the birthdays.csv

data = pandas.read_csv("birthdays.csv")
now = dt.datetime.now()
for (index, value) in data.iterrows():
    name = value["name"]
    email = value.email
    year = value.year
    month = value.month
    day = value.day

# 2. Check if today matches a birthday in the birthdays.csv

    if now.year == year and now.month == month and now.day == day:


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

        with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as data_file:
            data = data_file.read()
            letter = data.replace("[NAME]", name)

# 4. Send the letter generated in step 3 to that person's email address.

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=email_addrs, password=password)
            connection.sendmail(
                from_addr=email_addrs,
                to_addrs=email,
                msg=f"Subject:Happy Birthday {name}\n\n{letter}"
            )


