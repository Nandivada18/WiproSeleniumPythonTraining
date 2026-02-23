*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}    https://www.saucedemo.com/

*** Test Cases ***
Verify checkout
    Open Browser    ${url}    chrome
    #maximize the browser window
    Maximize Browser Window
    Wait Until Element Is Visible    xpath://input[@id = 'user-name']
    Input Text    xpath://input[@id = 'user-name']    standard_user
    Input Text    xpath://input[@id = 'password']    secret_sauce
    Click Element    xpath://input[@id='login-button']
    Sleep    2s
    Click Element    xpath://a[@class='shopping_cart_link']
    Sleep    2s
    Click Element    xpath://button[@id='checkout']
    Sleep    2s
    Input Text    xpath://input[@id='first-name']    Prasad
    Input Text    xpath://input[@id='last-name']     N
    Input Text    xpath://input[@id='postal-code']   533105
    Click Element    xpath://input[@id='continue']
    Sleep    2s
    Click Element    xpath://button[@id='finish']
    Sleep    2s

    Close Browser