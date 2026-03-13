# from altair.theme import options
from selenium import webdriver
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
opts.add_argument('--headless')
## use of --headless: This runs the browser in the background without a visible graphical user interface (GUI)

driver = webdriver.Chrome(options = opts)
driver.get('https://www.myntra.com')
sleep(4)
print('its working fine')