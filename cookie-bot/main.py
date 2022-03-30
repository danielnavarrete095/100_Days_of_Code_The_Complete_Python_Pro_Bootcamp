from posixpath import split
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

URL = "https://orteil.dashnet.org/cookieclicker/"
CHROME_DRIVER_PATH = r"C:\Users\danie\OneDrive\Documents\Software\chromedriver_win32\chromedriver"

driver = webdriver.Chrome(CHROME_DRIVER_PATH)

driver.get(URL)
cookie = driver.find_element(by=By.ID, value="bigCookie")
# for _ in range(1000):
while(True):
    current_cookies = driver.find_element(by=By.ID, value="cookies")
    try:
        current_cookies = current_cookies.text
    except:
        continue
    if 'cookie' in current_cookies:
        current_number_of_cookies = current_cookies.split("cookie")[0].strip().replace(",", "")
    else:
        continue
    try:
        current_number_of_cookies = int(current_number_of_cookies)
    except Exception as e:
        print(type(e))
        print(e)
        current_number_of_cookies = int(float(current_number_of_cookies) * 1000000)

    current_cookie_rate = current_cookies.split(":")[-1].strip()

    # print(f"Current cookies: {current_number_of_cookies}")
    # print(f"Current rate: {current_cookie_rate}")
    upgrades = driver.find_elements(by=By.CLASS_NAME, value="crate.upgrade.enabled")
    products = driver.find_elements(by=By.CLASS_NAME, value="product.unlocked")
    for upgrade in upgrades:
        upgrade.click()
        break
    product_lst = []
    for product in products:
        product_splitted = product.text.split('\n')
        name = product_splitted[0]
        price = int(product_splitted[1].replace(",", ""))
        product_lst.append({"name": name, "price": price})
    if product_lst:
        maxPricedItem = max(product_lst, key=lambda x:x['price'])
        if current_number_of_cookies > maxPricedItem["price"]:
            product.click()
    cookie.click()
driver.quit()