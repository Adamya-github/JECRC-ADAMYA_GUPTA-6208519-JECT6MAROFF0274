from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opts= webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)

driver.get('https://abc.com')
driver.maximize_window()
wait = WebDriverWait(driver,10)
image = wait.until(EC.presence_of_all_elements_located((By.XPATH,'//figure[@class="Image aspect-ratio--parent tile__imagecontainer"]/div[2]/picture/img')))
for i in image:
    print(i.get_attribute('src'))

print('Task1 work completed')
driver.quit()
