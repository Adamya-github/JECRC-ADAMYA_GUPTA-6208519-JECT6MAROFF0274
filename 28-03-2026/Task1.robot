*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}  https://testautomationpractice.blogspot.com/

*** Test Cases ***
handling dropdown
    Open Browser    ${url}  chrome
    Maximize Browser Window
    Sleep    2s
##    Scroll Element Into View    xpath=//label[text()="Colors:"]
    Mouse Over    id=colors
    Sleep    2s

    Page Should Contain List    id=colors
    ${options}=  Get List Items    id=colors
    Log To Console    ${options}
    Sleep    2s

    Select From List By Label    id=colors  Blue  Yellow
    Sleep    1s
##    Select From List By Label    id=colors  Yellow
##    Sleep    2s

    @{select_option}=  Get Selected List Labels    id=colors
    Log To Console    ${select_option}
    Sleep    2s

    Close Browser