*** Settings ***
Library    SeleniumLibrary
Library    OperatingSystem
Library    Collections

*** Variables ***
${url}    https://www.amazon.in/

*** Test Cases ***
Verify links
    Open Browser    ${url}    chrome
    #maximize the browser window
    Maximize Browser Window
    #wait till the element is loaded
    Set Selenium Implicit Wait    2s
    #for links
    @{links}=         Get WebElements    xpath://a
    FOR    ${link}    IN    @{links}
        ${text}=      Get Text    ${link}
        ${url}=   Get Element Attribute    ${link}    href
        Log To Console    ${text}
        Log To Console    ${url}
    END
    #close browser
    Close Browser