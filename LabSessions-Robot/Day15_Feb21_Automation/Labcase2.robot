*** Settings ***
Library    SeleniumLibrary
Library    OperatingSystem
Library    Collections

*** Variables ***
${url}    http://automationexercise.com

*** Test Cases ***
Verify scroll
    Open Browser    ${url}    firefox
    #maximize the browser window
    Maximize Browser Window
    #wait till the element is loaded
    Set Selenium Implicit Wait    3s
    Wait Until Element Is Visible    xpath://a[normalize-space()='Home']
    Click Element    xpath://a[normalize-space()='Signup / Login']
    Wait Until Element Is Visible    xpath://h2[normalize-space()='Login to your account']
    Input Text    xpath://input[@data-qa='login-email']   prasad123ddaa@gmail.com
    Input Text    xpath://input[@placeholder='Password']     prasad@111
    Click Element    xpath://button[normalize-space()='Login']
    Wait Until Element Is Visible    xpath://li[10]//a[1]
    #close browser
    Close Browser