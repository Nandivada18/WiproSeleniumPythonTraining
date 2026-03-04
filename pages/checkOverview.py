import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class OverviewPage:
    # locators
    finish = (By.XPATH, "//button[@id='finish']")
    def __init__(self, driver):
        self.driver = driver

    # click on finish button
    def click_finish(self):
        self.driver.find_element(*self.finish).click()
        time.sleep(1)

    def click_btn(self):
        self.click_finish()