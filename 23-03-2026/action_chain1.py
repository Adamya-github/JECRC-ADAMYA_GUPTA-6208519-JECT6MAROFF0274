from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get('https://supertails.com')
driver.maximize_window()
sleep(3)
action = ActionChains(driver)
catto = driver.find_element(By.XPATH,'//div[@data-ganame="Breed 5"]')
action.scroll_to_element(catto).perform()
sleep(5)

## also see what is scroll to: (100,100), scroll by: (100,100), difference between them
action.scroll_by_amount(0,-1500).perform()
sleep(5)

# action.scroll_from_origin(0,0,1000).perform() # see to it why it is not working
#  File "C:\Users\Adamya Gupta\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\selenium\webdriver\common\action_chains.py", line 362, in scroll_from_origin
#     raise TypeError(f"Expected object of type ScrollOrigin, got: {type(scroll_origin)}")
# TypeError: Expected object of type ScrollOrigin, got: <class 'set'

# action.context_click() # right click
# action.double_click() # double click
# action.click() # left click