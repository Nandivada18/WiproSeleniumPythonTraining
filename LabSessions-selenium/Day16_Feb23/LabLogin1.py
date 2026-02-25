import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service = Service(GeckoDriverManager().install()))
driver.maximize_window()
driver.get('https://www.saucedemo.com/')

time.sleep(4)
#enter username
name = driver.find_element(By.NAME, "Username")
name.send_keys("standard_user")

#enter password
password = driver.find_element(By.NAME, "Password")
password.send_keys("secret_sauce")

time.sleep(4)
#click on login button
Login = driver.find_element(By.XPATH, "//button[normalize-space()='Login']")
Login.click()

assert "OrangeHRM" in driver.title