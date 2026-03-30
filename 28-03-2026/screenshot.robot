*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}  https://in.bookmyshow.com/explore/home/jaipur

*** Test Cases ***
Screenshots
    Open Browser    ${url}  chrome
    Maximize Browser Window
    Sleep    5s
    Set Screenshot Directory    Screenshots  ## This also putting in current directory
#    Set Screenshot Directory    ${CURDIR}/Screenshots1  ## this for putting in current directory
#    Set Screenshot Directory    ${CURDIR}/../Screenshot2  ## this for putting the previous directory of current directory
    Capture Page Screenshot    file1.jpg
    Sleep    2s
    Capture Element Screenshot    xpath=//img[@alt="Dhurandhar The Revenge"]  file2.jpg
    Sleep    3s
    Close Browser
