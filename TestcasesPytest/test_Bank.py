import time
import pytest
from pages.Bank_page1 import LoginPage
from pages.Bank_page2 import ManagerPage
from pages.Bank_page3 import CustomerPage
from utilities.logger import get_logger
from utilities.excel_utils import get_excel_data
logger = get_logger()
test_data = get_excel_data("C://Users//prasa//PycharmProjects//SeleniumPytestPOM//testdata//login_data.xlsx", "Sheet1")

class TestLogin:
    # test data stored in excel sheet
    @pytest.mark.parametrize("First_name, Last_name , Post,Money,Full_name,Deposit,withdraw", test_data)
    def test_excel(self, driver,First_name, Last_name , Post,Money,Full_name,Deposit,withdraw):
        logger.info("Opening application")
        driver.get("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")
        time.sleep(3)
        login = LoginPage(self.driver)
        manager = ManagerPage(self.driver)
        customer = CustomerPage(self.driver)

        # Manager Login
        login.click_manager()
        time.sleep(2)

        # Add Customer
        manager.add_customer(First_name, Last_name, Post)
        time.sleep(2)

        # Open Account
        manager.open_account(Full_name, Money)
        time.sleep(2)

        # Back to Home
        customer.click_home()
        time.sleep(2)

        # Customer Login
        login.click_customer()
        customer.login(Full_name)
        time.sleep(2)

        # Deposit
        customer.deposit(Deposit)
        time.sleep(2)

        # Withdraw
        customer.withdraw(withdraw)
        time.sleep(2)

        # Validate Balance
        balance = customer.get_balance()
        assert int(balance) == 300
        time.sleep(2)