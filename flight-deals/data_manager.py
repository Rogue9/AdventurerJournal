import requests
class DataManager:
    # This class is responsible for talking to the Google Sheet.

    def __init__(self):

        self.prices=[]
        self.sheety_get = "https://api.sheety.co/8fb7ddf47d238927d755d218416c6058/flightDeals/prices"
        self.sheety_put = "https://api.sheety.co/8fb7ddf47d238927d755d218416c6058/flightDeals/prices/"
        self.get_prices()



    def get_prices(self):

        self.sheety_response = requests.get(url=self.sheety_get)
        self.sheety_response.raise_for_status()
        self.sheet_data = self.sheety_response.json()



    def set_iata(self, id, code):
        self.put_url =f"{self.sheety_put}{id}"
        self.parameters = {
            "price": {
            "iataCode": f"{code}"
        }
        }
        self.headers= {
            "Content-Type":"application/json"
        }
        self.sheety_put_response = requests.put(url=self.put_url, json=self.parameters, headers=self.headers)
        self.sheety_put_response.raise_for_status()
        self.show=self.sheety_put_response.text
        print(self.show)
