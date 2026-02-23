*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}    https://www.tutorialspoint.com/selenium/practice/check-box.php

*** Test Cases ***
Verify login scenario with valid credentials
    Open Browser    ${url}    chrome
    #maximize the browser window
    Maximize Browser Window
    #wait till the element  is loaded
    Wait Until Element Is Visible    xpath://a[normalize-space()='Check Box']
    #click on select
    Click Element    xpath://a[normalize-space()='Check Box']
    #click on box1
    Click Element    xpath://input[@id='c_bs_1']
    #click on box 2
    Click Element    xpath://input[@id='c_bs_2']
    #close browser
    Close Browser