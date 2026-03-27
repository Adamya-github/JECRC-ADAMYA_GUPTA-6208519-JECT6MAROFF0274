*** Settings ***
Documentation    handling checkboxes
Library    SeleniumLibrary

*** Variables ***
${url}  https://the-internet.herokuapp.com/
${url1}  https://testautomationpractice.blogspot.com/
@{days}  sunday  monday  tuesday  wednesday  thursday  friday  saturday

*** Test Cases ***
Handling Checkboxes
    How to Handle Checkboxes
Handling Radio + Checkboxes
    How to Handle Radio and Multiple Checkboxes
Handling Radio + Checkboxes For
    How to Handle Radio and Multiple Checkboxes via For

*** Keywords ***
How to Handle Checkboxes
    [Documentation]    herokuapp checkboxes
    Open Browser    ${url}  headlesschrome
    Maximize Browser Window
    Sleep    3s
    Click Element    xpath=//a[text()="Checkboxes"]
    ## shift +f6 to rename all same names, hold ctrl to click on the functions
    Page Should Contain Checkbox    xpath=(//input[@type="checkbox"])[1]
    Sleep    3s
    Select Checkbox    xpath=(//input[@type="checkbox"])[1]
    Sleep    3s
    Unselect Checkbox    xpath=(//input[@type="checkbox"])[2]
    Sleep    3s
    Close Browser

How to Handle Radio and Multiple Checkboxes
    [Documentation]    Testautomation radio and checkboxes
    Open Browser    ${url1}  edge
    Maximize Browser Window
    Sleep    3s
    Click Element    xpath=//input[@id="male"]
    Sleep    2s
    Page Should Contain Checkbox    xpath=//input[@id="sunday"]
    Sleep    3s
    Select Checkbox    xpath=//input[@id="sunday"]
    Sleep    3s
    Select Checkbox    xpath=//input[@id="monday"]
    Sleep    3s
    Unselect Checkbox    xpath=//input[@id="sunday"]
    Sleep    3s
    Unselect Checkbox    xpath=//input[@id="monday"]
    Sleep    3s
    Close Browser

How to Handle Radio and Multiple Checkboxes via For
    [Documentation]    Testautomation radio and checkboxes
    Open Browser    ${url1}  edge
    Maximize Browser Window
    Sleep    3s
    Click Element    xpath=//input[@id="male"]
    Sleep    2s
    Page Should Contain Checkbox    xpath=//input[@id="sunday"]
    Sleep    2s
    FOR  ${day}  IN  @{days}
         Select Checkbox    xpath=//input[@id="${day}"]
         Sleep    2s
    END
    FOR  ${day}  IN  @{days[::-1]}
         Unselect Checkbox    xpath=//input[@id="${day}"]
         Sleep    2s
    END
    Close Browser

   

