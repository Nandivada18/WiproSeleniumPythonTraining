import os.path
import time
from itertools import count

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

class Test_Links:
    def test_Links(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        #navigation to url
        driver.get("https://trytestingthis.netlify.app/")
        time.sleep(3)
         #browser interaction
        title= driver.title
        print(title)

        url = driver.current_url
        print(url)

        #navigational commands
        driver.back()
        time.sleep(2)
        driver.forward()
        time.sleep(2)
        driver.refresh()
        time.sleep(2)
        driver.close()