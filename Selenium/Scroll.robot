*** Settings ***
Library    SeleniumLibrary
Library    OperatingSystem
Library    Collections

*** Variables ***
${url}    https://www.amazon.in/

*** Test Cases ***
Verify scroll
    Open Browser    ${url}    chrome
    #maximize the browser window
    Maximize Browser Window
    #wait till the element is loaded
    Set Selenium Implicit Wait    2s
    Scroll Element Into View    xpath://a[normalize-space()='Sell on Amazon']
    Sleep    2s
    Click Element    xpath://a[normalize-space()='Sell on Amazon']
    Title Should Be    Amazon.in: Selling on Amazon - Start Selling Now
    #close browser
    Close Browser
    