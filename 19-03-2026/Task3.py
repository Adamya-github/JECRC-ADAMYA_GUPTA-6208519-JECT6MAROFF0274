from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opts= webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)
driver.get("https://www.amazon.in/")
driver.maximize_window()

wait = WebDriverWait(driver, 15)
search_box = wait.until(EC.visibility_of_element_located((By.ID, "twotabsearchtextbox")))
search_box.send_keys("mobile")

suggestions = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.s-suggestion")))
suggestions[3].click()

sorting = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='a-button-text a-declarative']/span")))
sorting.click()

newest = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Newest')]")))
newest.click()

free_shipping = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[@id='p_n_free_shipping_eligible/205563695031']/span/a/div")))
free_shipping.click()

first_product = wait.until(EC.presence_of_element_located((By.XPATH, "(//div[@data-component-type='s-search-result'])[1]")))

name = first_product.find_element(By.XPATH, '//div[@class="a-section a-spacing-small a-spacing-top-small"]/descendant::span')
# name = first_product.find_element(By.XPATH, '//h2[@class="a-size-base-plus a-spacing-none a-color-base a-text-normal"]/span') ## For shirt or clothing
price = first_product.find_element(By.XPATH, "//span[@class='a-price-whole']")

print(name.text," = ",price.text)

driver.quit()