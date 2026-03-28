from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)

driver.get('https://www.amazon.in/')
driver.maximize_window()
sleep(2)

assert 'amazon' in driver.current_url, 'Error'

wait = WebDriverWait(driver, 10)

searchbox = wait.until(EC.visibility_of_element_located((By.ID, 'twotabsearchtextbox')))
searchbox.send_keys('Headphones')

driver.find_element(By.ID, 'nav-search-submit-button').click()

wait.until(EC.presence_of_element_located((By.XPATH, '//ul[@id="filter-p_123"]/descendant::li[3]'))).click()
wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="priceRefinements"]/descendant::a[6]'))).click()

new_product = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@role="listitem"]/descendant::h2/span')))
product_title = new_product.text
new_product.click()

driver.switch_to.window(driver.window_handles[-1])

product_price = wait.until(EC.presence_of_element_located(
    (By.XPATH, '//span[@class="a-price"]/span[@class="a-offscreen"]'))).text

assert product_title in wait.until(EC.presence_of_element_located(
    (By.ID, 'productTitle'))).text, 'Product not found'

assert product_price in wait.until(EC.presence_of_element_located(
    (By.XPATH, "//span[@class='a-price-whole']"))).text, 'Product not found'

cart_button = wait.until(EC.presence_of_element_located((By.ID, 'add-to-cart-button')))
cart_button.click()

cart = wait.until(EC.presence_of_element_located((By.ID, 'nav-cart')))
cart.click()

assert product_title in wait.until(EC.presence_of_element_located((By.XPATH, '//span[@class="a-truncate-full a-offscreen"]'))).get_attribute('textContent'), 'Wrong Product'

assert product_price in wait.until(EC.presence_of_element_located((By.XPATH, '//span[@class="a-offscreen"]'))).text, 'Wrong product'
print('successful')
driver.quit()
