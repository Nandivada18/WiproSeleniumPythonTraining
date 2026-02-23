*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}    https://www.tutorialspoint.com/selenium/practice/alerts.php

*** Test Cases ***
Verify drop downs
    Open Browser    ${url}    chrome
    #maximize the browser window
    Maximize Browser Window
    Wait Until Element Is Visible    xpath:(//button[@type='button'])[6]
    Click Element    xpath:(//button[@type='button'])[6]
    #Informational alert - accept is for ok button
    Handle Alert    action=ACCEPT
    Sleep    2s
    Click Element    xpath:(//button[@type='button'])[8]
    #Confirmational alert - accept is for ok button dismiss is for cancel button
    Handle Alert    action=DISMISS
    Sleep    2s
    Click Element    xpath:(//button[@type='button'])[9]
    #Prompt alert - accept is for ok button dismiss is for cancel button
    Input Text Into Alert    Hello
    Sleep    2s

    Close Browser