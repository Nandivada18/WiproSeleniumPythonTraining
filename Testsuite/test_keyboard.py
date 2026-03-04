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
        driver.get("https://www.facebook.com/")
        time.sleep(4)
        actions = ActionChains(driver)
        email = driver.find_element(By.XPATH,"//input[@name = 'email']")
        password = driver.find_element(By.XPATH, "//input[@type='password']")

        seriesofactions = actions.move_to_element(email).key_down(Keys.SHIFT).send_keys("hello")
        seriesofactions.perform()
        time.sleep(2)
        action = actions.key_down(Keys.CONTROL).send_keys("a").send_keys("c").key_up(Keys.CONTROL)
        action.perform()
        time.sleep(2)
        passaction = actions.click(password).key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL)
        passaction.perform()

        time.sleep(3)
        driver.close()