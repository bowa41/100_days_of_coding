from selenium import webdriver
from selenium.webdriver.common.by import By

PRODUCT_URL = ("https://www.amazon.com/Sony-Premium-Compact-Digital-DSCRX100M4/dp/B00ZDWGM34/ref=sr_1_2?crid"
               "=120Y348AJM67M&dib=eyJ2IjoiMSJ9.mEjpvXr11-PKPYf30DNtCsrDhu9C7RVEmUSRh7EXqyTLArutdKNPUFbjyKF"
               "-2LPMXL2PtIvnBefeJSUuQ8b0hP1"
               "-947q9ARJoB_H5xxV5YHMLRmfReIO5jPMoermjxyvNjIwtVEpiqonpzQ49FV1E7otInvY7QHotBml"
               "-erk5z9A5ZsASMqadnA8aHF4zWv1VSlPfGTLdhnUq4OwiSIB5q65XsuWzwYqDBwFo"
               "-MZSmandiygbIjc87_5wuzWBabCu_QMvqDPtv9OdPLnXQMzev4_ACODUvkwjAbyj8PqObA"
               ".mw9ih0iMWUdEqGwepaVnvysZawHdaCl2rvOj6kgVKZQ&dib_tag=se&keywords=Sony%2BRX100%2BIV&qid=1719337299&s"
               "=electronics&sprefix=sony%2Brx100%2Biv%2Celectronics%2C185&sr=1-2&th=1")
PYTHON_URL = "https://www.python.org/"


# chrome_driver_path = r"C:\Users\bowa4\PycharmProjects\100_days_of_coding\chromedriver"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
# driver = webdriver.Chrome(service=webdriver.chrome.service.Service(executable_path=chrome_driver_path),
#                           options=chrome_options)
driver.get(PYTHON_URL)

# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
# print(f"The price is {price_dollar.text}.{price_cents.text}")

# #Find elements by name
# search_bar = driver.find_element(By.NAME, value="q")
# print(search_bar.tag_name)
# print(search_bar.get_attribute("placeholder"))
#
# #Find elements by ID
# button = driver.find_element(By.ID, value="submit")
# print(button.size)
#
# #Find elements by CSS Selector
# documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
# print(documentation_link.text)
#
# #Find elements by XPath
# path = driver.find_element(By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul')


#Pull upcoming events from python website Challenge
event_times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
event_descr = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")

# events = {}
# for n in range(len(event_times)):
#     events[n] = {
#         "time": event_times[n].text,
#         "name": event_descr[n].text,
#     }
events = { n: {
        "time": event_times[n].text,
        "name": event_descr[n].text
    }
    for n in range(len(event_times))
}
print(events)

# events = {action for elements in calendar_info}
# {}


#CLose 1 tab
# driver.close()

#Close entire browser
driver.quit()