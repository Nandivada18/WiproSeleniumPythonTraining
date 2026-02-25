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

DOWNLOAD_DIR = "C://Users//prasa//Downloads"
class Test_Actions:
    def test_actions(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get("https://the-internet.herokuapp.com/download")
        time.sleep(3)
        alert = driver.find_element(By.XPATH,"//a[normalize-space()='alert.jpeg']")
        alert.click()

        #verify file downloaded
        file_path = os.path.join(DOWNLOAD_DIR,"alert.jpeg")
        assert os.path.exists(file_path)
        time.sleep(3)
        driver.close()