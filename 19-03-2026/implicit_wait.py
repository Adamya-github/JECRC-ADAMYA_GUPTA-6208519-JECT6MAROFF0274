from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


opts= webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)

driver.get('https://abc.com/')
driver.maximize_window()
driver.implicitly_wait(1)

ele = driver.find_element(By.XPATH, '(//a[@class="AnchorLink"]/parent::li/descendant::img)[1]')
print(ele.get_attribute('src'))

sleep(2)
driver.quit()

## Implicit wait
# An implicit wait in Selenium is a global setting that
# tells the WebDriver to wait for a certain amount of
# time before throwing a NoSuchElementException if an
# element is not found right away. Once you set it,
# it applies to all `findElement` and `findElements`
# calls throughout the entire session. The driver keeps
# checking the DOM repeatedly until the element appears
# or the time runs out, and if the element is found earlier,
# it continues immediately, making it better than a fixed delay
# like `sleep`. By default, the wait time is zero, so errors
# are thrown instantly. Implicit wait only checks if an element
# exists in the DOM, not whether it is visible or clickable.
# It is useful for simple and stable pages, but for dynamic
# websites where elements load at different times, explicit
# waits are usually better because they allow waiting for
# specific conditions. Also, it’s best not to use implicit
# and explicit waits together, as this can cause unpredictable delays.
