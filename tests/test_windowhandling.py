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
        driver.get("https://the-internet.herokuapp.com/windows")
        time.sleep(3)

        clickhere = driver.find_element(By.XPATH, "//a[normalize-space()='Click Here']")
        clickhere.click()

        #fetch the window handles of both tabs
        windows = driver.window_handles
        print(windows)
        #move the control to the child window
        driver.switch_to.window(windows[1])

        text  =driver.find_element(By.XPATH,"//h3[contains(text(),'New Window')]")
        print(text)
        driver.close()
        #get back to parent window
        driver.switch_to.window(windows[0])
        clickhere.is_displayed()

        time.sleep(2)
        driver.close()