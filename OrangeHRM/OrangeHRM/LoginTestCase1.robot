*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}         https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
${BROWSER}     chrome
${USERNAME}    Admin
${PASSWORD}    admin123

*** Test Cases ***
Testcase Verify Successful Employee Login

    [Documentation]    Verify Successful ESS Employee Login to OrangeHRM

    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Set Selenium Timeout    20s
    Wait Until Element Is Visible    xpath=//input[@name='username']
    Sleep    3s
    Input Text    xpath=//input[@name='username']    ${USERNAME}
    Sleep    2s
    Input Text    xpath=//input[@name='password']    ${PASSWORD}
    Sleep    2s
    Click Button    xpath=//button[@type='submit']
    Sleep    3s
    Wait Until Page Contains    Dashboard    20s
    Sleep    3s
    Page Should Contain    Dashboard
    Sleep    3s
    # Verify user dropdown visible
    Element Should Be Visible    xpath=//p[@class='oxd-userdropdown-name']

    Close Browser