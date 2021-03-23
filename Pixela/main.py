import requests
from datetime import datetime

USERNAME= "bulby37"
TOKEN= "B00tsW1tDaFur"
GRAPH_ID="graph1"
pixela_endpoint ="https://pixe.la/v1/users"

parameters= {
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"

}

headers= {
    "X-USER-TOKEN": TOKEN
}
#
# response =requests.post(url=pixela_endpoint, json=parameters)
# print(response.text)
#
# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
#
# graph_config= {
#     "id": GRAPH_ID,
#     "name": "Cycling Graph",
#     "unit": "Km",
#     "type": "float",
#     "color": "ajisai"
# }
# headers= {
#     "X-USER-TOKEN": TOKEN
# }
# response= requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
today= datetime(year=2021, month=3, day=18)
# today= datetime.now()

pixel_params={
    "quantity": "25.0"
}
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
response= requests.delete(graph_endpoint, headers=headers)
print(response.text)
