*** Settings ***
Library   SeleniumLibrary
*** Variables ***
${url}       https://automationexercise.com/
*** Test Cases ***
Verify the login scenario with the valid credentials
      Open Browser                 ${url}         chrome
      Maximize Browser Window
      Wait Until Element Is Visible    xpath://a[@href='/products']
      Scroll Element Into View    xpath://a[@href='/products']
      Click Element    xpath://a[@href='/products']
      Wait Until Element Is Visible    xpath://h2[normalize-space()='All Products']
      Scroll Element Into View    xpath://a[@href='/brand_products/Biba']
      Click Element    xpath://div[@class='col-sm-9 padding-right']//div[2]//div[1]//div[1]//div[2]//div[1]//a[1]
      Sleep    2s
      Click Element    xpath://button[@class='btn btn-success close-modal btn-block']
      Wait Until Element Is Visible    xpath://div[@class='view-product']//img[@alt='ecommerce website products']
      Page Should Contain Element    xpath://p[normalize-space()='Category: Women > Tops']
      Page Should Contain Element    xpath://label[normalize-space()='Quantity:']
      Page Should Contain Element    xpath://div[@class='product-details']//p[1]
      Page Should Contain Element    xpath://div[@class='product-details']//p[1]
      Page Should Contain Element    xpath://div[@class='product-details']//p[1]
      Close Browser