import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import os
from selenium.webdriver.common.by import By
import selenium.common.exceptions
from selenium.webdriver.common.keys import Keys

def login():
    url = "https://www.instagram.com/"

    driver.get(url)

    time.sleep(3)  # Waiting 3 seconds after we open the page.

    # Login element
    login = driver.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[2]/div[2]/p/a")
    login.click()
    time.sleep(2)

    username = driver.find_element_by_name("username")
    username.send_keys("Insta_Username")

    password = driver.find_element_by_name("password")
    password.send_keys("Insta_password####")

    # Logging in Instagram through our password and surname which is saved under loginInfo.py file.
    login_button = driver.find_element_by_xpath(
        "/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[4]/button")
    login_button.click()
    time.sleep(2)


def igram_scrap(username=[], tag=[], max_comments=12, post_no=0):
    # set up chromedriver
    handle = []
    for x in username:
        handle.append(x)
    for x in tag:
        handle.append(str('explore/tags/' + x))
    if post_no>14:
        login()
    for x in handle:
        base_url = "https://www.instagram.com/"
        handle = x

        driver.get(base_url + handle)
        got=True
        while got:
            try:
                images = driver.find_elements_by_class_name("_bz0w")
                image_curr = images[post_no].find_element_by_tag_name("a").get_attribute("href")
                driver.get(image_curr)  # go to first picture
                got=False
            except Exception as e:
                driver.find_element_by_tag_name('body').send_keys(Keys.END)
        click_count = 0
        max_count = max_comments / 12

        while max_count > click_count:
            try:
                load_more = driver.find_element_by_css_selector(
                    "#react-root > section > main > div > div > article > div.eo2As > div.EtaWk > ul > li > div > button")
                load_more.click()
                click_count += 1
                time.sleep(1)
            except selenium.common.exceptions.StaleElementReferenceException:
                time.sleep(7)
            except Exception as e:
                print(e)
                break
        print(
            "final click count: " + str(click_count) + "; should yield roughly " + str(click_count * 12) + " comments")
        comments = driver.find_elements_by_class_name("C4VMK")

        comments_list, users_list = [], []

        for c in comments:
            comment = c.find_element_by_css_selector('span').get_attribute("textContent")
            user = c.find_element_by_class_name("TlrDj").get_attribute("textContent")
            print("" + user + ": " + str(comment))
            comments_list.append(comment)
            users_list.append(user)

        df = pd.DataFrame({"user": users_list, "comment": comments_list})
        if 'explore/tags/' in x:
            x = x.replace('explore/tags/', '')
        df.to_csv(str(x + ".csv"), index=False)

chromedriver = "D:/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
igram_scrap(username=['narendramodi'],  max_comments=200, post_no=20)

