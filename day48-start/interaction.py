from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "/Users/jrlew/Development/chromedriver.exe"
driver= webdriver.Chrome(executable_path=chrome_driver_path)

driver.get('https://orteil.dashnet.org/cookieclicker/')
# # article_count = driver.find_element_by_css_selector('#articlecount a')
# # print(article_count.text)
# # article_count.click()
# search = driver.find_element_by_name("search")
# search.send_keys("python")
# search.send_keys(Keys.ENTER)
while True:
    cookie= driver.find_element_by_id("bigCookie")
    cookie.click()
    for i in range (17,-1,-1):
        try:
            cookie.click()
            upgrade = driver.find_element_by_id(f"product{i}")
            cookie.click()
            cookie.click()
            cookie.click()
            upgrade.click()
            cookie.click()

        except:
            cookie.click()
            continue

    try:
        cookie.click()
        crate = driver.find_element_by_class_name(".crate upgrade")
        cookie.click()
        crate.click()
    except:
        cookie.click()
        continue