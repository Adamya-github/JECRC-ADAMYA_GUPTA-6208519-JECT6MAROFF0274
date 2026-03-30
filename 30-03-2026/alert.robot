*** Settings ***
Library  SeleniumLibrary
*** Variables ***
${url}  https://the-internet.herokuapp.com/javascript_alerts

*** Test Cases ***
Handling alerts(simple)
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    2s

    Click Button    xpath=//button[@onclick="jsAlert()"]
    Handle Alert

    Sleep    5s
    Close Browser

Confirmation
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    2s

    Click Button    xpath=//button[@onclick="jsConfirm()"]

    Handle Alert  action=DISMISS      #for cancelling

    Sleep    5s
    Close Browser

prompt
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    2s

    Click Button    xpath=//button[@onclick="jsPrompt()"] 

#    Input Text Into Alert    AbAB    action=DISMISS
    Input Text Into Alert    AbAb    
    Sleep    2s
    Close Browser