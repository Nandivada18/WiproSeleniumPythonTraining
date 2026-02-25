import time
from itertools import count

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager


class Test_Actions:
    def test_actions(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get("https://the-internet.herokuapp.com/upload")
        time.sleep(4)
        browse = driver.find_element(By.XPATH, "//input[@id='file-upload']")
        browse.send_keys("C://Users//prasa//Downloads//rs.jpg")
        time.sleep(2)
        upload = driver.find_element(By.XPATH, "//input[@id='file-submit']")
        upload.click()
        time.sleep(2)
        fileupload = driver.find_element(By.XPATH,"//h3[normalize-space()='File Uploaded!']" )
        assert fileupload.text == "File Uploaded!"
        time.sleep(3)
        driver.close()