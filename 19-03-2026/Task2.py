from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

opts= webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)
driver.get("https://qavbox.github.io/demo/signup/")
driver.maximize_window()

wait = WebDriverWait(driver, 10)
name = wait.until(EC.visibility_of_element_located((By.NAME, "uname")))
name.send_keys("John Doe")

email = wait.until(EC.visibility_of_element_located((By.ID, "email")))
email.send_keys("john@test.com")

phone = wait.until(EC.visibility_of_element_located((By.ID, "tel")))
phone.send_keys("1234567890")

photo = wait.until(EC.visibility_of_element_located((By.NAME, "datafile")))
photo.send_keys(r"C:\Users\Adamya Gupta\OneDrive\Desktop\Testing_Tech\JECRC\19-03-2026\Profile.png")

gender = wait.until(EC.visibility_of_element_located((By.NAME, "sgender")))
select = Select(gender)
select.select_by_visible_text("Male")

wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@value='two']"))).click()

wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@value='automationtesting']"))).click()
wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@value='java']"))).click()

tool = wait.until(EC.visibility_of_element_located((By.ID, "tools")))
select1 = Select(tool)
select1.select_by_visible_text("Selenium")

wait.until(EC.visibility_of_element_located((By.ID, "submit"))).click()

driver.quit()