*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}  https://demo.automationtesting.in/Frames.html

*** Test Cases ***
Handling Iframes
    Open Browser    ${url}  chrome
    Maximize Browser Window
    Sleep    2s
    Mouse Over    xpath=//span[text()="Discover more"]
    Sleep    2s

    Click Element    xpath=//a[text()="Iframe with in an Iframe"]
    Sleep    2s

    Select Frame    //iframe[@src="MultipleFrames.html"]
#    Page Should Contain    Nested iFrames
    Sleep  2s

    Select Frame    //iframe[@src="SingleFrame.html"]
#    Page Should Contain    iFrame Demo
    Sleep    2s

    Input Text   xpath=//input[@type="text"]  ABCD
    Sleep    2s

    Unselect Frame
    Sleep    2s
    Page Should Contain    Nested iFrames

    Unselect Frame
    Sleep  2s
    Page Should Contain    Automation Demo Site

    Sleep    2s
    Close Browser

#*** Settings ***
#Library    SeleniumLibrary
#
#*** Variables ***
#${url}    https://demo.automationtesting.in/Frames.html
#
#*** Test Cases ***
#Handling Iframes Properly
#    Open Browser    ${url}    chrome
#    Maximize Browser Window
#
#    # Open nested iframe section
#    Click Element    xpath=//a[text()="Iframe with in an Iframe"]
#
#    # Wait for outer frame and switch
##    Wait Until Element Is Visible    xpath=//iframe[@src="MultipleFrames.html"]    10s
#    Select Frame    xpath=//iframe[@src="MultipleFrames.html"]
#
#    # Wait for inner frame and switch
##    Wait Until Element Is Visible    xpath=//iframe[@src="SingleFrame.html"]    10s
#    Select Frame    xpath=//iframe[@src="SingleFrame.html"]
#
#    # Wait for input box and interact
##    Wait Until Element Is Visible    xpath=//input[@type="text"]    10s
#    Input Text    xpath=//input[@type="text"]    ABCD
#    Sleep    2
#    # Exit frames step-by-step
#    Unselect Frame
#    Unselect Frame
#
#    Close Browser