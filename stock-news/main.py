import datetime as dt
from numpy import percentile
import requests
from keys import *
from twilio.rest import Client
from smtp import send_mail

STOCK = "TSLA"
COMPANY_NAME = "Tesla"

STOCK_API = "https://www.alphavantage.co/query"


NEWS_API = "https://newsapi.org/v2/everything"


def get_trading_date(offset = 0):
    today = dt.datetime.today()
    #check for weekends
    offset_date = today - dt.timedelta(days = offset)
    while offset_date.isoweekday() in [6, 7]:
        offset +=1
        offset_date = today - dt.timedelta(days = offset)

    return ("{}-{:0>2}-{:0>2}".format(offset_date.year, offset_date.month, offset_date.day))


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
req_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY,
}
response = requests.get(STOCK_API, req_params)
response.raise_for_status()
stock_data = response.json()["Time Series (Daily)"]
yesterdays_date = get_trading_date(1)
day_before_yesterday_date = get_trading_date(2)
yesterday_close_price = float(stock_data[yesterdays_date]["4. close"])
dby_close_price = float(stock_data[day_before_yesterday_date]["4. close"])
threshold = yesterday_close_price * 0.03
delta = dby_close_price - yesterday_close_price
get_news = False
if abs(delta) > threshold:
    get_news = True

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
if get_news:
    req_params = {
        "function": "TIME_SERIES_DAILY",
        "q": COMPANY_NAME,
        "apikey": NEWS_API_KEY,
        "searchIn": "title",
        "from": day_before_yesterday_date,
        "language": "en",
        "sortBy": "publishedAt",
    }
    response = requests.get(NEWS_API, params=req_params)
    response.raise_for_status()
    total_results = response.json()["totalResults"]
    results = response.json()["articles"]
    if total_results > 3:
        top_results = results[:3]
        # print(top_results)
## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 
    icon = "🔺" if delta > 0 else "🔻"
    percentage = delta / dby_close_price * 100
    formated_text = f"{COMPANY_NAME} {icon}"
    formated_text += "{:.2f}%".format(percentage)
    subject = formated_text
    body = ""
    for article in top_results:
        body += f"Headline: {article['title']}\n"
        body += f"Brief: {article['description']}\n\n"
    formated_text += "\n\n" + body
    print(formated_text)
    twilio_client = Client(TWILIO_SID, TWILIO_TOKEN)

    message = twilio_client.messages.create(
                                body=formated_text,
                                from_='+19108124332',
                                to='+526142153664'
                            )

    print(message.status)
    # Send a mail with the percentage change and each article's title and description.

    send_mail([GMAIL_USER, GMAIL_PASSWORD], HOTMAIL_USER, subject, body)