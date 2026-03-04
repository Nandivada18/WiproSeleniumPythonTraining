import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class InfoPage:
    # locators
    first_name = (By.XPATH, "//input[@id='first-name']")
    last_name = (By.XPATH, "//input[@id='last-name']")
    zipcode = (By.XPATH, "//input[@id='postal-code']")
    cont = (By.XPATH, "//input[@id='continue']")
    def __init__(self, driver):
        self.driver = driver

    # enter frst name
    def enter_fname(self,fname):
        self.driver.find_element(*self.first_name).send_keys(fname)
        time.sleep(1)

    # enter last name
    def enter_lname(self, lname):
        self.driver.find_element(*self.last_name).send_keys(lname)
        time.sleep(1)

    def enter_zip(self,zcode ):
        self.driver.find_element(*self.zipcode).send_keys(zcode)
        time.sleep(1)

    # click on prd button
    def click_con(self):
        self.driver.find_element(*self.cont).click()

    def click_btn(self,fname,lname,zcode):
        self.enter_fname(fname)
        self.enter_lname(lname)
        self.enter_zip(zcode)
        self.click_con()