*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}  https://testautomationpractice.blogspot.com/

*** Test Cases ***
simple
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    2s
    Click Button    xpath=//button[@onclick="myFunctionAlert()"]
    Handle Alert
    ${text}  Get Text    xpath=//p[@id="demo"]
    Log To Console    ${text}
    Close Browser

Confirmation
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    2s
    Click Button    xpath=//button[@onclick="myFunctionConfirm()"]
    Handle Alert
    Page Should Contain    OK!
    ${text}  Get Text    xpath=//p[@id="demo"]
    Log To Console    ${text}
    Close Browser

prompt
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    2s
    Click Button    xpath=//button[@onclick="myFunctionPrompt()"]
    Input Text Into Alert    AbAb
    Page Should Contain    AbAb
    ${text}  Get Text    xpath=//p[@id="demo"]
    Log To Console  ${text}   
    Close Browser