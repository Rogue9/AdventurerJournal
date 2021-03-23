from twilio.rest import Client
import smtplib
import requests
class NotificationManager:

    def deal_alert(self, price, departure_city, departure_iata, arrival_city, arrival_iata, outbound, inbound):
        account_sid = "AC19f500636ea7b50d71ef1b374c93aa80"
        auth_token = "006d579b8cba31be87c691f56301a0c8"
        client = Client(account_sid, auth_token)

        message = client.messages \
            .create(
            body=f"Deal Alert✯ A flight from {departure_city} {departure_iata} to {arrival_city} {arrival_iata} has been found for {outbound} through {inbound}, price is {price}! What a hot deal",
            from_='+12402582361',
            to='+14789199371'
        )
        response=requests.get("https://api.sheety.co/8fb7ddf47d238927d755d218416c6058/flightDeals/users")
        response.raise_for_status()
        user_data=response.json()
        print("HOT DEAL TEXTED")
        for position in range(len(user_data)):
            user_email=user_data['users'][position]['email']
            EMAIL = "Gray24.Bulby37@gmail.com"
            PASSWORD = "S3V4fZ(Tfo"
            with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
                connection.starttls()
                connection.login(EMAIL, PASSWORD)
                connection.sendmail(from_addr=EMAIL,
                                    to_addrs=user_email,
                                    msg=f"Deal Alert\n\n A flight from {departure_city} {departure_iata} to {arrival_city} {arrival_iata} has been found for {outbound} through {inbound}, price is {price}! What a hot deal\nhttps://www.google.com/flights?hl=en#flt={departure_iata}.{arrival_iata}.{outbound}*{arrival_iata}.{departure_iata}.{inbound}",)
            print("HOT DEAL EMAILED")