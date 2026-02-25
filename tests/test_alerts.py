import time
from itertools import count

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

class Test_Alerts:
    def test_alerts(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get("https://the-internet.herokuapp.com/javascript_alerts")
        time.sleep(4)
        # simple alert with ok button only
        # switch the control to alert
        simplealt = driver.find_element(By.XPATH, "//button[@onclick='jsAlert()']")
        simplealt.click()
        alt = driver.switch_to.alert
        time.sleep(2)
        alt.accept()#click on accept button
        time.sleep(2)

        #confirm alert with ok button and cancel
        #switch the control to alert
        confalt = driver.find_element(By.XPATH, "//button[@onclick='jsConfirm()']")
        confalt.click()
        alt = driver.switch_to.alert
        time.sleep(2)
        alt.dismiss() #click on cancel button
        time.sleep(2)

        #promptalert
        prompalt = driver.find_element(By.XPATH, "//button[@onclick='jsPrompt()']")
        prompalt.click()
        alt = driver.switch_to.alert
        alerttext = alt.text
        print(alerttext)
        alt.send_keys("test hello")
        time.sleep(2)
        alt.accept()
        time.sleep(2)

        driver.close()