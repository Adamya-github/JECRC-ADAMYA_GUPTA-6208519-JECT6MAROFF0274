from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

from time import sleep

# #drag and drop
driver = webdriver.Chrome()
driver.get('https://demoqa.com/droppable')
driver.maximize_window()
sleep(3)
action = ActionChains(driver)
# origin_ele = driver.find_element(By.XPATH,'//div[@id="draggable"]')
# target_ele = driver.find_element(By.XPATH, '(//div[@id="droppable"])[1]')
origin_ele = driver.find_element(By.ID,'draggable')
target_ele = driver.find_element(By.ID, 'droppable')
action.drag_and_drop(origin_ele,target_ele).perform() ## it is mandatory to put perform to have an action
sleep(5)
assert 'Dropped!' == target_ele.text, 'Not Done'
print('Done perfectly')

# ##Drag and Drop using wait NOt working without giving sleep after maximize, is there any way to do it.
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# driver = webdriver.Chrome()
# driver.get('https://demoqa.com/droppable')
# driver.maximize_window()
# sleep(3)
# wait = WebDriverWait(driver, 10)
# origin_ele = wait.until(EC.visibility_of_element_located((By.ID, 'draggable')))
# target_ele = wait.until(EC.visibility_of_element_located((By.ID, 'droppable')))
# actions = ActionChains(driver)
# # actions.drag_and_drop(origin_ele, target_ele).perform()
# assert 'Dropped!' == target_ele.text, 'Not Done'
# print('Done perfectly')


