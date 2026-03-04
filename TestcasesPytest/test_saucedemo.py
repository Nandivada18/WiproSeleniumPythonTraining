import time
import pytest
from pages.saucedemo_page import LoginPage
from pages.products_page import ProductPage
from pages.checkout_page import CheckoutPage
from pages.info_page import InfoPage
from pages.checkOverview import OverviewPage
from pages.complete_page import CompletePage
from utilities.logger import get_logger
from utilities.excel_utils import get_excel_data
logger = get_logger()
test_data = get_excel_data("C://Users//prasa//PycharmProjects//SeleniumPytestPOM//testdata//login_data.xlsx", "Sheet1")

class TestLogin:
    # test data stored in excel sheet
    @pytest.mark.parametrize("username, password , fname,lname,zcode", test_data)
    def test_excel(self, driver, username, password,fname,lname,zcode):
        logger.info("Opening application")
        driver.get("https://www.saucedemo.com/")
        time.sleep(3)
        # create the object of login_page
        logger.info("Giving Credentials")
        lp = LoginPage(driver)
        lp.login(username, password)
        time.sleep(2)

        #product
        logger.info("Selecting Product and add to cart")
        product = ProductPage(driver)
        product.click_btn()
        time.sleep(2)

        #checkout
        logger.info("checking product")
        check = CheckoutPage(driver)
        check.click_btn()
        time.sleep(2)

        #Info
        logger.info("Giving information")
        info = InfoPage(driver)
        info.click_btn(fname,lname,zcode)
        time.sleep(2)

        #Overview
        logger.info("Checking its Done")
        over = OverviewPage(driver)
        over.click_btn()

        time.sleep(3)
        assert "Swag Labs" in driver.title

        back = CompletePage(driver)
        back.click_btn()
        time.sleep(2)
        logger.info("Thanks Completed")