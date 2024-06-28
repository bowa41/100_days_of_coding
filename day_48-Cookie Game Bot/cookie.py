from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

URL = "https://orteil.dashnet.org/experiments/cookie/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get(URL)


cookie = driver.find_element(By.ID, value="cookie")
store = driver.find_element(By.ID, value="store")
items = driver.find_elements(by=By.CSS_SELECTOR, value="#store div")

item_ids = [item.get_attribute("id") for item in items]
cost = [item.text.split("\n")[:2] for item in items]
cost = [price[0].split(" - ") for price in cost]
cost = [price[-1].replace(',', '') for price in cost]

store_dict = {
        item_ids[n] : cost[n] for n in range(len(item_ids)-1)
    }
print(store_dict)

timeout = time.time() + 5
five_min = time.time() + 60*5  # 5 minutes
buy_item = ""
n = 5
while True:
    cookie.click()

# Find current Money and check against store
    if time.time() > timeout:
        timeout += n
        money = driver.find_element(By.ID, value="money").text.replace(',', '')
        for name, price in store_dict.items():
            if int(money) > int(price):
                buy_item = name
        click_store = driver.find_element(By.ID, value=buy_item)
        click_store.click()
        n += 5
    if time.time() > five_min:
        cookie_per_s = driver.find_element(by=By.ID, value="cps").text
        print(cookie_per_s)
        break
driver.quit()
