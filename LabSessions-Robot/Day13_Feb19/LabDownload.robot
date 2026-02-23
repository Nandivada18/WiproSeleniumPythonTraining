*** Settings ***
Library    SeleniumLibrary
Library    OperatingSystem
Library    Collections

*** Variables ***
${url}    https://the-internet.herokuapp.com/download

*** Test Cases ***
Verify drop downs
    Open Browser    ${url}    chrome
    #maximize the browser window
    Maximize Browser Window
    Wait Until Element Is Visible    xpath://a[@href='download/bb.txt']
    Click Element    xpath://a[@href='download/bb.txt']
    Sleep    2s
    #check if the file is present in the folder
    ${files}=       List Files In Directory     C:\Users\prasa\Downloads
    List Should Contain Value      ${files}        bb.txt
    Sleep    2s
    #close browser
    Close Browser