from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import NoSuchElementException

class Secretary:
    def __init__(self):
        self.chrome_driver_path = "/Users/jrlew/Development/chromedriver.exe"
        self.driver = webdriver.Chrome(executable_path=self.chrome_driver_path)

    def enter_data(self, url, data, len):
        for i in range(0, len):
            print(data[i])
            self.driver.get(url)
            sleep(1)
            address= self.driver.find_element_by_css_selector('#mG61Hd > div.freebirdFormviewerViewFormCard.exportFormCard > div > div.freebirdFormviewerViewItemList > div:nth-child(1) > div > div > div.freebirdFormviewerComponentsQuestionTextRoot > div > div.quantumWizTextinputPaperinputMainContent.exportContent > div > div.quantumWizTextinputPaperinputInputArea > input')
            address.send_keys(data[i][0])
            price = self.driver.find_element_by_css_selector('#mG61Hd > div.freebirdFormviewerViewFormCard.exportFormCard > div > div.freebirdFormviewerViewItemList > div:nth-child(2) > div > div > div.freebirdFormviewerComponentsQuestionTextRoot > div > div.quantumWizTextinputPaperinputMainContent.exportContent > div > div.quantumWizTextinputPaperinputInputArea > input')
            price.send_keys(data[i][1])
            link = self.driver.find_element_by_css_selector('#mG61Hd > div.freebirdFormviewerViewFormCard.exportFormCard > div > div.freebirdFormviewerViewItemList > div:nth-child(3) > div > div > div.freebirdFormviewerComponentsQuestionTextRoot > div > div.quantumWizTextinputPaperinputMainContent.exportContent > div > div.quantumWizTextinputPaperinputInputArea > input')
            link.send_keys(data[i][2])
            submit = self.driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div/div/span/span')
            submit.click()
            sleep(1)