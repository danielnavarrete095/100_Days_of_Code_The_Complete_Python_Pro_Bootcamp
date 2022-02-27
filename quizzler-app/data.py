import requests

req_params = {
    "amount": 35,
    "category": 18,
    "type": "boolean",
}

response = requests.get("https://opentdb.com/api.php", req_params)
response.raise_for_status()
question_data = response.json()["results"]