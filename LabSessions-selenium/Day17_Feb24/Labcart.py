import os.path
import time
from itertools import count

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

class Test_Links:
    def test_Links(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        #navigation to url
        driver.get("https://demowebshop.tricentis.com/login")
        time.sleep(2)

        reg = driver.find_element(By.XPATH,"//input[@value='Register']")
        reg.click()
        time.sleep(2)

        radio = driver.find_element(By.XPATH, "//input[@id='gender-male']")
        radio.click()
        time.sleep(2)

        firstname = driver.find_element(By.XPATH, "//input[@id='FirstName']")
        firstname.send_keys("Prasad")
        time.sleep(2)
        lastname = driver.find_element(By.XPATH, "//input[@id='LastName']")
        lastname.send_keys("N")
        time.sleep(2)
        email = driver.find_element(By.XPATH, "//input[@id='Email']")
        email.send_keys("prasad9989@gmail.com")
        time.sleep(2)

        password = driver.find_element(By.XPATH, "//input[@id='Password']")
        password.send_keys("Pra@123")
        time.sleep(2)
        conpassword = driver.find_element(By.XPATH, "//input[@id='ConfirmPassword']")
        conpassword.send_keys("Pra@123")
        time.sleep(2)

        regbut = driver.find_element(By.XPATH, "//input[@id='register-button']")
        regbut.click()
        time.sleep(3)

        contin = driver.find_element(By.XPATH, "//input[@value='Continue']")
        contin.click()
        time.sleep(2)

        prd = driver.find_element(By.XPATH, "(//input[@value='Add to cart'])[2]")
        driver.execute_script("arguments[0].scrollIntoView();", prd)
        time.sleep(2)
        crt = driver.find_element(By.XPATH, "(//input[@value='Add to cart'])[2]")
        crt.click()
        time.sleep(2)

        prd = driver.find_element(By.XPATH, "//span[normalize-space()='Shopping cart']")
        driver.execute_script("arguments[0].scrollIntoView();", prd)
        time.sleep(2)
        crt = driver.find_element(By.XPATH, "//a[normalize-space()='shopping cart']")
        crt.click()
        time.sleep(2)

        box = driver.find_element(By.XPATH, "//input[@id='termsofservice']")
        box.click()
        time.sleep(2)
        checkout = driver.find_element(By.XPATH, "//button[@id='checkout']")
        checkout.click()
        time.sleep(2)

        dropdown = driver.find_element(By.XPATH, "//select[@id='BillingNewAddress_CountryId']")
        sel = Select(dropdown)
        sel.select_by_visible_text("India")
        time.sleep(2)
        city = driver.find_element(By.XPATH, "//input[@id='BillingNewAddress_City']")
        city.send_keys("RJY")
        addr = driver.find_element(By.XPATH, "//input[@id='BillingNewAddress_Address1']")
        addr.send_keys("B-11")
        Zip = driver.find_element(By.XPATH, "//input[@id='BillingNewAddress_ZipPostalCode']")
        Zip.send_keys("533105")
        phn = driver.find_element(By.XPATH, "//input[@id='BillingNewAddress_PhoneNumber']")
        phn.send_keys("1234567891")

        con = driver.find_element(By.XPATH, "//input[@onclick='Billing.save()']")
        con.click()
        time.sleep(2)

        clbox = driver.find_element(By.XPATH, "//input[@id='PickUpInStore']")
        clbox.click()
        time.sleep(2)
        cn = driver.find_element(By.XPATH, "//input[@onclick='Shipping.save()']")
        cn.click()
        time.sleep(2)
        cn2 = driver.find_element(By.XPATH, "//input[@class='button-1 payment-method-next-step-button']")
        cn2.click()
        time.sleep(2)
        cn3 = driver.find_element(By.XPATH, "//input[@class='button-1 payment-info-next-step-button']")
        cn3.click()
        time.sleep(2)

        cn4 = driver.find_element(By.XPATH, "//input[@value='Confirm']")
        cn4.click()
        time.sleep(3)

        driver.close()