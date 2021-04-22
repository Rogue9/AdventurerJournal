import datetime as dt
import pandas
import random
import smtplib

EMAIL = "Gray24.Bulby37@gmail.com"
PASSWORD = "S3V4fZ(Tfo"
today = dt.datetime.now()
today_tuple = (dt.datetime.now().month, dt.datetime.now().day)
data = pandas.read_csv("birthdays.csv")

birthdays_dict = {(data_row.month,data_row.day): data_row for index,data_row in data.iterrows()}
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        new_contents =contents.replace("[NAME]", birthday_person['name'])

    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(EMAIL,PASSWORD)
        connection.sendmail(from_addr=EMAIL,
                            to_addrs=birthday_person['email'],
                            msg=f"Happy Birthday!\n\n{new_contents}")

