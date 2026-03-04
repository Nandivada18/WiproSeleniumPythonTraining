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
        driver.get("https://the-internet.herokuapp.com/tables")
        time.sleep(3)

        #no of rows
        rows = driver.find_elements(By.XPATH,"//table[@id = 'table1']/tbody/tr")
        for i in rows:
            print(i.text)
        time.sleep(2)

        #no of columns
        cols = driver.find_elements(By.XPATH, " //table[@id = 'table1']/tbody/tr[1]/td")
        for i in cols:
            print(i.text)
        time.sleep(2)

        #fetch the cell data
        celldata = driver.find_element(By.XPATH, "//table[@id = 'table1']/tbody/tr[3]/td[4]")
        assert "$100.00" in celldata.text

        driver.close()