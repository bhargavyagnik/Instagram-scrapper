# Instagram-comment-scrapper-using-python


While gathering Data from various social Media sites for my project in NLP, i found out that what my project aimed for, should target the audience on Instagram and hence I and my Friend Mohammed @github.com/momo1606 found out an amazing article on Medium that had solved this problem using Selenium and Beautiful Soup. So we reffered it and modified it to your best use for Instagram Scrapping.

```shell
pip install selenium
pip install beautifulsoup4
```

So for you to run this you need Selenium which is a tool for browser automation using python.(https://selenium-python.readthedocs.io/)
For this you need to install Chromedriver(https://chromedriver.chromium.org/) and save its path for futher use.
Then the next task is to 
try it out if Selenium is working properly

```python
from selenium import webdriver
import os
chromedriver = "D:/chromedriver"  #Path for Chrome Driver
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.get("https://github.com/bhargavyagnik")
```

This will open the browser and load the following link...
Now it comes to a difficult part that is much more complex for a pythongeek while here comes a part of a web developer to get the post classes and get its addresses and click buttons etc...

As instagram shows multiple of 12 comments at a time , you'll find out 12 in many snippets of the code . So we need to click button with the class *"#react-root > section > main > div > div > article > div.eo2As > div.EtaWk > ul > li > div > button"* we'll search it using css selector . There are various selector you can find out in the documentation of selenium , you may fiddle with it and try different options and get the class names in Inspect element of the browser


Once the path for the button is obtained , we just apply a click action on the button and hence load more comments. Delay time depends on your internet speed and ping. So we kept ideal 1 sec or you can increase it if you have slower internet.

``` python
def igram_scrap(username=[], tag=[], max_comments=12, post_no=0):
```
- Input the list of usernames you want to scrap
- Input Tags you want to scrap 
- Input the Max comments 
- Input Post no.  basically starting with 0(most recent post) and till n. 
 
 
The project is still in development and one can take a list of desired posts, etc permutations, but i hope you enjoy the usage of amaznig project./..

The final comments will be printed in the console as well as that would be saved in **.csv** format with respective usernames. 

The usage of this scrapper is to get Instagram comments and use for -
- For finding Support to Political leaders and can be done to perdict if the people will vote him in the next election or not
- Predicting Movie Reviews, earnings etc
- For blocking such comments by Instagram to Prevent Abuse on Social Media
- Predicting types of comments etc

Update- Scroll with no max. limit. i.e you can get more posts no limited to 14 and time is reduced to a great extent

* Update
Now you can find a auto-follower bot in the main.py 

