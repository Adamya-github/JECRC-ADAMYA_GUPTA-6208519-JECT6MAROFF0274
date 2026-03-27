from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.cleartrip.com/")
driver.maximize_window()
driver.implicitly_wait(10)

assert "cleartrip" in driver.current_url, "URL mismatch"

wait = WebDriverWait(driver, 15)
actions = ActionChains(driver)

one_way = wait.until(EC.element_to_be_clickable((By.XPATH, "//p[text()='One way']")))
one_way.click()

from_city = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Where from?']")))
from_city.click()
from_city.send_keys("Delhi")
sleep(2)
from_city.send_keys(Keys.DOWN, Keys.ENTER)

to_city = driver.find_element(By.XPATH, "//input[@placeholder='Where to?']")
to_city.send_keys("Mumbai")
sleep(2)
to_city.send_keys(Keys.DOWN, Keys.ENTER)

driver.find_element(By.XPATH, "//div[contains(@class,'DateInput')]").click()

while True:
    try:
        date = driver.find_element(By.XPATH, "//div[@aria-label='Fri Apr 25 2026']")
        date.click()
        break
    except:
        next_arrow = driver.find_element(By.XPATH, "//svg[@data-testid='rightArrow']")
        actions.move_to_element(next_arrow).click().perform()
        sleep(1)

driver.find_element(By.XPATH, "//button[contains(.,'Search flights')]").click()

wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class,'flightList')]")))

sleep(3)

first_flight = driver.find_element(By.XPATH, "(//div[contains(@class,'flightList')]//div[contains(@class,'row')])[1]")
print("First Flight Details:\n", first_flight.text)

driver.quit()