import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.firefox import GeckoDriverManager
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException

class Test_Checkcart:

    def test_checkout(self):
        driver = None
        try:
            driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
            driver.maximize_window()
            driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
            time.sleep(3)

            #product
            try:
                driver.find_element(By.CLASS_NAME, "search-keyword").send_keys("Tomato")
                print("Product searched")
            except NoSuchElementException:
                print("Search box not found")
            time.sleep(3)

            #Add product to cart
            try:
                driver.find_element(By.XPATH, "//h4[text()='Tomato - 1 Kg']/following-sibling::div/button").click()
                print("Product added to cart")
            except NoSuchElementException:
                print("Failed to add product")
            time.sleep(2)

            #Click cart
            try:
                driver.find_element(By.CLASS_NAME, "cart-icon").click()
                print("Cart opened")
            except NoSuchElementException:
                print("Cart icon not found")
            time.sleep(2)

            #checkout
            try:
                driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
                print("Proceeding to checkout")
            except NoSuchElementException:
                print("Proceed to checkout button not found")
            time.sleep(3)

            #Place Order
            try:
                driver.find_element(By.XPATH, "//button[text()='Place Order']").click()
                print("Place Order clicked")
            except NoSuchElementException:
                print("Place Order button not found")
            time.sleep(3)
            #proceed
            try:
                dropdown = driver.find_element(By.TAG_NAME, "select")
                # select class is used for the dropdowns
                sel = Select(dropdown)
                # select by visible text or label
                sel.select_by_visible_text("India")
                time.sleep(2)
                checkbox = driver.find_element(By.XPATH, "//input[@type='checkbox']")
                checkbox.click()
                time.sleep(2)
                driver.find_element(By.XPATH, "//div[@class='brand greenLogo']").click()
                print("Proceed done ")
            except NoSuchElementException:
                print("Proceed button not found")
            time.sleep(3)

        except Exception as e:
            print(f"Test failed due to unexpected error: {e}")

        finally:
            driver.quit()