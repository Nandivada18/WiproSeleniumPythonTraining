# selecting by visible text
# selecting by index
# selecting the value
*** Settings ***
Library    SeleniumLibrary
Library    OperatingSystem
Library    Collections

*** Variables ***
${url}    https://jqueryui.com/datepicker/

*** Test Cases ***
Verify Frames
    Open Browser    ${url}    chrome
    #maximize the browser window
    Maximize Browser Window
    #wait till the element is loaded
    Set Selenium Implicit Wait    2s
    Select Frame    xpath://iframe[@class='demo-frame']
    Sleep    2s
    Click Element    xpath://input[@id='datepicker']
    Sleep    2s
    Click Element    xpath://a[contains(text(),'21')]
    #close browser
    Close Browser