*** Settings ***
#setting we add the external library details
Library    SeleniumLibrary

*** Variables ***
${name}    John
${city}    Hyderabad
${address}    St Peters Road
@{list1}    green    red    grapes
@{list2}    apple    banana    grapes
&{creds}    username=admin    password=admin123


*** Test Cases ***
Verify the Variables
    Log    ${name}
    Log    ${city}
    Log    ${address}
    FOR    ${element}    IN    @{list1}
        Log    ${element}
    END
    FOR    ${element}    IN    @{list2}
        Log    ${element}
    END
    Log    ${list1}[0]
    Log    ${list1}[1]
    Log    ${creds}[username]
    Log    ${creds}[password]