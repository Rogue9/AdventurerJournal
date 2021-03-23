import requests
from datetime import datetime
import smtplib
import time
MY_LAT = 32.601458 # Your latitude
MY_LONG = -83.655397 # Your longitude
EMAIL ="Gray24.Bulby37@gmail.com"
PASSWORD= "S3V4fZ(Tfo"
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.
def is_overhead():
    if (MY_LAT-5) <= iss_latitude <= (MY_LAT+5) and (MY_LONG-5) <= iss_longitude <= (MY_LONG+5):
        return True
    else:
        return False


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

time_now = datetime.now()
def sun_up():
    if sunrise <= time_now <= sunset:
        return True
    else:
        return False
while True:
    if is_overhead() == True and sun_up()== False:
        with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
            connection.starttls()
            connection.login(EMAIL, PASSWORD)
            connection.sendmail(from_addr=EMAIL,
                                to_addrs="jrlewis84@gmail.com",
                                msg="Look up!\n\nThe ISS is overhead")
    time.sleep(60)
#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



