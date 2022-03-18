from email import header
import requests
from flight_data import FlightData
from credentials import API_KEY, SEARCH_ENDPOINT, LOCATION_ENDPOINT

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self) -> None:
        self.headers = {
            "apiKey": API_KEY
        }
    def get_iata_code(self, city):
        params = {
            "term": city,
            "location_types": "city"
        }
        response = requests.get(LOCATION_ENDPOINT, params=params, headers=self.headers)
        first_location = response.json()['locations'][0]
        if first_location["name"] == city or city.lower() in first_location["slug"]:
            return first_location["code"]
    
    def get_flight_prices(self, origin, destination, date_min, date_max, max_price) -> FlightData:
        body = {
            "fly_from": f"city:{origin}",
            "fly_to": f"city:{destination}",
            "date_from": date_min.strftime('%d/%m/%Y'),
            "date_to": date_max.strftime('%d/%m/%Y'),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "curr": "MXN",
            "one_for_city": 1, # cheapest flight per destination
            "max_stopovers": 0 # Direct flight
        }
        response = requests.get(SEARCH_ENDPOINT, params=body, headers=self.headers)
        # print(response.text)
        flight = response.json()['data'][0] if response.json()['data'] else None
        if flight:
            if flight["price"] < max_price:
                my_flight = FlightData(
                    price=flight["price"],
                    origin_city=flight["cityFrom"],
                    origin_city_code=flight["cityCodeFrom"],
                    origin_airport=flight["flyFrom"],
                    destination_city=flight["cityTo"],
                    destination_city_code=flight["cityCodeTo"],
                    destination_airport=flight["flyTo"],
                    departure_date=flight["route"][0]["local_departure"].split("T")[0],
                    return_date = flight["route"][1]["local_departure"].split("T")[0],                    
                )
                return my_flight
        return None