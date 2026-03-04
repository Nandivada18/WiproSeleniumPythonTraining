import time
from itertools import count

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

class Test_Actions:
    def test_actions(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get("https://www.amazon.in/")
        time.sleep(4)
        actions = ActionChains(driver)
        bestsellers = driver.find_element(By.XPATH, "//a[normalize-space()='Bestsellers']")
        #double  click using actions class
        actions.double_click(bestsellers).perform()#double check
        time.sleep(2)
        driver.back()
        time.sleep(2)

        mobile = driver.find_element(By.XPATH,"//a[normalize-space()='Mobiles']")
        actions.context_click(mobile).perform()#right click
        time.sleep(2)

        # move to element
        primes = driver.find_element(By.XPATH, "//span[normalize-space()='Prime']")
        actions.move_to_element(primes).perform()
        time.sleep(2)

        fresh = driver.find_element(By.XPATH, "//span[normalize-space()='Fresh']")
        actions.click_and_hold(fresh).perform()
        time.sleep(2)
        #close only the current browser
        driver.close()

