from twilio.rest import Client
from flight_data import FlightData
from smtp import send_mail
from credentials import TWILIO_NUMBER, MY_NUMBER, GMAIL_USER, GMAIL_PASSWORD, HOTMAIL_USER, TWILIO_SID, TWILIO_TOKEN


class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self) -> None:
        self.client = Client(TWILIO_SID, TWILIO_TOKEN)
    def send_flight_alert_sms(self, flight:FlightData):
        message = f"Low price alert!\nOnly ${flight.price} to fly from {flight.origin_city}-{flight.origin_airport_code} to {flight.destination_city}-{flight.destination_airport_code}, from {flight.departure_date} to {flight.return_date}"
        sent = self.client.messages.create(
                    body = message,
                    from_ = TWILIO_NUMBER,
                    to = MY_NUMBER
                )
        return sent.status
    def send_flight_alert_mail(self, flight:FlightData):
        message = f"Low price alert!\nOnly ${flight.price} to fly from {flight.origin_city}-{flight.origin_airport_code} to {flight.destination_city}-{flight.destination_airport_code}, from {flight.departure_date} to {flight.return_date}"
        send_mail((GMAIL_USER, GMAIL_PASSWORD), HOTMAIL_USER, "Flight price alert! ✈", message)