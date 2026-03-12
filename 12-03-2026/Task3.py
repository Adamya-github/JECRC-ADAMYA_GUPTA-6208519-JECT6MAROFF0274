## same for loop current url and title
from selenium import webdriver
from time import sleep

l1 = [webdriver.Chrome, webdriver.Edge, webdriver.Firefox]
for i in l1:
    driver = i()
    driver.get("https://github.com/Adamya-github/JECRC-ADAMYA_GUPTA-6208519-JECT6MAROFF0274")
    print(f'Adamya-github/JECRC-ADAMYA_GUPTA-6208519-JECT6MAROFF0274: {driver.current_url}')
    print(driver.name)
    sleep(2)