import requests
from keys import *

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
