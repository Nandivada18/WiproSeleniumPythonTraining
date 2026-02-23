*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}    https://rahulshettyacademy.com/AutomationPractice/

*** Test Cases ***
Verify drop downs
    Open Browser    ${url}    chrome
    #maximize the browser window
    Maximize Browser Window
    Wait Until Element Is Visible    xpath://input[@id='alertbtn']
    Click Element    xpath://input[@id='alertbtn']
    Handle Alert    action=ACCEPT
    Sleep    2s
    Click Element    xpath://input[@id='confirmbtn']
    Handle Alert    action=ACCEPT
    Sleep    2s
    Close Browser