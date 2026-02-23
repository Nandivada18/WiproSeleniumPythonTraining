*** Settings ***
Library   SeleniumLibrary
*** Variables ***
${url}       https://automationexercise.com/
*** Test Cases ***
Verify the login scenario with the valid credentials
      Open Browser                 ${url}         chrome
      Maximize Browser Window
      Wait Until Element Is Visible    xpath://a[contains(text(),'Test Cases')]
      Click Element    xpath://a[contains(text(),'Test Cases')]
      Wait Until Element Is Visible    xpath://b[normalize-space()='Test Cases']
      Close Browser
