import requests
from twilio.rest import Client
TWILIO_SID = "AC7e749c563a060f12580dbdb85a85cc03"
TWILIO_TOKEN = "edb8d0ad9b8583870dd4325f882729a9"
API_KEY = "4b19e39040fbf4a3cdecffc9f9800039"
MY_LONG = -106.052486
MY_LAT = 28.624353
OPEN_WEATHER_URL = "http://api.openweathermap.org/data/2.5/"
WEATHER_URL = OPEN_WEATHER_URL + "weather"
ONE_CALL_URL = OPEN_WEATHER_URL + "onecall"
req_params = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    # "q": "Chihuahua City",
    "appid": API_KEY,
    "units": "metric",
    "exclude": "current,minutely,daily"
}

response = requests.get(ONE_CALL_URL, params=req_params)
response.raise_for_status()
weather_data = response.json()["hourly"]
# print(weather_data)
weather_ids = [weather["weather"][0]["id"] for weather in weather_data][:12]
for id in weather_ids:
    # print(id)
    will_rain = False
    if id < 600:
        will_rain = True
        break
if will_rain:
    print("Bring an umbrella!")
    client = Client(TWILIO_SID, TWILIO_TOKEN)

    message = client.messages.create(
                                body='Bring an umbrella!',
                                from_='+19108124332',
                                to='+526142153664'
                            )

    print(message.status)