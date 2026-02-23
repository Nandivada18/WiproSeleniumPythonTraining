*** Settings ***
Library    SeleniumLibrary
Library    OperatingSystem
Library    Collections

*** Variables ***
${url}    https://www.tutorialspoint.com/selenium/practice/droppable.php

*** Test Cases ***
Verify drop downs
    Open Browser    ${url}    chrome
    #maximize the browser window
    Maximize Browser Window
    #wait till the element is loaded
    Sleep    2s
    Wait Until Element Is Visible    xpath://p[normalize-space()='Drag me to my target']
    Sleep    2s
    Drag And Drop    xpath://p[normalize-space()='Drag me to my target']    xpath://p[normalize-space()='Drop here']
    Sleep    2s
    #close browser
    Close Browser