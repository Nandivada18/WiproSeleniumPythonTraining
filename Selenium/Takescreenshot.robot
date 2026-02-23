*** Settings ***
Library    SeleniumLibrary
Library    OperatingSystem
Library    Collections

*** Variables ***
${url}    https://the-internet.herokuapp.com/upload

*** Test Cases ***
Verify right click
    Open Browser    ${url}    chrome
    #maximize the browser window
    Maximize Browser Window
    #wait till the element is loaded
    Sleep    2s
    Wait Until Element Is Visible    xpath://input[@id='file-upload']
    #capture page screenshot
    Capture Page Screenshot    C://Users//prasa//Downloads//rs.jpg
    #capture element screenshot
    Capture Element Screenshot    xpath://input[@id='file-upload']  C://sers//prasa//Downloads//rs.jpg
    Sleep    2s
    #close browser
    Close Browser