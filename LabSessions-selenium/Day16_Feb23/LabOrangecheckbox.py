import time
from itertools import count

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class Test_MultiSelectRadio:
    def test_multiradio(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

        time.sleep(5)
        # enter username
        name = driver.find_element(By.NAME, "username")
        name.send_keys("Admin")

        # enter password
        password = driver.find_element(By.NAME, "password")
        password.send_keys("admin123")

        time.sleep(4)
        # click on login button
        Login = driver.find_element(By.XPATH, "//button[normalize-space()='Login']")
        Login.click()
        time.sleep(5)
        #click on PIM
        PIM = driver.find_element(By.LINK_TEXT, "PIM")
        PIM.click()
        time.sleep(5)
        #click on check box one by one
        checkbox_list = driver.find_elements(By.XPATH, "//div[@role='checkbox']")
        count = len(checkbox_list)
        print(count)

        #Iterate the list
        for i in range(2, checkbox_list + 1):
            checkbox = driver.find_element(
                By.XPATH, f"(//div[@role='checkbox'])[{i}]"
            )

            driver.execute_script("arguments[0].scrollIntoView(true);", checkbox)
            time.sleep(1)

            driver.execute_script("arguments[0].click();", checkbox)
            time.sleep(1)
        #close only the current browser
        driver.close()