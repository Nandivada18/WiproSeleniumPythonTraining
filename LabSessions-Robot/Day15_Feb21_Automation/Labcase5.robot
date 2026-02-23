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
    Wait Until Element Is Visible    xpath://h2[normalize-space()='New User Signup!']
    Input Text    xpath://input[@placeholder='Name']   Ravi
    Input Text    xpath://input[@data-qa='signup-email']     prasad12ddaa@gmail.com
    Click Element    xpath://button[normalize-space()='Signup']
    Wait Until Element Is Visible    xpath://p[normalize-space()='Email Address already exist!']
    #close browser
    Close Browser