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
      Wait Until Element Is Visible    xpath://a[@href='/products']
      Click Element    xpath://a[@href='/products']
      Wait Until Element Is Visible    xpath://h2[normalize-space()='All Products']
      Sleep    2s
      Click Element    xpath://input[@id='search_product']
      Input Text    xpath://input[@id='search_product']    Blue Top
      Click Element    xpath://button[@id='submit_search']
      Wait Until Element Is Visible    xpath://h2[normalize-space()='Searched Products']
      Close Browser