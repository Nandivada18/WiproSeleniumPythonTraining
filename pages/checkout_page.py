import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class CheckoutPage:
    # locators
    check_button = (By.XPATH, "//button[@id='checkout']")
    money_text = (By.XPATH, "//span[@class='title']")
    def __init__(self, driver):
        self.driver = driver

    # click on prd button
    def click_check(self):
        self.driver.find_element(*self.check_button).click()
        time.sleep(1)

    def click_btn(self):
        self.click_check()