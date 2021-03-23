import requests
from twilio.rest import Client

account_sid = "AC19f500636ea7b50d71ef1b374c93aa80"
auth_token = "006d579b8cba31be87c691f56301a0c8"
API_KEY="53e29212bec886d1ca12a11f51037cf2"
LONG= -83.5999
LAT = 32.621
parameters= {
    "lat": LAT,
    "lon": LONG,
    "exclude":"minutely,daily",
    "units":"imperial",
    "appid":API_KEY,
}
response =requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
weather_data=response.json()
will_rain=False
high =0
humidities = []
wind_speeds = []
wind_gust= 0
hourly_data= [weather_data["hourly"]]
hours = hourly_data[0][0:12]
low = hourly_data[0][0:12][0]["temp"]

for position in range(0,12):
    if hourly_data[0][0:12][position]["weather"][0]["id"]<=700:
        will_rain=True
    if hourly_data[0][0:12][position]["temp"]> high:
        high =hourly_data[0][0:12][position]["temp"]
    if hourly_data[0][0:12][position]["wind_gust"] > wind_gust:
        wind_gust = hourly_data[0][0:12][position]["wind_gust"]
    if hourly_data[0][0:12][position]["temp"]< low:
        low=hourly_data[0][0:12][position]["temp"]
    humidities.append(hourly_data[0][0:12][position]["humidity"])
    wind_speeds.append(hourly_data[0][0:12][position]["wind_speed"])
humid= round(sum(humidities)/len(humidities))
speed= round(sum(wind_speeds)/len(wind_speeds))
if will_rain==True:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body=f"High={high}, Low={low}, humidity avg={humid}, wind spd={speed}, gust of {wind_gust}. Expect rain!✯",
        from_='+12402582361',
        to='+14789199371'
    )

    print(message.status)
else:
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                         body=f"High={high}, Low={low}, humidity avg={humid}, wind spd={speed}, gust of {wind_gust}. No rain expected. ✯",
                         from_='+12402582361',
                         to='+14789199371'
                     )

    print(message.status)