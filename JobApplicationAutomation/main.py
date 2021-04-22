from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import NoSuchElementException

chrome_driver_path = "/Users/jrlew/Development/chromedriver.exe"
driver= webdriver.Chrome(executable_path=chrome_driver_path)

driver.get('https://www.linkedin.com/jobs/search/?geoId=103950076&keywords=python%20developer&location=Georgia%2C%20United%20States')
sign_in = driver.find_element_by_link_text("Sign in")
sign_in.click()
sleep(5)
username_input = driver.find_element_by_xpath('//*[@id="username"]')

username_input.send_keys("jrlewis84@gmail.com")
password_input = driver.find_element_by_id("password")
password_input.send_keys("Tigernach21")
password_input.send_keys(Keys.ENTER)
sleep(5)
all_listings = driver.find_elements_by_css_selector(".job-card-container--clickable")

for listing in all_listings:
    print("called")
    listing.click()
    sleep(2)

    try:
        apply_button = driver.find_element_by_css_selector(".jobs-s-apply button")
        apply_button.click()
        sleep(5)


        submit_button = driver.find_element_by_css_selector("footer button")

        if submit_button.get_attribute("data-control-name") == "continue_unify":
            close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
            close_button.click()
            sleep(2)
            discard_button = driver.find_elements_by_class_name("artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()
            print("Complex application, skipped.")
            continue
        else:
            submit_button.click()

        sleep(2)
        close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
        close_button.click()

    except NoSuchElementException:
        print("No application button, skipped.")
        continue

sleep(5)
driver.quit()