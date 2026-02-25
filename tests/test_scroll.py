import time
from itertools import count

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

class Test_Scroll:
    def test_sroll(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get("https://www.amazon.in/")
        time.sleep(4)
        amz = driver.find_element(By.XPATH, "//a[normalize-space()='Amazon Pay on Merchants']")
        driver.execute_script("arguments[0].scrollIntoView();",amz)
        time.sleep(2)
        amz.click()
        time.sleep(2)
        #vertical up scroll - x coordinates should be zero
        driver.execute_script("window.scrollBy(0, -1000)")
        time.sleep(2)
        #vertical down scroll
        driver.execute_script("window.scrollBy(0, 5000)")
        time.sleep(2)
        #close only the current browser
        driver.close()