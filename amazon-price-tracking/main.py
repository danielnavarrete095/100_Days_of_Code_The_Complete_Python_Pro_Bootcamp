import requests
from bs4 import BeautifulSoup

ITEM_URL = "https://www.amazon.com.mx/dp/B00GLORM3M/?coliid=I2CZH0V16AVFWU&colid=5D8KJ0MDKAMZ&psc=1&ref_=lv_ov_lig_dp_it"

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.46",
    "Accept-Language":"en-US,en;q=0.9"
}
response = requests.get(ITEM_URL, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')
price = soup.select('span.a-price-whole')[0].text + soup.select('span.a-price-fraction')[0].text
print(price)
price = float(price)
print(price)