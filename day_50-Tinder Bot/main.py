from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
import time


URL = "https://tinder.com/"
EMAIL = "bottinder08@gmail.com"
PASS = "V2fv9c/XJWX,=*,"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get(URL)

login_1 = driver.find_element(by=By.XPATH, value='//*[@id="u-1419960890"]'
                                                 '/div/div[1]/div/main/div[1]/div/div/div/div/'
                                                 'header/div/div[2]/div[2]/a/div[2]/div[2]/div')
login_1.click()
time.sleep(3)
login_2 = driver.find_element(by=By.XPATH, value='//*[@id="u1146625330"]/div/div[1]/div/div[1]/div/div'
                                                 '/div[2]/div[2]/span/div[2]/button/div[2]/div[2]/div[2]/div/div')
login_2.click()

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)

#login to fb with email and password
email = driver.find_element(By.NAME, value="email")
email.send_keys(EMAIL)

PW = driver.find_element(By.NAME, value="pass")
PW.send_keys(PASS)
time.sleep(1)
submit = driver.find_element(By.NAME, value="login")
submit.click()

driver.switch_to.window(base_window)
time.sleep(3)

cookies = driver.find_element(by=By.XPATH, value='//*[@id="u1146625330"]/div/div[2]/'
                                                 'div/div/div[1]/div[1]/button/div[2]/div[2]/div')
cookies.click()
time.sleep(2)
location = driver.find_element(by=By.XPATH, value='//*[@id="u1146625330"]/div/div[1]/div'
                                                      '/div/div[3]/button[1]/div[2]/div[2]/div')
location.click()
time.sleep(2)

notification = driver.find_element(by=By.XPATH, value='//*[@id="u1146625330"]/div/div[1]'
                                                      '/div/div/div[3]/button[2]/div[2]/div[2]/div')
notification.click()
time.sleep(4)
swipe_nope = driver.find_element(by=By.XPATH, value='//*[@id="u-1419960890"]/div/div[1]/div/main/div[2]/'
                                                    'div/div/div[1]/div[1]/div/div[3]/div/div[2]/button/span/span/svg')
while True:
    try:
        swipe_nope = driver.find_element(by=By.XPATH, value='//*[@id="u-1419960890"]/div/div[1]/div/main/div[2]/'
                                                            'div/div/div[1]/div[1]/div/div[3]/div/div[2]/button/'
                                                            'span/span/svg')
        swipe_nope.click()

# If the Like button changes XPath after the first Like
    except NoSuchElementException:
        try:
            heart_icon = driver.find_element(By.XPATH, value="//*[@id='t2067052097']/div/div[1]/div/main/"
                                                             "div[1]/div/div/div[1]/div[1]/div/div[4]/div/"
                                                             "div[4]/button")
            heart_icon.click()
        # For "Add Tinder to your Home Screen" pop-up
        except ElementClickInterceptedException:
            not_interested_button = driver.find_element(By.XPATH, value="//*[@id='t338671021']/div/div/div[2]/button[2]/div[2]/div[2]/div")
            not_interested_button.click()

# driver.quit()