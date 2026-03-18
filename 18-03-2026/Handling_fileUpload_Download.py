from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

### To upload a file
driver = webdriver.Chrome()
driver.get('https://the-internet.herokuapp.com/upload')
driver.maximize_window()
choose_file = driver.find_element(By.ID, 'file-upload')
sleep(5)
choose_file.send_keys("C:/Users/Adamya Gupta/OneDrive/Desktop/Testing_Tech/JECRC/18-03-2026/Assert.py")
submit_button = driver.find_element(By.ID,'file-submit')
sleep(5)
submit_button.click()
sleep(5)
print('uploaded')
# driver.quit()

### To download a file
# driver = webdriver.Chrome()
driver.get('https://the-internet.herokuapp.com/download')
# driver.maximize_window()
sleep(5)
driver.find_element(By.XPATH,'//a[text()="Screenshot 2025-12-24 164603.png"]').click()
sleep(5)
print('Downloaded')

driver.quit()