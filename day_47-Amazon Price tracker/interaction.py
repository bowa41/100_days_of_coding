from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

URL = "https://en.wikipedia.org/wiki/Main_Page"
SIGNUP = ("https://secure-retreat-92358.herokuapp.com/")
FNAME = "Jordan"
LNAME = "Gans"
EMAIL = "bowa41@att.net"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get(SIGNUP)


# article_count = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/a[1]')
# # print(article_count.text)
# # article_count.click()
#
# #Find element by Link Text
# all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# # all_portals.click()
#
# #Find element and enter text
# search = driver.find_element(By.NAME, value="search")
# search.send_keys("Python", Keys.ENTER)
# # search.send_keys(Keys.ENTER)

fname = driver.find_element(By.NAME, value="fName")
# fname = driver.find_element(By.XPATH, value="/html/body/form/input[1]")
fname.send_keys(FNAME)

lname = driver.find_element(By.NAME, value="lName")
# lname = driver.find_element(By.XPATH, value="/html/body/form/input[2]")
lname.send_keys(LNAME)

email = driver.find_element(By.NAME, value="email")
# email = driver.find_element(By.XPATH, value="/html/body/form/input[3]")
email.send_keys(EMAIL)

submit = driver.find_element(By.CSS_SELECTOR, value="form button")
submit.click()

# driver.quit()