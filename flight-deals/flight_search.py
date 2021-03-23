import requests


class FlightSearch:
    def __init__(self):
        self.api_key ="M-PAffb7VkWHbJy9QZ668mS_jgR062ta"

        self.header = {
            "apikey": "M-PAffb7VkWHbJy9QZ668mS_jgR062ta"
        }
    def check_iata(self, city):
        self.parameters = {
            "term":f"{city}"
        }

        self.city=city
        self.tequila_response =requests.get(url="https://tequila-api.kiwi.com/locations/query", params=self.parameters, headers=self.header)
        self.tequila_response.raise_for_status()
        self.flight_data= self.tequila_response.json()
        self.iata = self.flight_data["locations"][0]["code"]

        return self.iata
    def get_prices(self, date, future, city):
        self.six_months_later=future
        self.params= {
            "fly_from":"city:ATL",
            "date_from":date,
            "date_to":future,
            "fly_to":city,
            "nights_in_dst_from":7,
            "nights_in_dst_to":28,
            "flight_type":"round",
            "curr":"USD",
            "one_for_city":1,
            "stop-overs":0,
            "via_city":""

        }
        self.tequila_response = requests.get(url="https://tequila-api.kiwi.com/v2/search", params=self.params, headers=self.header)
        self.tequila_response.raise_for_status()
        self.flight_data= self.tequila_response.json()
        print(self.flight_data)
        return self.flight_data

    #This class is responsible for talking to the Flight Search API.