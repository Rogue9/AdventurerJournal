import notification_manager
class FlightData:
    def __init__(self):
        self.head=4
        self.texter=notification_manager.NotificationManager()

    def print_price(self, data, price):

        try:
            self.departure_city=data["data"][0]["cityFrom"]
            self.departure_city_iata=data["data"][0]["cityCodeFrom"]
            self.arrival_city=data["data"][0]["cityTo"]
            self.arrival_city_iata=data["data"][0]["cityCodeTo"]
            self.date_departure = data["data"][0]['route'][0]['local_departure'].split("T")
            self.date_return = data["data"][0]['route'][-1]['local_departure'].split("T")
            print(f'{data["data"][0]["cityTo"]}:{data["data"][0]["price"]} \nDeparture:{self.date_departure[0]}, Return:{self.date_return[0]}')
            self.target=int(price)
            self.actual=int(data["data"][0]["price"])

            if self.target>self.actual:
                print("HOT DEAL")
                self.texter.deal_alert(price=data["data"][0]["price"], departure_city=self.departure_city, departure_iata=self.departure_city_iata, arrival_city=self.arrival_city, arrival_iata=self.arrival_city_iata, outbound=self.date_departure[0], inbound=self.date_return[0])

        except IndexError:
            print(f"No flights found from {self.departure_city}")
            return None