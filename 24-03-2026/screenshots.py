import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

folder = os.path.join(os.getcwd(),'Screenshots')
os.makedirs(folder,exist_ok=True)

driver = webdriver.Chrome()

driver.get('https://www.marvel.com/movies/blade')

driver.maximize_window()

sleep(2)

driver.save_screenshot(f"{folder}/full_scr.png")
sleep(2)