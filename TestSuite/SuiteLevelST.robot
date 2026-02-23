*** Settings ***
#settings add the external library details , resources , setup and teardown commands
#Suite Setup These run only once Before all tests start
#Suite Teardown These run only once After all tests finish
Library     SeleniumLibrary
Resource        ./../Resources/Resources.robot
Suite Setup  Open DB
Suite Teardown  Close DB

*** Test Cases ***
#name of the testcase
Verify login with valid credentials
                Login

Verify Add to cart functionality
                Login

    Log     User selects the product
    Log     User add the product to the cart
    Log     user verifies that the product with details is added to the cart