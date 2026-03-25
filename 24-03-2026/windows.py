from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://the-internet.herokuapp.com/windows')
driver.maximize_window()
sleep(3)

parent_window = driver.current_window_handle ## if i don't want to use index 0 to return to main window we can use it
print(driver.current_window_handle)
driver.find_element(By.XPATH,'//a[text()="Click Here"]').click()
sleep(2)

all_windows = driver.window_handles ## it returns the list of windows that are open after clicking
print(len(all_windows))
driver.switch_to.window(all_windows[-1])
print(driver.current_window_handle)
assert 'New' in driver.find_element(By.CLASS_NAME,'example').text, print('Not Done')
print('Done')

driver.close() ## it will close the current tab but not transfer the control so we need to do it by switching

driver.switch_to.window(parent_window)
sleep(3)
