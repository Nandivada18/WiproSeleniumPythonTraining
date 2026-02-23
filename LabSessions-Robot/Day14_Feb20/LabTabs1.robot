*** Settings ***
Library    SeleniumLibrary
Library    OperatingSystem
Library    Collections

*** Variables ***
${url}    https://rahulshettyacademy.com/AutomationPractice/

*** Test Cases ***
Verify links
    Open Browser    ${url}    chrome
    #maximize the browser window
    Maximize Browser Window
    #wait till the element is loaded
    Set Selenium Implicit Wait    2s
    Click Element    link=Open Tab
    @{windows}=   Get Window Handles
    Log To Console    ${windows}
    @{titles}=   Get Window Titles
    Log To Console    ${titles}
    Switch Window      title=QAClick Academy - A Testing Academy to Learn, Earn and Shine
    Wait Until Element Is Visible    xpath:(//img[@alt='Logo'])[1]
    Switch Window    MAIN
    #close browser
    Close Browser