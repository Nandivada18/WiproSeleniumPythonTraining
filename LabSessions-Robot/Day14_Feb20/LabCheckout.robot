*** Settings ***
Library    SeleniumLibrary
Library    OperatingSystem
Library    Collections

*** Variables ***
${url}    https://practice.automationtesting.in/

*** Test Cases ***
Verify scroll
    Open Browser    ${url}    chrome
    #maximize the browser window
    Maximize Browser Window
    #wait till the element is loaded
    Set Selenium Implicit Wait    3s
    Scroll Element Into View    xpath://div[@id='text-22-sub_row_1-0-2-1-0']
    Sleep    3s
    Click Element    xpath://div[@class='grippy-host']
    Sleep    2s
    Click Element    xpath://a[@data-product_id='163']
    Sleep    2s
    Scroll Element Into View    xpath://span[@class='cartcontents']
    Click Element    xpath://span[@class='cartcontents']
    Sleep    2s
    Click Element    xpath://a[@class='checkout-button button alt wc-forward']
    Sleep    2s
    Wait Until Element Is Visible    xpath://input[@id='billing_first_name']
    Input Text    xpath://input[@id='billing_first_name']    prasad
    Input Text    xpath://input[@id='billing_last_name']     N
    Scroll Element Into View    xpath://input[@id='billing_email']
    Input Text    xpath://input[@id='billing_email']    prasad@gmail.com
    Input Text    xpath://input[@id='billing_phone']    1234567891
    Scroll Element Into View    xpath://input[@id='billing_address_1']
    Input Text    xpath://input[@id='billing_address_1']   A-B
    Scroll Element Into View    xpath://input[@id='billing_city']
    Input Text    xpath://input[@id='billing_city']    RJY
    Input Text    xpath://input[@id='billing_postcode']    33333
    Scroll Element Into View    xpath://div[@id='content']
    Click Element    xpath://input[@id='place_order']
    Sleep    2s
    #close browser
    Close Browser