import requests
from bs4 import BeautifulSoup
from smtp import send_mail
from keys import *

# ITEM_URL = "https://www.amazon.com.mx/dp/B00GLORM3M/?coliid=I2CZH0V16AVFWU&colid=5D8KJ0MDKAMZ&psc=1&ref_=lv_ov_lig_dp_it"
# THRESHOLD_PRICE = 700
ITEM_URL = "https://www.amazon.com.mx/Kingston-HX-KB1SS2-LA-Teclado-Gamer/dp/B07HGM451V/?_encoding=UTF8&pd_rd_w=XzOwk&pf_rd_p=071bc561-9b74-43ec-a730-1961db87c1e6&pf_rd_r=D2XYEBH3SDH773EJA673&pd_rd_r=99a5c4bf-0b95-45a5-b76f-f767bdd83827&pd_rd_wg=PQOJO&ref_=pd_gw_ci_mcx_mr_hp_d"
THRESHOLD_PRICE = 2000

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.46",
    "Accept-Language":"en-US,en;q=0.9"
}
response = requests.get(ITEM_URL, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')
have_current_price = False
try:
    current_price = soup.select('span.a-price-whole')[0].text.replace(",", "") + soup.select('span.a-price-fraction')[0].text
    current_price = float(current_price)
    have_current_price = True
except Exception as e:
    print(type(e))
    print(e)

# Send an email if current_price is below threshold
if have_current_price:
    if current_price < THRESHOLD_PRICE:
        product_title = soup.select("span#productTitle")
        if product_title:
            product_title = product_title[0].text.strip()
        if not product_title:
            product_title = "Your item"
        message = f"The price for \"{product_title}\" just dropped below {THRESHOLD_PRICE}!\n Check it out at:\n {ITEM_URL}"
        send_mail((GMAIL_USER, GMAIL_PASSWORD), HOTMAIL_USER, "Price alert!", message)