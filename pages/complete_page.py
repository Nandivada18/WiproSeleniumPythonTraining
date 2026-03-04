import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class CompletePage:
    # locators
    tick = (By.XPATH, "//img[@alt='Pony Express']")
    backhome = (By.XPATH, "//button[@id='back-to-products']")

    def __init__(self, driver):
        self.driver = driver

    # click on back button
    def click_back(self):
        self.driver.find_element(*self.backhome).click()

    def click_btn(self):
        self.click_back()