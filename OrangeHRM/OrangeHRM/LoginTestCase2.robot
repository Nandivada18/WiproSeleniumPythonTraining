*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}            https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
${BROWSER}        chrome
${VALID_USER}     Admin
${INVALID_PASS}   wrong123

*** Test Cases ***
Testcase Verify Error Message On Invalid Login

    [Documentation]    Verify error message when valid username and invalid password are used.

    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Set Selenium Timeout    20s
    Wait Until Element Is Visible    xpath=//input[@name='username']
    Sleep    3s
    Input Text    xpath=//input[@name='username']    ${VALID_USER}
    Sleep    3s
    Input Text    xpath=//input[@name='password']    ${INVALID_PASS}
    Sleep    3s
    Click Button    xpath=//button[@type='submit']
    Sleep    3s
    Wait Until Element Is Visible    xpath=//p[contains(@class,'oxd-alert-content-text')]
    Element Text Should Be    xpath=//p[contains(@class,'oxd-alert-content-text')]    Invalid credentials
    Page Should Not Contain    Dashboard

    Close Browser