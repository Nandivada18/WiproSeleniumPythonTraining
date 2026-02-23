*** Settings ***
Library    SeleniumLibrary
Library    OperatingSystem
Library    Collections

*** Variables ***
${url}    https://www.tutorialspoint.com/selenium/practice/upload-download.php

*** Test Cases ***
Verify drop downs
    Open Browser    ${url}    chrome
    #maximize the browser window
    Maximize Browser Window
    #wait till the element is loaded
    Sleep    2s
    Wait Until Element Is Visible    xpath://input[@id='uploadFile']
    Choose File    xpath://input[@id='uploadFile']     C://Users//prasa//Downloads//rs.jpg
    #click the upload button
    Sleep    2s
    #close browser
    Close Browser