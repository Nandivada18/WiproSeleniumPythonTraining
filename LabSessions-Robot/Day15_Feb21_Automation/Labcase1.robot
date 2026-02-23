*** Settings ***
Library    SeleniumLibrary
Library    OperatingSystem
Library    Collections

*** Variables ***
${url}    https://automationexercise.com/

*** Test Cases ***
Verify scroll
    Open Browser    ${url}    chrome
    #maximize the browser window
    Maximize Browser Window
    #wait till the element is loaded
    Set Selenium Implicit Wait    3s
    Wait Until Element Is Visible    xpath://a[normalize-space()='Signup / Login']
    Click Element    xpath://a[normalize-space()='Signup / Login']
    Sleep    2s
    Input Text    xpath://input[@placeholder='Name']   prasad
    Input Text    xpath://input[@data-qa='signup-email']     prasad12ddaa@gmail.com
    Click Element    xpath://button[normalize-space()='Signup']
    Sleep    2s
    Wait Until Element Is Visible    xpath://b[normalize-space()='Enter Account Information']
    Click Element    xpath://input[@id='id_gender1']
    Sleep    2s
    Input Text    xpath://input[@id='password']  prasad@111
    Click Element    xpath://select[@id='days']/option[@value='29']
    Sleep    2s
    Click Element    xpath://select[@id='months']/option[@value='10']
    Sleep    2s
    Click Element    xpath://select[@id='years']/option[@value='2001']
    Sleep    2s
    Click Element    xpath://input[@id='newsletter']
    Sleep    2s
    Click Element    xpath://input[@id='optin']
    Sleep    2s
    Scroll Element Into View    xpath://input[@id='company']
    Input Text    xpath://input[@id='first_name']    prasad
    Input Text    xpath://input[@id='last_name']   N
    Scroll Element Into View    xpath://input[@id='company']
    Input Text    xpath://input[@id='company']    wipro
    Input Text    xpath://input[@id='address1']   a-b
    Scroll Element Into View    xpath://input[@id='state']
    Sleep    2s
    Input Text    xpath://input[@id='state']  AP
    Sleep    2s
    Input Text    xpath://input[@id='city']   RJY
    Sleep    2s
    Input Text    xpath://input[@id='zipcode']   123
    Scroll Element Into View    xpath://input[@id='mobile_number']
    Input Text    xpath://input[@id='mobile_number']   1234567891
    Click Element    xpath://button[normalize-space()='Create Account']
    Sleep    2s
    Wait Until Element Is Visible    xpath://b[normalize-space()='Account Created!']
    Click Element    xpath://a[@class='btn btn-primary']
    Sleep    2s
    Wait Until Element Is Visible    xpath://li[10]//a[1]
    Sleep    2s
    #close browser
    Close Browser