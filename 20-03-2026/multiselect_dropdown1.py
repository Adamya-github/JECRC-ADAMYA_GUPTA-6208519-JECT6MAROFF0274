from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep

opts= webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)

driver.get(r'C:\Users\Adamya Gupta\OneDrive\Desktop\Testing_Tech\JECRC\20-03-2026\playlist.html') ## when sending pdf path it will open and you can read it and for document when you pass path it will download, and then you have to manually open via file explorer and read it
driver.maximize_window()

multi_drop_song = driver.find_element(By.ID,'songs')
select = Select(multi_drop_song)

if select.is_multiple:
    select.select_by_index(4)
    select.select_by_visible_text('Shape of You')
    select.select_by_visible_text('Animals')

print([i.text for i in select.options])
print(len(select.options))
print([i.text for i in select.all_selected_options])

driver.find_element(By.XPATH, '//button[text()="Add to Playlist"]').click()


sleep(5)

driver.quit()