*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}  https://testautomationpractice.blogspot.com/

*** Test Cases ***
Window Handling
    Open Browser    ${url}  chrome
    Maximize Browser Window
    Sleep    2s
    Mouse Over    xpath=//button[@id="PopUp"]
    Sleep    2s

#    Click Button    xpath=//button[@id="PopUp"]
    Click Element    xpath=//button[@id="PopUp"]
    Sleep    2s

    @{windows}  Get Window Handles
    
    Switch Window    NEW
    Sleep    2s
    Page Should Contain Element    xpath=//h4[@class="alert-heading text-center m-2"]
    
    @{title}  Get Window Titles    
    Log To Console    ${title}[2]
    Sleep    2s
    
    Switch Window    ${windows}[0]
    Log To Console    ${title}[0]
    Page Should Contain     Automation Testing Practice
    Sleep    2s

    Close Browser

