import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class ProductPage:
    # locators
    prd_button = (By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
    cart_button = (By.XPATH, "//a[@class='shopping_cart_link']")
    money_text = (By.XPATH, "//div[@class='inventory_item_price']")
    def __init__(self, driver):
        self.driver = driver

    # click on prd button
    def click_prd(self):
        self.driver.find_element(*self.prd_button).click()
        time.sleep(1)

    # click on prd button
    def click_cart(self):
        self.driver.find_element(*self.cart_button).click()

    def click_btn(self):
        self.click_prd()
        self.click_cart()

