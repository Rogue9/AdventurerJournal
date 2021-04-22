from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException


CHROME_DRIVER_PATH = "/Users/jrlew/Development/chromedriver.exe"
SIMILAR_ACCOUNT = 'igndotcom'
USERNAME = "Bulby37"
PASSWORD= "1nstagram37"

class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

    def login(self):
        self.driver.get('https://www.instagram.com')
        sleep(2)
        login = self.driver.find_element_by_css_selector('#loginForm > div > div:nth-child(1) > div > label > input')
        login.send_keys(USERNAME)
        password= self.driver.find_element_by_css_selector('#loginForm > div > div:nth-child(2) > div > label > input')
        password.send_keys(PASSWORD)
        login_button = self.driver.find_element_by_css_selector('#loginForm > div > div:nth-child(3) > button')
        login_button.click()
        sleep(3)
        not_now = self.driver.find_element_by_css_selector('#react-root > section > main > div > div > div > div > button')
        not_now.click()
        sleep(3)
        not_again = self.driver.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div > div > div.mt3GC > button.aOOlW.HoLwm')
        not_again.click()
        sleep(3)
        self.find_followers()

    def find_followers(self):
        search =self.driver.find_element_by_css_selector('#react-root > section > nav > div._8MQSO.Cx7Bp > div > div > div.LWmhU._0aCwM > input')
        search.send_keys(SIMILAR_ACCOUNT)
        sleep(2)
        search.send_keys(Keys.ENTER)
        search.send_keys(Keys.ENTER)
        sleep(2)
        followers = self.driver.find_element_by_css_selector('#react-root > section > main > div > header > section > ul > li:nth-child(2) > a')
        followers.click()
        sleep(2)
        self.follow()



    def follow(self):
        follow_window = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')
        while True:
            follow_buttons =self.driver.find_elements_by_xpath('/html/body/div[5]/div/div/div[2]/ul/div/li/div/div[3]/button')
            for button in follow_buttons:
                try:
                    button.click()
                    sleep(3.5)
                except ElementClickInterceptedException:
                    cancel = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[2]')
                    cancel.click()
                    continue
            for i in range(10):
                self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", follow_window)




followbot= InstaFollower()
followbot.login()
