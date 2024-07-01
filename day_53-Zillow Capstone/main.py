from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
import time

FORM_URL = "https://forms.gle/5giJsUyczky31dS66"
ZILLOW_URL = "https://appbrewery.github.io/Zillow-Clone/"

headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/120.0.0.0 Safari/537.36',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6'
        }
response = requests.get(ZILLOW_URL, headers=headers)
zillow_web_page = response.text
soup = BeautifulSoup(zillow_web_page, "html.parser")
# print(soup.prettify())

#Create list of addresses, links, and prices for each property
listing_address = soup.find_all(name="li", class_="ListItem-c11n-8-84-3-StyledListCardWrapper")
addresses = [address.find("address").getText().strip().replace("| ","") for address in listing_address]
print(addresses)

listing_links = soup.find_all(name="li", class_="ListItem-c11n-8-84-3-StyledListCardWrapper")
links = [link.find("a").get("href") for link in listing_links]
print(links)

listing_prices = soup.find_all('span', attrs={"data-test": "property-card-price"})
prices = [price.getText().split("+")[0].replace("/mo","") for price in listing_prices]
print(prices)

#Fill in google form to create spreadsheet
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get(FORM_URL)



for n in range(0, len(addresses)-1):
    time.sleep(1)
    address_entry = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]'
                                                           '/div/div[1]/div/div[1]/input')
    price_entry = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]'
                                                         '/div/div[1]/div/div[1]/input')
    link_entry = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]'
                                                        '/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]'
                                                           '/div/span/span')
    address_entry.send_keys(addresses[n])
    price_entry.send_keys(prices[n])
    link_entry.send_keys(links[n])
    submit_button.click()
    next_response = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    next_response.click()
driver.quit()