import requests
from credentials import SHEET_ENDPOINT, SHEETY_USERNAME, SHEETY_PASSWORD

headers = {
    "Content-Type": "application/json"
}
class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def get_sheet_rows(self):
        response = requests.get(SHEET_ENDPOINT, auth=(SHEETY_USERNAME, SHEETY_PASSWORD))
        # print(response.text)
        return response.json()['prices']
    def update_row(self, id, new_row):
        row_endpoint = f"{SHEET_ENDPOINT}/{id}"
        response = requests.put(row_endpoint, json=new_row, auth=(SHEETY_USERNAME, SHEETY_PASSWORD), headers=headers)
        # print(response.text)