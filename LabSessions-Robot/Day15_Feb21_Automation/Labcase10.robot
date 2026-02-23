*** Settings ***
Library   SeleniumLibrary
*** Variables ***
${url}       https://automationexercise.com/
*** Test Cases ***
Verify the login scenario with the valid credentials
      Open Browser                 ${url}         chrome
      Maximize Browser Window
      Wait Until Element Is Visible    xpath://a[normalize-space()='Home']
      Sleep    2s
      Scroll Element Into View    xpath://div[@class='footer-bottom']
      Wait Until Element Is Visible     xpath://h2[normalize-space()='Subscription']
      Sleep    2s
      Input Text    xpath://input[@id='susbscribe_email']    prasad12ddaa@gmail.com
      Click Element    xpath://i[@class='fa fa-arrow-circle-o-right']
      Sleep    2s
      Close Browser