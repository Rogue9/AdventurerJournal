##################### Extra Hard Starting Project ######################
import datetime as dt
import random
import smtplib
import pandas
templates = ["letter_templates/letter_1.txt", "letter_templates/letter_2.txt", "letter_templates/letter_3.txt"]
data= pandas.read_csv("birthdays.csv")
birthday_data=[]
now= dt.datetime.now()
today_date=(now.month, now.day)




birthdays = [(data.loc[position]["month"], data.loc[position]["day"]) for position in range(len(data.index))]



index_range= len(data.index)
for position in range(index_range):
    if data.loc[position]["month"]==now.month:
        if data.loc[position]["day"]==now.day:
            birthday_data.append(data.loc[position]["name"])
            template_choice= random.choice(templates)
            with open(template_choice) as body:
                for line in body:
                    email= body.readlines()
                    end_email="".join([name.replace("[NAME]", data.loc[position]['name']) for name in email])
                    print(data.loc[position]['name'])
            my_email = "Gray24.Bulby37@gmail.com"
            password = "S3V4fZ(Tfo"
            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(user= my_email, password=password)
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs=data.loc[position]["email"],
                    msg=f"Subject:Happy Birthday!\n\n{end_email}"
                )
            print(data.loc[position]["email"])


# name = data[data.name == 'John Boy']
# print(name)
# print(str(name.email))
# 1. Update the birthdays.csv CHECK

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




