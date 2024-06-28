from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
import time

PROMISED_UP = 150
PROMISED_DOWN = 10

EMAIL = "bottinder08@gmail.com"
PASS = "sdfjkl@#$%lhjksdfg"
ST_URL = "https://www.speedtest.net/"
X_URL = "https://x.com/home"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

class InternetSpeedTwitterBot:
    def __init__(self, URL):
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.maximize_window()
        self.driver.get(URL)
        self.up = 0
        self.down = 0
        up = ''

    def get_internet_speed(self):
        time.sleep(2)
        self.start_test = self.driver.find_element(by=By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div'
                                                            '/div[2]/div[3]/div[1]/a/span[4]')
        self.start_test.click()
        time.sleep(40)
        self.up = self.driver.find_element(by=By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]'
                                                              '/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]'
                                                              '/div[1]/div/div[2]/span').text
        self.down = self.driver.find_element(by=By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]'
                                                                '/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]'
                                                                '/div[2]/div/div[2]/span').text
        self.driver.quit()

    def tweet_at_provider(self, DOWN, UP):
        self.clicker = self.driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div'
                                                                   '/div/div[1]/div[1]/div/div[3]/div[4]/a/div'
                                                                   '/span/span')
        self.clicker.click()
        time.sleep(3)
        self.login = self.driver.find_element(by=By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]'
                                                                 '/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]'
                                                                 '/label/div/div[2]/div/input')
        self.login.send_keys(EMAIL)
        try:
            self.next = self.driver.find_element(by=By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/'
                                                                    'div[2]/div/div/div[2]/div[2]/div/div/div/button[2]'
                                                                    '/div/span/span')
            self.next.click()
            time.sleep(2)

            self.pw = self.driver.find_element(by=By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]'
                                                                  '/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]'
                                                                  '/div/label/div/div[2]/div[1]/input')
            self.pw.send_keys(PASS)
            self.pw.click()
        except NoSuchElementException:
            self.username = self.driver.find_element(by=By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div'
                                                                        '/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/'
                                                                        'div/div[2]/label/div/div[2]/div/input')
            self.username.send_keys("@TinderBot465808")
            self.username.send_keys(Keys.ENTER)
            time.sleep(2)
            self.pw = self.driver.find_element(by=By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]'
                                                                  '/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]'
                                                                  '/div/label/div/div[2]/div[1]/input')
            self.pw.send_keys(PASS)
            self.pw.send_keys(Keys.ENTER)
        time.sleep(4)
        self.text = self.driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div'
                                                                '/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div'
                                                                '/div/div[2]/div[1]/div/div/div/div/div/div/div/div'
                                                                '/div/div/div/div[1]/div/div/div/div/div/div[2]/div'
                                                                '/div/div/div')
        self.text.send_keys(f"Why is my ISP delivering below the minimum specs? \n\nDownload Speed {DOWN}\n"
                            f"Upload Speed {UP}"
                            )
        self.post = self.driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/div/div/div[2]'
                                                                 '/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]'
                                                                 '/div/div/div/div[2]/div[2]/div[2]/div/div/div/button'
                                                                 '/div/span/span')
        self.post.click()


speed_bot = InternetSpeedTwitterBot(ST_URL)
speed_bot.get_internet_speed()

twitter_bot = InternetSpeedTwitterBot(X_URL)
twitter_bot.tweet_at_provider(speed_bot.up, speed_bot.down)





