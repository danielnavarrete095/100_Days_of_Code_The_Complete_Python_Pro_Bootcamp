import smtplib

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