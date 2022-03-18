class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, price, origin_city, origin_city_code, origin_airport, destination_city, destination_city_code, destination_airport, departure_date, return_date) -> None:
        self.price = price

        self.origin_city = origin_city
        self.origin_city_code = origin_city_code
        self.origin_airport_code = origin_airport
        
        self.destination_city = destination_city
        self.destination_city_code = destination_city_code
        self.destination_airport_code = destination_airport

        self.departure_date = departure_date
        self.return_date = return_date