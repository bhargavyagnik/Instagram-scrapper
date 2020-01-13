from selenium import webdriver
import time
import os

chromedriver = "D:/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
browser = webdriver.Chrome(chromedriver)
url = "https://www.instagram.com/"

browser.get(url)

time.sleep(3)  # Waiting 3 seconds after we open the page.

# Login element
login = browser.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[2]/div[2]/p/a")
login.click()
time.sleep(2)

username = browser.find_element_by_name("username")
username.send_keys("yagnikbhargav")

password = browser.find_element_by_name("password")
password.send_keys("bhargavyagnik13111999")

# Logging in Instagram through our password and surname which is saved under loginInfo.py file.
login_button = browser.find_element_by_xpath(
    "/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[4]/button")
login_button.click()
time.sleep(2)

browser.close()


