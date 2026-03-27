## four sections settings, variables, test cases and keywords,
## here using two spaces and tabs, single space will not work

*** Settings ***
## it have import files/resources
Documentation  Opening of browsers
## it is used to give description, when given in setting is is for whole file that is open_browser.robot
Library  SeleniumLibrary


*** Variables ***
## declare all variables that we are going to use, scalar ${}, syntax(list) @{}, dict &{}
## ${url}=  url or ${url}  url
${url}  https://www.cricbuzz.com/
##
@{bikes}  ktm  kwasaki  honda  pulsar  bullet
&{cars}  nissan=gtr  honda=civic  bmw=m5


*** Test Cases ***
## here we write test scripts
Opening Chrome Browser
    [Documentation]  Chrome browser navigating to https://www.cricbuzz.com/
    [Tags]    smoke  dfsf
    ## used for grouping the test cases
    ## single space complete name
    ## double space different group names
    Open Browser  https://www.cricbuzz.com/  chrome
    ## when in chrome given single space it will run it in firefox not in chrome but 
    ## when we use double space it will run on that particular browser
    Maximize Browser Window
    Log  navigated to cricbuzz
    Log To Console  navigated to cricbuzz
    Sleep  3s
    ## also can be 5 minutes 30s
#    Close Window
#    Close Browser
#    Close All Browser

Opening Edge Browser
    [Documentation]  Edge browser navigating to https://www.cricbuzz.com/
    [Tags]    smoke
    Open Browser  https://www.cricbuzz.com/  edge
    Maximize Browser Window
    Log  navigated to cricbuzz
    Log To Console  navigated to cricbuzz
    Sleep  3s

Opening Firefox Browser
    [Documentation]  Firefox browser navigating to https://www.cricbuzz.com/
    Open Browser  ${url}  firefox
    Maximize Browser Window
    Log  navigated to cricbuzz
    Log To Console    ${bikes}[3] & ${bikes}[2],${bikes}[1] ${bikes}[0]${cars.honda}
    Sleep  3s
    Close All Browsers

Opening Chrome headless Browser
    Opening headless Browser    


*** Keywords ***
## user defined keywords are written in this section
Opening headless Browser
    [Documentation]  Chrome headless browser navigating to https://www.cricbuzz.com/
    Open Browser  ${url}  headlesschrome
    ## headless work only on chrome and firefox
    Maximize Browser Window

    Log  navigated to cricbuzz
    Log To Console  ${cars.bmw}
    Sleep  3s

    Close Browser



## python -m robot -d reports open_browser.robot
## python -m robot -d reports -t "Opening Chrome headless Browser" open_browser.robot
## python -m robot -d reports -i "smoke" open_browser.robot
## python -m robot -d reports -e "smoke" open_browser.robot