from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(options = opts)

driver.get("https://the-internet.herokuapp.com/login")
driver.maximize_window()

sleep(2)

print("Website opened successfully")

xpath1 = driver.find_element(By.XPATH, "//div[@class='row']/descendant::label[text()='Password']")
print(xpath1)
print("Done 1")

driver.quit()

