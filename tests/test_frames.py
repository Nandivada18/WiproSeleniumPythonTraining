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
        driver.get("https://jqueryui.com/datepicker/")
        time.sleep(3)

        #frame = driver.find_element(By.XPATH, "//iframe[@class='demo-frame']")
        driver.switch_to.frame(0)

        datepicker  =driver.find_element(By.XPATH,"//input[@id='datepicker']")
        datepicker.click()

        driver.close()