import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class Test_AutomationPractice:
    def test_all_features(self):

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get("https://rahulshettyacademy.com/AutomationPractice/")
        time.sleep(3)

        #Class
        suggestion = driver.find_element(By.ID, "autocomplete")
        suggestion.send_keys("ind")
        time.sleep(2)
        options = driver.find_elements(By.CSS_SELECTOR, "li.ui-menu-item div")
        for option in options:
            if option.text == "India":
                option.click()
                break
        time.sleep(2)

        # Window
        driver.find_element(By.ID, "openwindow").click()
        time.sleep(3)

        parent = driver.current_window_handle
        windows = driver.window_handles

        for window in windows:
            if window != parent:
                driver.switch_to.window(window)
                break

        print("Switched Window Title:", driver.title)
        driver.close()
        driver.switch_to.window(parent)
        time.sleep(2)

        # Tab
        driver.find_element(By.ID, "opentab").click()
        time.sleep(3)

        tabs = driver.window_handles
        driver.switch_to.window(tabs[1])
        print("Switched Tab Title:", driver.title)
        driver.close()
        driver.switch_to.window(parent)
        time.sleep(2)

        #Alert
        name = driver.find_element(By.ID, "name")
        name.send_keys("Test")

        driver.find_element(By.ID, "alertbtn").click()
        time.sleep(2)

        alert = driver.switch_to.alert
        print("Alert Text:", alert.text)
        alert.accept()
        time.sleep(2)

        #Web Table
        rows = driver.find_elements(By.XPATH, "//table[@name='courses']//tr/td[2]")
        for row in rows:
            if "Advanced Selenium Framework Pageobject" in row.text:
                print("Course Found:", row.text)
        time.sleep(2)

        #Web Table Fixed Header (City = Chennai)
        city_rows = driver.find_elements(By.XPATH, "//div[@class='tableFixHead']//td[1]")
        for city in city_rows:
            if city.text == "Chennai":
                print("City Found:", city.text)
        time.sleep(2)

        # iFrame - Get Text
        driver.switch_to.frame("courses-iframe")
        time.sleep(2)

        # Get some visible text inside iframe
        text = driver.find_element(By.XPATH, "//a[contains(text(),'Courses')]").text
        print("iFrame Text:", text)

        driver.switch_to.default_content()
        time.sleep(2)

        #Mouse Hover
        hover = driver.find_element(By.ID, "mousehover")
        ActionChains(driver).move_to_element(hover).perform()
        time.sleep(2)

        top = driver.find_element(By.LINK_TEXT, "Top")
        top.click()
        time.sleep(2)

        print("Current URL after Top click:", driver.current_url)

        time.sleep(3)
        driver.quit()