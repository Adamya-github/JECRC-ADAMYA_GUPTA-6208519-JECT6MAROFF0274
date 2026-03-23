from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep

# ##drag and drop
# driver = webdriver.Chrome()
# driver.get('https://the-internet.herokuapp.com/drag_and_drop')
# driver.maximize_window()
# sleep(3)
# action = ActionChains(driver)
# origin_ele = driver.find_element(By.ID,'column-a')
# target_ele = driver.find_element(By.ID, 'column-b')
# action.drag_and_drop(origin_ele,target_ele).perform() ## it is mandatory to put perform to have an action
# sleep(5)

## Mouse Hover
driver = webdriver.Chrome()
driver.get('https://supertails.com')
driver.maximize_window()
sleep(3)
action = ActionChains(driver)
doggo = driver.find_element(By.XPATH,'(//span[contains(text(),"Dogs")])[1]')
action.move_to_element(doggo).perform()
sleep(3)

