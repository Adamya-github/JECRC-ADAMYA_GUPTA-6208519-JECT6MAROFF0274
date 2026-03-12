## driver.close() it will close current windows but doesn't affect the connection
## driver,quit() it will close all windows and quit the connection that is come out of connection

from selenium import webdriver

opt = webdriver.ChromeOptions()
opt.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opt)
driver.get('https://supertails.com')
driver.maximize_window()


opt = webdriver.EdgeOptions()
opt.add_experimental_option('detach', True)
driver = webdriver.Edge(options=opt)
driver.get('https://supertails.com')
driver.maximize_window()

opt = webdriver.FirefoxOptions()
opt.set_preference("detach", True)
driver = webdriver.Firefox(options=opt)
driver.get('https://supertails.com')
driver.maximize_window()

driver.close()
driver.quit()

