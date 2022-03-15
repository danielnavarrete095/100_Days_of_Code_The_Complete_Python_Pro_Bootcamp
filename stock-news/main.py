import datetime as dt
import requests
from keys import *

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
print(yesterday_close_price)
print(dby_close_price)
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
        print(top_results)
## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

