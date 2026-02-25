import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException

class Test_Saucedemo:
    def test_checkout(self):
        try:
            driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
            driver.maximize_window()
            driver.get("https://www.saucedemo.com/")
            time.sleep(2)
            #Login
            try:
                driver.find_element(By.ID, "user-name").send_keys("standard_user")
                driver.find_element(By.ID, "password").send_keys("secret_sauce")
                driver.find_element(By.ID, "login-button").click()
            except NoSuchElementException:
                print("Login elements not found!")
            time.sleep(2)

            #Add product to cart
            try:
                product = driver.find_element(By.XPATH, "(//button[contains(@id,'add-to-cart')])[6]")
                driver.execute_script("arguments[0].scrollIntoView(true);", product)
                product.click()
                print("Product added to cart ")
            except NoSuchElementException:
                print("Failed to add product")
            time.sleep(2)
            #Go to cart
            try:
                cart = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
                cart.click()
            except NoSuchElementException:
                print("Cart icon not found")
            time.sleep(2)
            #Checkout
            try:
                driver.find_element(By.ID, "checkout").click()
            except NoSuchElementException:
                print("Checkout button not found")
            time.sleep(2)
            try:
                driver.find_element(By.ID, "first-name").send_keys("Prasad")
                time.sleep(2)
                driver.find_element(By.ID, "last-name").send_keys("N")
                time.sleep(2)
                driver.find_element(By.ID, "postal-code").send_keys("33333")
                time.sleep(2)
                driver.find_element(By.ID, "continue").click()
            except NoSuchElementException:
                print("Checkout form elements not found!")
            time.sleep(2)

            #Finish checkout
            try:
                driver.find_element(By.ID, "finish").click()
                print("Checkout completed successfully")
            except NoSuchElementException:
                print("Finish button not found!")
            time.sleep(2)
        except Exception as e:
            print(f"Test failed due to unexpected error: {e}")


        finally:
            driver.quit()