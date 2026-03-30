*** Settings ***
Documentation    handling dropdowns
Library    SeleniumLibrary

*** Variables ***
${url}  https://the-internet.herokuapp.com/
${browser}  chrome
*** Test Cases ***
handle dropdown
    Open Browser    ${url}  ${browser}
    Maximize Browser Window
    
    Sleep    2s
    
    Click Element    xpath=//a[text()="Dropdown"]
    
    Sleep    2s
    
##    Page Should Contain Element    id=dropdown ## user either one of it, list one is more prefer because list means dropdown
    Page Should Contain List    id=dropdown

    ${options}=  Get List Items    id=dropdown
    Log To Console    ${options}
    
    Select From List By Label  id=dropdown  Option 1
    
    Sleep    2s
    
    ${select_option}=  Get Selected List Label    id=dropdown
    Log To Console    ${select_option}

    List Selection Should Be    id=dropdown  Option 1
##    List Selection Should Be    id=dropdown  Option 2 ## List 'id=dropdown' should have had selection [ Option 2 ] but selection was [ Option 1 (1) ].
    Sleep    3s

    Close Browser


##  python -m robot -d reports -v browser:"edge" dropdown.robot

# $ = 1, @ = [1,2,3], & = {1:'a',2:'b'}, @--> ['Blue', 'White'], $ --> [['Blue','White']]


