from selenium import webdriver

chrome_driver_path = "/Users/jrlew/Development/chromedriver.exe"
driver= webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org")
event_list = {}
for i in range(1,6):
    attempt =driver.find_element_by_xpath(f'//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li[{i}]/a')
    print(attempt.text)
    time =driver.find_element_by_xpath(f'//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li[{i}]/time')
    print(time.text)
    iteration = i-1
    event_list[iteration] = {"time": time.text, "name": attempt.text}
print(event_list)
driver.quit()