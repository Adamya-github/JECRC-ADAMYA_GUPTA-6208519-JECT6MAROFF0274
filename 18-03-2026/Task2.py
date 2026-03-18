from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)
driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window()
sleep(3)

# 1.
driver.find_element(By.ID, "firstName").send_keys("Adamya")
sleep(3)

# 2.
driver.find_element(By.ID, "lastName").send_keys("Gupta")
sleep(3)

# 3.
driver.find_element(By.ID, "userEmail").send_keys("adamya@gmail.com")
sleep(3)

# 4.
driver.find_element(By.XPATH, "//label[text()='Male']").click()
sleep(3)

# 5.
driver.find_element(By.ID, "userNumber").send_keys("1234567890")
sleep(3)

# 6.
subject = driver.find_element(By.ID, "subjectsInput")
subject.send_keys("Computer Science")
subject.send_keys(Keys.ENTER)
sleep(3)

# 7.
driver.find_element(By.XPATH, "//label[text()='Reading']").click()
driver.find_element(By.XPATH, "//label[text()='Music']").click()
sleep(3)

# 8.
driver.find_element(By.ID, "uploadPicture").send_keys(r"C:\Users\Adamya Gupta\OneDrive\Desktop\Testing_Tech\JECRC\18-03-2026\Profile.jpg")
sleep(3)

# 9.
driver.find_element(By.ID, "currentAddress").send_keys("JECRC University, Jaipur, Rajasthan")
sleep(3)

# 10.
state = driver.find_element(By.ID, "react-select-3-input")
state.send_keys("Rajasthan", Keys.ENTER)
sleep(3)

# 11.
city = driver.find_element(By.ID, "react-select-4-input")
city.send_keys("Jaipur", Keys.ENTER)
sleep(3)

# 12.
driver.find_element(By.ID, "submit").click()
sleep(3)

driver.quit()
