from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.rajasthanroyals.com/")
driver.maximize_window()
sleep(2)
action = ActionChains(driver)
wait = WebDriverWait(driver,10)
# rr = driver.find_element(By.XPATH,'(//div[@class="article-wrap"])[23]')
rr = wait.until(EC.presence_of_element_located((By.XPATH,'(//div[@class="article-wrap"])[23]')))

for i in range(5):
    action.scroll_to_element(rr).perform()
    sleep(3)
    action.send_keys(Keys.PAGE_UP).perform()
    sleep(3)
