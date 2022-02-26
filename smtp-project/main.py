import smtplib
import datetime as dt
from login_info import *
import random

# SMTP_HOTMAIL = "smtp.live.com"
SMTP_HOTMAIL = "smtp.office365.com"
SMTP_GMAIL = "smtp.gmail.com"
SMTP_PORT = 587

def send_mail(_from, _to, subject, message):
    if "@gmail" in _from[0]:
        smtp = SMTP_GMAIL
    else :
        smtp = SMTP_HOTMAIL

    with smtplib.SMTP(smtp, SMTP_PORT) as connection:

        connection.starttls()
        connection.login(user=_from[0], password=_from[1])

        connection.sendmail(from_addr=_from[0], to_addrs=_to, msg=f"Subject:{subject}\n\n{message}\n Sent from python!")

def get_date(year, month, day):
    day_of_birth = dt.datetime(year=year, month=month, day=day)
    return day_of_birth

def get_day_of_week():
    now = dt.datetime.now()
    day_of_week = now.weekday()
    days_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    return days_of_week[day_of_week]

def get_quote():
    with open("quotes.txt", "r") as file:
        lines = file.readlines()
        return random.choice(lines)
        
def main():
    # If current day is Friday
    if (get_day_of_week() == "Fri"):
        # Send an email with a motivational quote
        quote = get_quote()
        print(f"Sending mail to {HOTMAIL_USER}")
        send_mail((GMAIL_USER, GMAIL_PASSWORD), HOTMAIL_USER, "Quote of the day", quote)
        


if __name__ == '__main__':
    main()
