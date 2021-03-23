import requests
from datetime import *
API_KEY ="c09466fd20ff8ae586d72396faa39d56"
APP_ID = "28518702"
nut_endpoint ="https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint="https://api.sheety.co/8fb7ddf47d238927d755d218416c6058/copyWorkouts/workouts"
headers = {
    "x-app-id" : APP_ID,
    "x-app-key": API_KEY,
}

exercise_input= input("What exercise did you do?\n")
parameters = {
    "query": exercise_input,
}

response=requests.post(url=nut_endpoint, json=parameters, headers=headers)
response.raise_for_status()
exercise_data= response.json()
loops=len(exercise_data["exercises"])
today= datetime.now()
time=today.strftime("%H:%M:%S")
date=today.strftime("%d/%m/%Y")
sheety_header = {
    "Authorization": "Bearer 88%Tiger%88"
}
print(exercise_data["exercises"][0]["name"])


for exercise in exercise_data:

    print(f"{position}, {exercise}, {duration}, {calories}")
    workout_parameters = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
     }
    sheety_response = requests.post(url=sheety_endpoint, json=workout_parameters, headers=sheety_header)
    sheety_response.raise_for_status()
# print(len(exercise_data["exercises"]))