*** Settings ***
Library    SeleniumLibrary
Library    OperatingSystem
Library    Collections

*** Variables ***
${url}    https://practice.expandtesting.com/hovers

*** Test Cases ***
Verify right click
    Open Browser    ${url}    chrome
    #maximize the browser window
    Maximize Browser Window
    #wait till the element is loaded
    Sleep    2s
    Wait Until Element Is Visible    xpath://div[@class='container']//div[1]//img[1]
    Mouse Over    xpath://div[@class='container']//div[1]//img[1]
    Sleep    2s
    Element Should Be Visible    xpath://h5[normalize-space()='name: user1']
    #close browser
    Close Browser