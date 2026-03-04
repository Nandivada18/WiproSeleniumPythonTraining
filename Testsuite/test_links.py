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
        driver.get("https://the-internet.herokuapp.com/download")
        time.sleep(3)
        links = driver.find_elements(By.TAG_NAME,"a")
        count = len(links)
        print(count)

        for link in links:
            print(link.text)
        time.sleep(2)
        driver.close()