*** Settings ***
Library    SeleniumLibrary
Library    OperatingSystem

*** Variables ***
${url}  https://the-internet.herokuapp.com/
${path1}  C:\\Users\\Adamya Gupta\\Downloads\\file.txt

*** Test Cases ***
File Upload
    Open Browser    ${url}  chrome
    Maximize Browser Window   
    Click Element    xpath=//a[@href="/upload"]
    Sleep    2s   
##    ${path}  Normalize Path    ${CURDIR}/sample.txt
    ${path}  Normalize Path    C:\\Users\\Adamya Gupta\\OneDrive\\Desktop\\Testing_Tech\\JECRC\\30-03-2026\\sample.txt   
    Choose File    id=file-upload    ${path}
    Sleep    3s
    Click Button    id=file-submit
    Sleep    3s
    Close Browser

File Download
    Open Browser    ${url}  chrome
    Maximize Browser Window
    Click Element    xpath=//a[@href="/download"]
    Sleep    2s
    Click Element    xpath=//a[@href="download/file.txt"]
    Wait Until Created    ${path1}  timeout=10s
    File Should Exist    ${path1}
    Log To Console    it downloaded successfully
    Close Browser