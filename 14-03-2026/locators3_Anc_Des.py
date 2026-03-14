## locator--> link text and partial link text
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(options = opts)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

sleep(2)

xpath1 =driver.find_element(By.LINK_TEXT,'Udemy Courses')
print(xpath1)
print("Done 1")

xpath2 =driver.find_element(By.PARTIAL_LINK_TEXT,'Practice')
print(xpath2)
print("Done 2")

xpath3 = driver.find_elements(By.XPATH,'//td[text()="300"]/ancestor::tr[1]/td[1]')
print(xpath3)
print(len(xpath3))

xpath4 = driver.find_elements(By.XPATH,'//table[@id="taskTable"]/descendant::tbody[@id="rows"]/descendant::tr/td[1]')
print(xpath4)
print(len(xpath4))

driver.quit()