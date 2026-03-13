from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
## ATLAS MODE
opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# opts.add_argument('--headless')
driver = webdriver.Chrome(options= opts)
# sleep(2)
driver.get("https://codehelp-portfolio-website.netlify.app/")
driver.maximize_window()
sleep(1)

nav_bar = driver.find_element(By.CLASS_NAME, 'nav-logo')
print(nav_bar)
nav_items= driver.find_elements(By.CLASS_NAME, 'nav-items')
print(nav_items)
hero= driver.find_element(By.CLASS_NAME, 'hero-section-left')
print(hero)
description= driver.find_element(By.CLASS_NAME, 'hero-section-description')
print(description)
btn_pink= driver.find_element(By.CLASS_NAME, 'btn-pink')
print(btn_pink)

email= driver.find_element(By.NAME, 'email')
print(email)
subject= driver.find_element(By.NAME, 'subject')
print(subject)
name= driver.find_element(By.NAME, 'name')
print(name)


contact= driver.find_element(By.ID, 'contactme')
print(contact)
btn_bottom=driver.find_element(By.ID, 'btn-bottom')
print(btn_bottom)
project1= driver.find_element(By.ID, 'project1')
print(project1)
project2= driver.find_element(By.ID, 'project2')
print(project2)
project3= driver.find_element(By.ID, 'project3')
print(project3)


nav= driver.find_elements(By.TAG_NAME, 'nav')
print(nav)

section= driver.find_elements(By.TAG_NAME, 'section')
print(section)

h2= driver.find_elements(By.TAG_NAME, 'h2')
print(h2)

form= driver.find_elements(By.TAG_NAME, 'form')
print(form)

footer=driver.find_elements(By.TAG_NAME, 'footer')
print(footer)