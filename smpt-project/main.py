import smtplib

from login_info import *

SMTP_HOTMAIL = "smtp.live.com"
SMTP_GMAIL = "smtp.gmail.com"
# smtp.office365.com

connection = smtplib.SMTP(SMTP_GMAIL)

connection.starttls()
connection.login(user=GMAIL_USER, password=GMAIL_PASSWORD)

connection.sendmail(from_addr=GMAIL_USER, to_addrs=HOTMAIL_USER, msg="Hello world! \nSending mail from python!")
connection.close()