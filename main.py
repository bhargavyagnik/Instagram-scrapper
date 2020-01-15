from selenium import webdriver
import os
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

chromedriver = "D:/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
class InstagramBot:
    def __init__(self, email, password):
        self.email = email
        self.password = password
    def login(self):
        url = "https://www.instagram.com/"

        driver.get(url)

        time.sleep(3)  # Waiting 3 seconds after we open the page.

        # Login element
        login = driver.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[2]/div[2]/p/a")
        login.click()
        time.sleep(2)

        username = driver.find_element_by_name("username")
        username.send_keys(self.email)

        password = driver.find_element_by_name("password")
        password.send_keys(self.password)

        # Logging in Instagram through our password and surname which is saved under loginInfo.py file.
        login_button = driver.find_element_by_xpath(
            "/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[4]/button")
        login_button.click()
        time.sleep(2)

    def follow(self):
        url="https://www.instagram.com/explore/people/suggested/"
        driver.get(url)
        time.sleep(3)
        while True:
            button=driver.find_elements_by_css_selector()
            button.click()
            time.sleep(3)
            # print(len(buttons))
            # for button in buttons :
            #     if button.text != "Following":
            #         button.click()
            #         time.sleep(2)
            # driver.find_element_by_tag_name('body').send_keys(Keys.END)
            time.sleep(3)


i=InstagramBot(email="bhukkhads_of_india",password="Bjty@906")
i.login()
i.follow()
