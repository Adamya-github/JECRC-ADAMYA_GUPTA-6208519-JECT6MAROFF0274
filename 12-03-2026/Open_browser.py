# To open Chrome browser
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
sleep(1)
driver.get('https://supertails.com')
driver.maximize_window() ## use to maximize the windows
sleep(2)
driver.back()
sleep(2)
driver.forward()
sleep(2)
driver.refresh()
sleep(2)
driver.minimize_window()
sleep(2)


driver = webdriver.Edge()
sleep(2)
driver.get('https://supertails.com')
driver.maximize_window() ## use to maximize the windows
sleep(2)
driver.back()
sleep(2)
driver.forward()
sleep(2)
driver.refresh()
sleep(2)
driver.minimize_window()
sleep(2)


# driver = (webdriver.Firefox()) ## not working in my system, wait for some time, then it is working
# sleep(2)
# driver.get('https://supertails.com')
# driver.maximize_window() ## use to maximize the windows
# sleep(2)
# driver.back()
# sleep(2)
# driver.forward()
# sleep(2)
# driver.refresh()
# sleep(2)
# driver.minimize_window()
# sleep(2)

