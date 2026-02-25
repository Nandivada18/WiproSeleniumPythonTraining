import time
from itertools import count

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class Test_MultiSelectRadio:
    def test_multiradio(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get("https://testautomationpractice.blogspot.com/")

        #click on check box one by one
        checkbox_list = driver.find_elements(By.XPATH, "//input[@type = 'checkbox']")
        count = len(checkbox_list)
        print(count)

        #Iterate the list
        for i in checkbox_list:
            time.sleep(2)
            i.click()
            #close only the current browser
        driver.close()
