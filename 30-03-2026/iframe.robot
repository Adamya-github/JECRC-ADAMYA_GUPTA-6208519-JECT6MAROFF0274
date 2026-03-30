*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}  https://demo.automationtesting.in/Frames.html

*** Test Cases ***
Handling Iframes
    Open Browser    ${url}  chrome
    Maximize Browser Window
    Sleep    2s
    Mouse Over    id=singleframe
    Sleep    2s
    
    Select Frame    id=singleframe

    Input Text    xpath=//input[@type="text"]  ABCD
    Sleep    2s

    Unselect Frame
    Sleep    2s

    Close Browser