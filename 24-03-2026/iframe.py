from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://demo.automationtesting.in/Frames.html')
driver.maximize_window()
sleep(3)
action = ActionChains(driver)

## single iframe
## driver.find_element(By.XPATH,'//input[@type="text"]').send_keys('123') ## It will not work because it is in iframe and rightnow control is in html not iframe html, so first changr control
iframe = driver.find_element(By.ID,'singleframe')
driver.switch_to.frame(iframe) ## frame to switch to iframe and window for switching to window
sleep(2)
driver.find_element(By.XPATH,'//input[@type="text"]').send_keys('123')
sleep(5)

##
driver.switch_to.default_content() ## To go back to the main HTML (default content), there is parent to which go one step above
##

## iframe within iframe
driver.find_element(By.XPATH,'//a[text()="Iframe with in an Iframe"]').click()
sleep(2)

outer_iframe=driver.find_element(By.XPATH,'//iframe[@src="MultipleFrames.html"]')
driver.switch_to.frame(outer_iframe)
sleep(2)
inner_iframe=driver.find_element(By.XPATH,'//iframe[@src="SingleFrame.html"]')
driver.switch_to.frame(inner_iframe)
sleep(2)
driver.find_element(By.XPATH,'//input[@type="text"]').send_keys('123')
sleep(2)

driver.switch_to.parent_frame()
# driver.switch_to.default_content() ## it will not work here as we need access iframe
driver.find_element(By.XPATH,'//div[@class="iframe-container"]').click() ## this will work when I go to above parent of inner iframe

action.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
sleep(1)
action.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()
sleep(2)

driver.switch_to.default_content()
sleep(2)
