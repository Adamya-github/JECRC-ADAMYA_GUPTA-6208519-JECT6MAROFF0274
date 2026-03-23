from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('https://www.myntra.com')
driver.maximize_window()
sleep(3)
wait = WebDriverWait(driver,10)
action = ActionChains(driver)

men = wait.until(EC.presence_of_element_located((By.XPATH,'(//div[@class="desktop-navLink"]/a)[1]')))
action.move_to_element(men).perform()

wait.until(EC.presence_of_element_located((By.XPATH,'//a[text()="Perfumes & Body Mists"]'))).click()

five = wait.until(EC.presence_of_element_located((By.XPATH,'(//div[@class="product-imageSliderContainer"])[12]')))
action.scroll_to_element(five).perform()
sleep(3)


