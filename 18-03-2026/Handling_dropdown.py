from selenium import webdriver
from selenium.webdriver.common.by import By ## from common we always call by, keys and action_chains
from selenium.webdriver.support.select import Select
from time import sleep

from sqlalchemy.testing.plugin.plugin_base import options

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)

driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()

country_dropdown = driver.find_element(By.ID,'country')
dropdown = Select(country_dropdown)

dropdown.select_by_value('india')
sleep(5)
dropdown.select_by_index(4) ## here index is staring from 0 to n , but in xpath it is 1 to n
sleep(5)
dropdown.select_by_visible_text("Japan")
sleep(5)

driver.quit()

## if dropdown is in select--> what to do
## if dropdown is in div or somthing else --> what to do