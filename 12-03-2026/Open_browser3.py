from selenium import webdriver
from time import sleep

opt = webdriver.ChromeOptions()
opt.add_experimental_option('detach', True)
driver = webdriver.Chrome()
driver.get("https://github.com/Adamya-github/JECRC-ADAMYA_GUPTA-6208519-JECT6MAROFF0274")
print(f'Adamya-github/JECRC-ADAMYA_GUPTA-6208519-JECT6MAROFF0274: {driver.current_url}')
print(driver.name)
sleep(5)


## write a for loop for numerous browser , just open it
## same for loop current url and title