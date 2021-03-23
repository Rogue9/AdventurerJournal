import requests
from pprint import pprint
from flight_data import FlightData
from datetime import *
from flight_search import FlightSearch
from data_manager import DataManager
TEQUILA_KEY = "M-PAffb7VkWHbJy9QZ668mS_jgR062ta"
sheety_header = {
    "Authorization": "Bearer 88%Tiger%88"
}
searcher = FlightSearch()
sheet=DataManager()
sheet_data =sheet.sheet_data
city_data = sheet_data["prices"]
today= datetime.now()
printer=FlightData()
half_year=today+timedelta(weeks=24)
future=half_year.strftime("%d/%m/%Y")
date=today.strftime("%d/%m/%Y")
# print(sheet_data["prices"][0]["city"])
#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
# for position in range(len(sheet_data["prices"])):

for city in city_data:
    target_price =city["lowestPrice"]
    if city["iataCode"]=="":
        id = city["id"]
        city["iataCode"] = searcher.check_iata(city['city'])
        code = city["iataCode"]
        sheet.set_iata(id=id, code=code)
    data = searcher.get_prices(date, future, city["iataCode"])
    if data is None:
        continue
    printer.print_price(data, target_price)

