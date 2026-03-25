from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains ## why we prefer javascript then action chain for scrolling and other things and for finding elements we will be usibfg waits not find elemet with sleep why

from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get('https://in.pinterest.com/')
driver.maximize_window()
sleep(2)

driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
sleep(3)

## scroll tp origin
driver.execute_script('window.scrollTo(0,0)')
sleep(3)

## using scroll by
driver.execute_script('window.scrollBy(0,500);') ## scrolling down  by 500px
sleep(3)
driver.execute_script('window.scrollBy(0,-200);') ## scrolling up 200px from 500px
sleep(3)

## scrolling to element
ele = driver.find_element(By.XPATH,'//img[contains(@alt,"Photo of a woman in a cherry-patterned")]')
driver.execute_script('arguments[0].scrollIntoView();',ele)
sleep(3)

## clicking
ele1 = driver.find_element(By.XPATH,'(//div[text()="Join Pinterest"])[1]')
driver.execute_script('arguments[0].click();',ele1)
sleep(3)
