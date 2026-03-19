from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opts= webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)

driver.get('https://abc.com/')
driver.maximize_window()

wait_obj = WebDriverWait(driver,10, poll_frequency=200) ## by default explicit wait has 500ms or 0.5 sec poll frequency

submit_button = wait_obj.until(EC.element_to_be_clickable((By.ID,'button')))
submit_button.click()


driver.quit()


## Explicit wait
# An explicit wait in Selenium is used to wait for a specific
# condition to happen before moving forward in the script.
# Unlike implicit wait, it is not global and is applied only
# to particular elements or situations where you need it.
# With explicit wait, you can wait for things like an element
# becoming visible, clickable, or having certain text.
# It works by checking the condition repeatedly until it
# is met or the maximum time is reached, and if the
# condition is satisfied earlier, the script continues
# immediately. This makes it very useful for dynamic web
# pages where elements load at different times.
# Explicit waits give more control and are more reliable
# than implicit waits, especially for complex applications,
# and they are generally preferred in most real-world automation scenarios.

# | Feature              | Implicit Wait                                                     | Explicit Wait                                                                                                                                                                    |
# | -------------------- | ----------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
# | Definition           | Waits for a fixed time before throwing error if element not found | Waits for a specific condition before proceeding                                                                                                                                 |
# | Scope                | Global (applies to all elements)                                  | Local (used only where needed)                                                                                                                                                   |
# | Conditions           | Only checks if element is present in DOM                          | Checks visibility, clickability, text, etc.                                                                                                                                      |
# | Flexibility          | Less flexible                                                     | More flexible and powerful                                                                                                                                                       |
# | Best For             | Simple pages                                                      | Dynamic pages                                                                                                                                                                    |
# | **Imports (Python)** | *(no extra import needed)*                                        | `from selenium.webdriver.common.by import By`<br>`from selenium.webdriver.support.ui import WebDriverWait`<br>`from selenium.webdriver.support import expected_conditions as EC` |
# | **Example (Python)** | `driver.implicitly_wait(10)`                                      | `wait = WebDriverWait(driver, 10)`<br>`wait.until(EC.visibility_of_element_located((By.ID, "example")))`                                                                         |


#  Polling Frequency kya hota hai?
# #  Simple words me:
# # “Selenium kitni der ke gap me baar-baar check kare ki condition satisfy hui ya nahi”
# # Default Behavior
# #  By default:
# # Polling Frequency = 0.5 seconds (500 ms)
# # Matlab:
# # Agar tumne WebDriverWait(driver, 10) diya
# # To Selenium:
#  Har 0.5 sec me check karega
# Max 10 sec tak

# Fluent wait in Python Selenium is an advanced type
# of explicit wait that lets you control how long to
# wait, how often Selenium should check for the condition
# (polling frequency), and which exceptions to ignore while
# waiting. Instead of checking continuously, it checks at
# defined intervals and keeps trying until the condition
# is met or the timeout is reached. This makes it very useful
# for dynamic or unstable elements that may take time to load
# or may temporarily throw errors. In Python, fluent wait is
# implemented using WebDriverWait by setting parameters like
# poll_frequency and ignored_exceptions.
