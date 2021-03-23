import requests
from datetime import date, timedelta
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
AV_KEY = "AIOGT8TS5YI80DPP"
NEWS_KEY = "8e988aba77ff49d6ad7dd1176bb7f91e"
account_sid = "AC19f500636ea7b50d71ef1b374c93aa80"
auth_token = "006d579b8cba31be87c691f56301a0c8"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
av_parameters= {
    "function":"TIME_SERIES_DAILY",
    "symbol": STOCK,
    "interval":"60min",
    "apikey":AV_KEY
}
news_parameters = {
    "apiKey": NEWS_KEY,
    "q": STOCK,
    "language": "en"
}
today= date.today()
yesterday = today - timedelta(days=1)
anteayer = today - timedelta(days=2)
response= requests.get("https://www.alphavantage.co/query", params=av_parameters)
response.raise_for_status()
stock_data= response.json()
news_response = requests.get("https://newsapi.org/v2/everything", params=news_parameters)
news_response.raise_for_status()
news = news_response.json()
news_slice = news["articles"][:3]
yesterday_price = float(stock_data["Time Series (Daily)"][f"{yesterday}"]["4. close"])
anteayer_price = float(stock_data["Time Series (Daily)"][f"{anteayer}"]["4. close"])

indicator = "▲"
percentage = round(abs((yesterday_price-anteayer_price)/anteayer_price)*100)
print (percentage)
if percentage <0:
    indicator = "▼"

if percentage > 5 or percentage < -5:
    for i in range(0,3):
        client = Client(account_sid, auth_token)

        message = client.messages \
            .create(
            body=f"{STOCK}: {indicator}{percentage}%\nHeadline: {news_slice[i]['title']}\nBrief: {news_slice[i]['description']}",
            from_='+12402582361',
            to='+14789199371'
        )

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.


## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

