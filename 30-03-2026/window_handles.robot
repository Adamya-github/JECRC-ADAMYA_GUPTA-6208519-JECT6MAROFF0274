*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}  https://the-internet.herokuapp.com/windows

*** Test Cases ***
Window Handling
    Open Browser    ${url}  chrome
    Maximize Browser Window
    Sleep    2s
    Click Element    xpath=//a[@href="/windows/new"]
    Sleep    2s
    
    @{windows}  Get Window Handles 
    @{titles}  Get Window Titles       
    Log To Console    ${windows} ${titles}
    
    Switch Window    NEW
    Sleep    2s
    Page Should Contain    New Window
#    Page Should Contain Element    xpath=//h3[text()="New Window"]  ## both ways
    Sleep    2s

    Switch Window    ${windows}[0]
    Sleep    2s

    Close Browser

    