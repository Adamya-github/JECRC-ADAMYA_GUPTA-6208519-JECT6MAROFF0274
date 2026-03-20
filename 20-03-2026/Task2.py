from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep

opts= webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)

driver.get(r'C:\Users\Adamya Gupta\OneDrive\Desktop\Testing_Tech\JECRC\20-03-2026\playlist.html')
driver.maximize_window()

song_list = driver.find_element(By.ID, 'songs')
select= Select(song_list)
songs = driver.find_elements(By.XPATH, "//optgroup[@label='One Direction']/option")

if select.is_multiple:
    for i in songs:
        select.select_by_visible_text(i.text)

driver.find_element(By.XPATH, '//button[text()="Add to Playlist"]').click()
print([i.text for i in select.all_selected_options])

sleep(2)
driver.quit()