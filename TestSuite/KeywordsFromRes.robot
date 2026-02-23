*** Settings ***
#settings add the external library details , resources , setup and teardown commands
Library     SeleniumLibrary
Resource        ./../Resources/Resources.robot

*** Test Cases ***
#name of the testcase
Verify login with valid credentials
                Login

Verify Add to cart functionality
                Login

    Log     User selects the product
    Log     User add the product to the cart
    Log     user verifies the product with details

