# import smtplib
#
# my_email = "Gray24.Bulby37@gmail.com"
# password = "S3V4fZ(Tfo"
# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls()
#     connection.login(user= my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="Bulby37@yahoo.com",
#         msg="Subject:Hello\n\nThis is the body \nthe body is ready\nthe body is ready"
#     )
# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# if year == 2021:
#     print("Wear a facemask")
# day_of_week = now.weekday()
# print(day_of_week)
# date_of_birth = dt.datetime(year= 1984, month= 7, day= 21)
# print(date_of_birth)
import smtplib
import random
import datetime as dt
now= dt.datetime.now()
day = now.weekday()
my_email = "Gray24.Bulby37@gmail.com"
password = "S3V4fZ(Tfo"
if day==6:
    with open("quotes.txt") as quotes:
        all_quotes = quotes.readlines()
        sunday_quote= random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user= my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="Bulby37@yahoo.com",
            msg=f"Subject:Sunday Motivation\n\n{sunday_quote}"
    )
