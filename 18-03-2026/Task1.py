from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)
driver.get("https://the-internet.herokuapp.com/")
sleep(2)

# 1. Find "Checkboxes" using LINK_TEXT
checkbox_link = driver.find_element(By.LINK_TEXT, "Checkboxes")
print("Checkbox found")
sleep(2)

# 2. Find "Drag and Drop" using PARTIAL_LINK_TEXT
drag_drop_link = driver.find_element(By.PARTIAL_LINK_TEXT, "Drag")
print("Drag and Drop found")
sleep(2)

# 3. Count the number of <li> elements
li_elements = driver.find_elements(By.TAG_NAME, "li")
print("Total list item elements:", len(li_elements))
sleep(2)

# 4. Navigate to the next page
driver.get("https://the-internet.herokuapp.com/tables")
sleep(2)

# 5. Write an XPath to find the "Web Site" (td) for the person with email "jdoe@hotmail.com" in table 1 (Hint: Use text() and ancestor/following sibling or preceding-sibling).
website = driver.find_element(By.XPATH, "//table[@id='table1']//td[text()='jdoe@hotmail.com']/following-sibling::td[2]")
print("Website:", website.text)
sleep(2)

# 6. XPath for Delete link for Last Name "Bach"
delete_link = driver.find_element(By.XPATH, "//table[@id='table1']//td[text()='Bach']/following-sibling::td/a[text()='delete']")
sleep(2)

# 7. XPath for the second table using indexing
second_table = driver.find_element(By.XPATH, "//table[2]")
print("Table 2 found")
sleep(2)

# 8. Find "$100.00" in table 2 and get its parent <tr>
cell = driver.find_element(By.XPATH, "//table[@id='table2']//td[text()='$100.00']")
parent_row = cell.find_element(By.XPATH, "./parent::tr")
print("Parent row text:", parent_row.text)
sleep(2)

driver.quit()
