*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}       https://automationexercise.com/
*** Test Cases ***
Verify the login scenario with the valid credentials
      Open Browser                 ${url}         chrome
      Maximize Browser Window
      Wait Until Element Is Visible    xpath://a[normalize-space()='Contact us']
      Click Element    xpath://a[normalize-space()='Contact us']
      Wait Until Element Is Visible    xpath://h2[normalize-space()='Get In Touch']
      Scroll Element Into View    xpath://h2[normalize-space()='Get In Touch']
      Click Element    xpath://input[@placeholder='Name']
      Input Text    xpath://input[@placeholder='Name']    prasad
      Sleep    2s
      Input Text    xpath://input[@placeholder='Email']   prasad12ddaa@gmail.com
      Click Element    xpath://input[@placeholder='Subject']
      Input Text    xpath://input[@placeholder='Subject']   Inquiry about products
      Click Element    xpath://textarea[@id='message']
      Input Text    xpath://textarea[@id='message']   Hello, I would like to know more about your products and their availability. Please provide the details.
      Wait Until Element Is Visible    xpath://input[@name='upload_file']
      Choose File    xpath://input[@name='upload_file']    C://Users//prasa//Downloads//rs.jpg
      Click Element    xpath://input[@name='submit']
      Handle Alert     action=ACCEPT       timeout=3
      Sleep    5s
      Wait Until Element Is Visible    xpath://div[@class='status alert alert-success']
      Close Browser