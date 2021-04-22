from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import NoSuchElementException



class InternetSpeedTwitterBot:
    def __init__(self):
        self.chrome_driver_path = "/Users/jrlew/Development/chromedriver.exe"
        self.driver = webdriver.Chrome(executable_path=self.chrome_driver_path)
        self.down = 0
        self.up = 0

    def get_internet_speed(self, url):
        self.driver.get(url)
        go_button = self.driver.find_element_by_css_selector('#container > div > div.main-content > div > div > div > div.pure-u-custom-speedtest > div.speedtest-container.main-row > div.start-button > a')
        go_button.click()
        sleep(40)
        # close_popup = self.driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[8]/div/a/svg/use')
        # close_popup.click()
        download = self.driver.find_element_by_css_selector('#container > div > div.main-content > div > div > div > div.pure-u-custom-speedtest > div.speedtest-container.main-row > div.main-view > div > div.result-area.result-area-test > div > div > div.result-container-speed.result-container-speed-active > div.result-container-data > div.result-item-container.result-item-container-align-center > div > div.result-data.u-align-left > span')
        self.down =download.text
        upload = self.driver.find_element_by_css_selector('#container > div > div.main-content > div > div > div > div.pure-u-custom-speedtest > div.speedtest-container.main-row > div.main-view > div > div.result-area.result-area-test > div > div > div.result-container-speed.result-container-speed-active > div.result-container-data > div.result-item-container.result-item-container-align-left > div > div.result-data.u-align-left > span')
        self.up = upload.text
        print(self.down)
        print(self.up)


    def tweet_at_provider(self, login, password, down_target, up_target):
        if float(self.down) < down_target or float(self.up) < up_target:
            self.driver.get("https://www.twitter.com")
            sleep(5)
            twitter_login_button = self.driver.find_element_by_link_text("Log in")
            twitter_login_button.click()
            sleep(2)
            twitter_email_input = self.driver.find_element_by_css_selector('#react-root > div > div > div.css-1dbjc4n.r-13qz1uu.r-417010 > main > div > div > div.css-1dbjc4n.r-13qz1uu > form > div > div:nth-child(6) > label > div > div.css-1dbjc4n.r-18u37iz.r-16y2uox.r-1wbh5a2.r-1wzrnnt.r-1udh08x.r-iphfwy.r-s1qlax.r-ttdzmv > div > input')
            twitter_email_input.send_keys(login)
            twitter_password_input = self.driver.find_element_by_css_selector('#react-root > div > div > div.css-1dbjc4n.r-13qz1uu.r-417010 > main > div > div > div.css-1dbjc4n.r-13qz1uu > form > div > div:nth-child(7) > label > div > div.css-1dbjc4n.r-18u37iz.r-16y2uox.r-1wbh5a2.r-1wzrnnt.r-1udh08x.r-iphfwy.r-s1qlax.r-ttdzmv > div > input')
            twitter_password_input.send_keys(password)
            twitter_submit_button = self.driver.find_element_by_css_selector('#react-root > div > div > div.css-1dbjc4n.r-13qz1uu.r-417010 > main > div > div > div.css-1dbjc4n.r-13qz1uu > form > div > div:nth-child(8) > div > div')
            twitter_submit_button.click()
            sleep(5)
            twitter_tweet_text = self.driver.find_element_by_css_selector('#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > main > div > div > div > div.css-1dbjc4n.r-14lw9ot.r-1gm7m50.r-1ljd8xs.r-13l2t4g.r-1phboty.r-1jgb5lz.r-11wrixw.r-61z16t.r-1ye8kvj.r-13qz1uu.r-184en5c > div > div.css-1dbjc4n.r-14lw9ot.r-184en5c > div > div.css-1dbjc4n.r-14lw9ot.r-oyd9sg > div:nth-child(1) > div > div > div > div.css-1dbjc4n.r-1iusvr4.r-16y2uox.r-1777fci.r-1h8ys4a.r-1bylmt5.r-13tjlyg.r-7qyjyx.r-1ftll1t > div.css-1dbjc4n.r-184en5c > div > div > div > div > div > div > div > div > div > div.css-901oao.r-18jsvk2.r-6koalj.r-16y2uox.r-1qd0xha.r-adyw6z.r-16dba41.r-135wba7.r-bcqeeo.r-qvutc0 > div > div > div > div.DraftEditor-editorContainer > div > div > div > div')
            twitter_tweet_text.send_keys(f"My internet speed is {self.down} down and {self.up} up. \nThanks @CoxComm\nWe were supposed to make a complaint bot, but my speed is always consistent lol")
            tweet_button =self.driver.find_element_by_css_selector('#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > main > div > div > div > div.css-1dbjc4n.r-14lw9ot.r-1gm7m50.r-1ljd8xs.r-13l2t4g.r-1phboty.r-1jgb5lz.r-11wrixw.r-61z16t.r-1ye8kvj.r-13qz1uu.r-184en5c > div > div.css-1dbjc4n.r-14lw9ot.r-184en5c > div > div.css-1dbjc4n.r-14lw9ot.r-oyd9sg > div:nth-child(1) > div > div > div > div.css-1dbjc4n.r-1iusvr4.r-16y2uox.r-1777fci.r-1h8ys4a.r-1bylmt5.r-13tjlyg.r-7qyjyx.r-1ftll1t > div:nth-child(4) > div > div > div:nth-child(2) > div.css-18t94o4.css-1dbjc4n.r-urgr8i.r-42olwf.r-sdzlij.r-1phboty.r-rs99b7.r-1w2pmg.r-19u6a5r.r-ero68b.r-1gg2371.r-1ny4l3l.r-1fneopy.r-o7ynqc.r-6416eg.r-lrvibr > div')
            tweet_button.click()