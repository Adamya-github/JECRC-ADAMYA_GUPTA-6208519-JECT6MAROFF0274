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

xpath1 = driver.find_element(By.XPATH, '//input[@id="username"]/parent')
print(xpath1)
print("Done 1")

# //label[text()='Username']/following-sibling::input # elder siblings
# //input[@id='password']/preceding-sibling::label # younger siblings
# //div[@id='content']/div # immediate child
# //input[@id='username']/parent::div # immediate parent
# //label[@for='username']/following-sibling::input[1] # specific sibling either via index or unique value [@..=""]..
# //label[text()='Username']/following-sibling::input[@id='username'] same specific sibling example
# //div[@id='container']/input[@id='username'] # specific immediate child




driver.quit()

## how can you write xpath for dynamic elements that is it is changing at runtime