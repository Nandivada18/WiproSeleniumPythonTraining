
*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}    https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php

*** Test Cases ***
Verify drop downs
    Open Browser    ${url}    chrome
    #maximize the browser window
    Maximize Browser Window
    Wait Until Element Is Visible    id=state
    ${labels}=    Get Selected List Labels    id=state
    Log    ${labels}
    #select by label - visible text
    Select From List By Label    id=state   Uttar Pradesh
    Sleep    2s
    Wait Until Element Is Visible    xpath://select[@name='city']
    ${labels}=    Get Selected List Labels    xpath://select[@name='city']
    Log    ${labels}
    #select by label - visible text
    Select From List By Label    xpath://select[@name='city']   Lucknow
    Sleep    2s

    Close Browser