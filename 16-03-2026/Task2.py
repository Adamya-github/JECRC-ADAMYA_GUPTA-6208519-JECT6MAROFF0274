from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get("https://demoqa.com/radio-button")

driver.maximize_window()

print("Page Title:", driver.title)

sleep(2)

yes_radio = driver.find_element(By.XPATH, "//input[@id='yesRadio']")
yes_radio.click()

sleep(2)

result = driver.find_element(By.XPATH, '//p[@class="mt-3"]')
print("Result Message:", result.text)

print("Radio Button Class:", yes_radio.get_attribute("class"))
print("Radio Button ID:", yes_radio.get_attribute("for"))

print("Current URL:", driver.current_url)


driver.quit()
