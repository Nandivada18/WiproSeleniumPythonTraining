*** Settings ***
#setting we add the external library details
Library    SeleniumLibrary

#1.Create a scalar variable ${NAME} and print it.
*** Variables ***
${NAME}    Prasad

*** Test Cases ***
Print Name
    Log    ${NAME}

#2.Assign two numbers to variables and print their sum.
*** Test Cases ***
Add Two Numbers
    ${num1}=    Set Variable    10
    ${num2}=    Set Variable    20
    ${sum}=     Evaluate    ${num1} + ${num2}
    Log To Console    Sum is: ${sum}

#3.Create a variable ${CITY} and use it inside a sentence.
*** Variables ***
${CITY}    Hyderabad

*** Test Cases ***
Use City In Sentence
    Log To Console    I live in ${CITY}.

#4.Reassign a variable value inside a test case and log the updated value.
*** Variables ***
${CITY}    Hyderabad

*** Test Cases ***
Reassign City Value
    Log To Console    Original city: ${CITY}
    ${CITY}=    Set Variable    Bengaluru
    Log To Console    Updated city: ${CITY}

#5.Create a list variable @{FRUITS} and print the first item.
*** Variables ***
@{FRUITS}    Apple    Banana    Mango

*** Test Cases ***
Print First Fruit
    Log To Console    First fruit: ${FRUITS}[0]

#6.Loop through a list variable and print each element.
*** Variables ***
@{FRUITS}    Apple    Banana    Mango    Orange

*** Test Cases ***
Print All Fruits
    FOR    ${fruit}    IN    @{FRUITS}
        Log To Console    Fruit: ${fruit}
    END

#7.Find the length of a list variable.
*** Variables ***
@{FRUITS}    Apple    Banana    Mango    Orange

*** Test Cases ***
Get List Length
    ${length}=    Get Length    ${FRUITS}
    Log To Console    The list has ${length} items.

#8.Create a dictionary variable &{USER} and print one key value.
*** Variables ***
&{USER}    name=Prasad    age=25    city=Hyderabad

*** Test Cases ***
Print User Name
    Log To Console    User name is: ${USER['name']}

#9.Add a new key-value pair to a dictionary variable.
*** Settings ***
Library    Collections

*** Variables ***
&{USER}    name=Prasad    age=25    city=Hyderabad

*** Test Cases ***
Add Key To Dictionary
    Log To Console    Original dictionary: ${USER}
    Set To Dictionary    &{USER}    country=India

    Log To Console    Updated dictionary: ${USER}
    Log To Console    Country: ${USER['country']}

#10.Access dictionary values inside a loop and print key and value.
*** Settings ***
Library    Collections

*** Variables ***
&{USER}    name=Prasad    age=25    city=Hyderabad

*** Test Cases ***
Loop Through Dictionary
    FOR    ${key}    IN    &{USER}
        ${value}=    Get From Dictionary    &{USER}    ${key}
        Log To Console    ${key} : ${value}
    END






