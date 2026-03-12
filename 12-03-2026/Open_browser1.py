# To open Chrome browser
from selenium import webdriver
from time import sleep

opt = webdriver.ChromeOptions() ## use of ChromeOptions
opt.add_experimental_option('detach', True) ## it will insure that chrome don't go sleep or closr by own
driver = webdriver.Chrome(options=opt)
# sleep(1)
driver.get('https://supertails.com')
driver.maximize_window()
# sleep(2)
driver.back()
# sleep(2)
driver.forward()
# sleep(2)
driver.refresh()
# sleep(2)
driver.minimize_window()
# sleep(2)


opt = webdriver.EdgeOptions()
opt.add_experimental_option('detach', True)
driver = webdriver.Edge(options=opt)
# sleep(1)
driver.get('https://supertails.com')
driver.maximize_window()
# sleep(2)
driver.back()
# sleep(2)
driver.forward()
# sleep(2)
driver.refresh()
# sleep(2)
driver.minimize_window()
# sleep(2)


opt = webdriver.FirefoxOptions()
opt.set_preference("detach", True)
driver = webdriver.Firefox(options=opt)
# sleep(1)
driver.get('https://supertails.com')
driver.maximize_window()
# sleep(2)
driver.back()
# sleep(2)
driver.forward()
# sleep(2)
driver.refresh()
# sleep(2)
driver.minimize_window()
# sleep(2)