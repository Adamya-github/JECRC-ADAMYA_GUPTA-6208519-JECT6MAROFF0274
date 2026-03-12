## write a for loop for numerous browser , just open it
from selenium import webdriver
from time import sleep

# ## Method 1
# l1 = ['Chrome', 'Edge', 'Firefox']
# for i in l1:
#     if i == 'Chrome':
#         driver = webdriver.Chrome()
#         sleep(2)
#     elif i == 'Edge':
#         driver = webdriver.Edge()
#         sleep(2)
#     else:
#         driver = webdriver.Firefox()
#         sleep(2)

## Method 2
l1 = [webdriver.Chrome, webdriver.Edge, webdriver.Firefox]
for i in l1:
    driver = i()
    sleep(2)

