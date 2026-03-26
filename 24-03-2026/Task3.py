from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get("https://demoqa.com/browser-windows")
driver.maximize_window()
sleep(3)
main_window = driver.current_window_handle

# 1. New Tab
driver.find_element(By.ID, "tabButton").click()
all_windows = driver.window_handles
driver.switch_to.window(all_windows[-1])
text1 = driver.find_element(By.ID, "sampleHeading").text
sleep(2)
assert "This is a sample page" in text1, 'Different'
print('Same')
driver.close()

driver.switch_to.window(main_window)
sleep(3)

# 2. New Window
driver.find_element(By.ID, "windowButton").click()
all_windows = driver.window_handles
driver.switch_to.window(all_windows[-1])
text1 = driver.find_element(By.ID, "sampleHeading").text
sleep(2)
assert "This is a sample page" in text1, 'Different'
print('Same')
driver.close()

driver.switch_to.window(main_window)
sleep(3)

# 3. New Window Message
driver.find_element(By.ID, "messageWindowButton").click()
all_windows = driver.window_handles
driver.switch_to.window(all_windows[-1])
driver.close()

driver.switch_to.window(main_window)
sleep(3)

driver.quit()