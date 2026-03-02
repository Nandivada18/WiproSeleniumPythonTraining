*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}        https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login
${BROWSER}    Chrome
${FIRST}      Prasad
${LAST}       N
${POST}       12345
${CUSTOMER}   Prasad N
${DEPOSIT}    500
${WITHDRAW}   200

*** Test Cases ***
Complete Banking Flow
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Wait Until Element Is Visible    xpath=//button[text()='Bank Manager Login']

    #Manager
    Click Button    xpath=//button[text()='Bank Manager Login']
    Sleep    2s

    # Add Customer
    Click Button    xpath=//button[normalize-space()='Add Customer']
    Sleep    2s
    Input Text      xpath=//input[@placeholder='First Name']    ${FIRST}
    Sleep    2s
    Input Text      xpath=//input[@placeholder='Last Name']     ${LAST}
    Sleep    2s
    Input Text      xpath=//input[@placeholder='Post Code']     ${POST}
    Sleep    2s
    Click Button    xpath=//button[@type='submit']
    Sleep    2s
    Handle Alert    ACCEPT
    Sleep    2s

    # Open Account
    Click Button    xpath=//button[normalize-space()='Open Account']
    Sleep    2s
    Select From List By Label    id=userSelect    ${CUSTOMER}
    Sleep    2s
    Select From List By Label    id=currency    Rupee
    Sleep    2s
    Click Button    xpath=//button[text()='Process']
    Sleep    2s
    Handle Alert    ACCEPT
    Sleep    2s

    # Back to Home
    Click Button    xpath=//button[text()='Home']
    Sleep    2s

    # Customer Login
    Click Button    xpath=//button[text()='Customer Login']
    Sleep    2s
    Select From List By Label    id=userSelect    ${CUSTOMER}
    Sleep    2s
    Click Button    xpath=//button[text()='Login']
    Sleep    2s

    # Deposit
    Click Button    xpath=//button[normalize-space()='Deposit']
    Sleep    2s
    Input Text      xpath=//input[@ng-model='amount']    ${DEPOSIT}
    Sleep    2s
    Click Button    xpath=//button[@type='submit']
    Sleep    2s
    Element Should Contain    xpath=//span[@class='error ng-binding']    Deposit Successful
    Sleep    2s

    # Withdraw
    Click Button    xpath=//button[normalize-space()='Withdrawl']
    Sleep    2s
    Input Text      xpath=//input[@ng-model='amount']    ${WITHDRAW}
    Sleep    2s
    Click Button    xpath=//button[@type='submit']
    Sleep    2s
    Element Should Contain    xpath=//span[@class='error ng-binding']    Transaction successful
    Sleep    2s

    # Validate Balance
    ${balance}=    Get Text    xpath=//div[@ng-hide='noAccount']/strong[2]
    Sleep    2s
    ${expected}=   Evaluate    ${DEPOSIT} - ${WITHDRAW}
    Sleep    2s
    Should Be Equal As Integers    ${balance}    ${expected}
    Sleep    2s

    Close Browser