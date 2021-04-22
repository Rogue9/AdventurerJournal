from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from SpeedTweet import InternetSpeedTwitterBot
# chrome_driver_path = "/Users/jrlew/Development/chromedriver.exe"
# driver= webdriver.Chrome(executable_path=chrome_driver_path)

PROMISED_DOWN = 200
PROMISED_UP = 8
TWITTER_EMAIL= "jrlewis84@gmail.com"
TWITTER_PASSWORD = "Tw1tt3r37"
SPEEDTEST_URL = "https://www.speedtest.net/"
speeder_tweeter = InternetSpeedTwitterBot()
speeder_tweeter.get_internet_speed(SPEEDTEST_URL)
speeder_tweeter.tweet_at_provider(login=TWITTER_EMAIL,
                                  password=TWITTER_PASSWORD,
                                  down_target=PROMISED_DOWN,
                                  up_target=PROMISED_UP)
