import smtplib

from login_info import *

# SMTP_HOTMAIL = "smtp.live.com"
SMTP_HOTMAIL = "smtp.office365.com"
SMTP_GMAIL = "smtp.gmail.com"
SMTP_PORT = 587

# with smtplib.SMTP(SMTP_GMAIL, GMAIL_PORT) as connection:

#     connection.starttls()
#     connection.login(user=GMAIL_USER, password=GMAIL_PASSWORD)

#     connection.sendmail(from_addr=GMAIL_USER, to_addrs=HOTMAIL_USER, msg="Subject:Hello\n\nHello world! \nSending mail from python!")
    
with smtplib.SMTP(SMTP_HOTMAIL, PORT) as connection:

    connection.starttls()
    connection.login(user=HOTMAIL_USER, password=HOTMAIL_PASSWORD)

    connection.sendmail(from_addr=HOTMAIL_USER, to_addrs=GMAIL_USER, msg="Subject:Hello\n\nHello world! \nSending mail from python!")