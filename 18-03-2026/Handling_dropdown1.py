from selenium import webdriver
from selenium.webdriver.common.by import By ## from common we always call by, keys and action_chains
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from time import sleep



opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)

driver.get('https://www.lenskart.com/')
driver.maximize_window()
sleep(2)
search = driver.find_element(By.XPATH,'//input[@class="aa-Input"]')
search.send_keys('sunglasses', Keys.ENTER)
sleep(2)

sorting = driver.find_element(By.ID,'sortByDropdown')
dropdown = Select(sorting)
dropdown.select_by_value('saving')
t1 = driver.find_elements(By.XPATH,'//div[@class="sc-23b7d3eb-6 hYdmOJ"]/div/following-sibling::p')
print(t1[0].text)
sleep(5)
driver.quit()
