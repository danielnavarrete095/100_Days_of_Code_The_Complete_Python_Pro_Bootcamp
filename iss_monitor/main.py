import requests
from datetime import datetime, timezone
from smtp import *
from login_info import *
import time
MY_LAT = 28.644100
MY_LONG = -106.073230

def get_sunrise_sunset():
    params = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("http://api.sunrise-sunset.org/json", params=params)
    response.raise_for_status()
    sunrise = response.json()["results"]["sunrise"].split("T")[1].split("+")[0]
    sunset = response.json()["results"]["sunset"].split("T")[1].split("+")[0]
    print(f"sunrise: {sunrise}")
    print(f"sunset: {sunset}")
    return (sunrise, sunset)


def get_current_time_utc():
    time_now = str(datetime.now(timezone.utc).time()).split(".")[0]
    print(f"current time: {time_now}")
    return time_now

def is_night():
    sunrise, sunset = get_sunrise_sunset()
    # current = "12:00:00"
    current = get_current_time_utc()
    sunrise = int(sunrise.replace(":", ""))
    sunset = int(sunset.replace(":", ""))
    current = int(current.replace(":", ""))
    print(sunrise)
    print(sunset)
    print(current)
    if sunset < current < sunrise:
        return True
    return False

def get_iss_position():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    print(response.status_code)
    data = response.json()
    print(data["iss_position"])
    longitude = data["iss_position"]["longitude"]
    latitude = data["iss_position"]["latitude"]
    iss_position = (float(latitude), float(longitude))
    print(iss_position)
    return iss_position

def is_iss_close():
    iss_lat, iss_lon = get_iss_position()
    print(iss_lat, iss_lon)
    print(MY_LAT, MY_LONG)
    if MY_LAT - 5 <= iss_lat <= MY_LAT + 5 and \
        MY_LONG - 5 <= iss_lat <= MY_LONG + 5:
        return True
    return False

def main():
    i = 0
    new_time = 0
    new_time = 0
    prev_time = 0
    while(True):
        new_time = time.perf_counter()
        if new_time >= prev_time + 60:
            prev_time = new_time
            if is_iss_close():
                if is_night():
                    subject = "Look to the sky!!"
                    message = "ISS is just passing above your location, it's dark and you may be able to see it!"
                else:
                    subject = "ISS passing by..."
                    message = "ISS is just passing above your location, althought you may not be able to see it"
                send_mail((GMAIL_USER, GMAIL_PASSWORD), HOTMAIL_USER, subject, message)

if __name__ == '__main__':
    main()