*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}    https://www.amazon.in/

*** Test Cases ***
Amazon Electronics boAt Product Flow
    Open Browser    ${URL}    chrome
    Maximize Browser Window
    Sleep    3s
    Click Element    xpath=//a[text()=" Electronics "]
    Sleep    3s

    Execute JavaScript    window.scrollBy(0,500)
    Sleep    2s
    Click Element    xpath=(//span[text()='boAt'])[2]
    Sleep    3s
    Execute JavaScript    window.scrollBy(0,700)
    Sleep    2s


    ${product_name}=    Get Text    (//div[@data-cy="title-recipe"])[5]/descendant::span
    Log To Console    Selected Product: ${product_name}

    Click Element    xpath=(//div[@data-cy="title-recipe"])[5]/descendant::span
    Sleep    3s

    Switch Window    NEW
    Sleep    3s

    ${page_title}=    Get Text    id=productTitle
    Page Should Contain    ${page_title}

    ${actual_price}=  Get Text  xpath=(//span[@class="a-price a-text-price apex-basisprice-value"]/span)[2]
    ${discounted_price}=  Get Text  xpath=//span[@class="apex-savings-container"]/following-sibling::span/span[2]/span[2]
    ${discount_percent}=  Get Text  xpath=//span[@class="apex-savings-container"]/span

    Log To Console    Actual Price: ${actual_price}
    Log To Console    Discounted Price: ${discounted_price}
    Log To Console    Discount %: ${discount_percent}

    Scroll Element Into View    id=add-to-cart-button
    Click Button    id=add-to-cart-button
    Sleep    3s

    Click Element    id=nav-cart
    Sleep    3s

    Page Should Contain    ${page_title}

    Close Browser