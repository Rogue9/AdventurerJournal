from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import NoSuchElementException

chrome_driver_path = "/Users/jrlew/Development/chromedriver.exe"
driver= webdriver.Chrome(executable_path=chrome_driver_path)

driver.get('https://tinder.com/')
sleep(3)
log_in = driver.find_element_by_css_selector("#t--942482051 > div > div.App__body.H\(100\%\).Pos\(r\).Z\(0\) > div > main > div.H\(100\%\) > div > div > div > div > header > div > div.H\(100\%\).D\(f\).Ai\(c\) > div.H\(40px\).Px\(28px\) > button")
log_in.click()
sleep(3)
facebook = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div/div[3]/span/div[2]/button')
facebook.click()
sleep(2)
base_window= driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)
email = driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/form/div/div[1]/div/input')
email.send_keys("bulby37@gmail.com")
password = driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/form/div/div[2]/div/input')
password.send_keys('AbbyFr33ks')
submit= driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/form/div/div[3]/label[2]')
submit.click()
sleep(30)
driver.switch_to.window(base_window)
agree = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div[1]/button')
agree.click()
sleep(1)
allow = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/button[1]/span')
allow.click()
sleep(1)
not_interested = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/button[2]/span')
not_interested.click()
sleep(1)
no_thanks = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/button/span')
no_thanks.click()
sleep(1)
window= driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/span[1]/div')
window.click()
for i in range(1, 11):
    no_button = driver.find_element_by_xpath('//*[@id="t--942482051"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[2]/div[2]/button')
    no_button.click()
    sleep(2)

