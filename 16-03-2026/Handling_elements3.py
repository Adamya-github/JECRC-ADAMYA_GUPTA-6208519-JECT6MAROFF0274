# 1. navigate to flipkart,
# 2. find search field and search for a product,
# 3. get attribute of the product searched,
# 4. Ket enter on search button,
# 5. click on a checkbox or boxes in filter,
# 6. get the text of that  filter
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=opts)

driver.get('https://www.flipkart.com/')
driver.maximize_window()
sleep(2)
search = driver.find_element(By.XPATH, '//input[@placeholder="Search for Products, Brands and More"]')
search.clear()
search.send_keys('titan')
print(search.get_attribute('value'))
search.send_keys(Keys.ENTER)
sleep(2)
click1= driver.find_element(By.XPATH,'//div[text()="Men"]/preceding-sibling::div')
print(driver.find_element(By.XPATH,'//div[text()="Men"]').text)
click1.click()
sleep(5)

src1 = driver.find_element(By.XPATH,'//div[@class="fWB4Ui TTHoOY"]/img') ## * it represent the all html tags/elements when done via copy xpath
print(src1.get_attribute('src'))

driver.quit()