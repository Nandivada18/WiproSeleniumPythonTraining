import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage:
    # locators
    username_input = (By.XPATH, "//input[@id='user-name']")
    password_input = (By.XPATH, "//input[@id='password']")
    login_button = (By.XPATH, "//input[@id='login-button']")
    swag_text = (By.XPATH, "//div[@class='app_logo']")
    error_msg = (By.XPATH,"//h3[@data-test='error']")
    def __init__(self, driver):
        self.driver = driver

    # self.driver.find_element(self.username_input[0], self.username_input[1])
    # We use * to unpack the tuple.

    # enter username
    def enter_username(self, username):
        self.driver.find_element(*self.username_input).send_keys(username)
        time.sleep(1)

    # enter password
    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)
        time.sleep(1)

    # click on login button
    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def get_error_message(self):
        return self.driver.find_element(*self.error_msg).text
