from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager
ORIGIN = "CUU"
#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()
# Get rows from google sheet
rows = data_manager.get_sheet_rows()
tomorrow = datetime.now() + timedelta(days=1)
six_months = tomorrow + timedelta(days=30*6)
# Check if rows have IATA code
for row in rows:
    code = row['iataCode']
    city = row['city']
    if not code:
        # Get code from flight search and fill each row
        iata_code = flight_search.get_iata_code(city)
        row['iataCode'] = iata_code
        # Update row in sheet
        body = {
            "price": {k:v for (k,v) in row.items() if k != "id"}
        }
        data_manager.update_row(row['id'], body)
    # Check for a cheap flight for each city
    found_flight = flight_search.get_flight_prices(ORIGIN, row['iataCode'], tomorrow, six_months, 10000)
    print(f"{found_flight.destination_city}: {found_flight.price}")
    # If found flight is cheaper than sheet's price, send a SMS/mail
    if found_flight.price < row['lowestPrice']:
        # notification_manager.send_flight_alert_sms(found_flight)
        notification_manager.send_flight_alert_mail(found_flight)


