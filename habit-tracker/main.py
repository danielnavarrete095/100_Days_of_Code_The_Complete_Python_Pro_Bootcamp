import requests
from keys import *
from datetime import datetime, timedelta

GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"
req_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(pixela_endpoint, json=req_params)
# response.raise_for_status()
# print(response.text)


graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
req_params = {
    "id": GRAPH_ID,
    "name": "Programming graph",
    "unit": "Hr",
    "type": "int",
    "color": "kuro",
}
headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(graph_endpoint, json=req_params, headers=headers)
# print(response.text)

add_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now() - timedelta(1)
# today = datetime(year=2022, month=2, day=15)

req_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "1",
}
# response = requests.post(add_pixel_endpoint, json=req_params, headers=headers)
# print(response.text)

req_params = {
    "quantity": "1",
}
update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
response = requests.put(update_pixel_endpoint, json=req_params, headers=headers)
print(response.text)

delete_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
response = requests.delete(delete_pixel_endpoint, headers=headers)
print(response.text)

