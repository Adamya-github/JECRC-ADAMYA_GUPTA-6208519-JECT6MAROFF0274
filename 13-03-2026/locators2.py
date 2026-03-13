from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(options= opts)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
sleep(1)

## advantage of XPath--->

# | Feature          | CSS Selector                                          | XPath                                              |
# | ---------------- | ----------------------------------------------------- | -------------------------------------------------- |
# | Definition       | Pattern used to select HTML elements using CSS syntax | Language used to navigate XML/HTML documents       |
# | Syntax           | Short and simple                                      | Longer and more complex                            |
# | Speed            | Faster in most browsers                               | Slightly slower                                    |
# | Direction        | Works **only from parent → child**                    | Works **both directions (parent, child, sibling)** |
# | Complexity       | Easier to write and read                              | More powerful but harder                           |
# | Browser support  | Supported by all modern browsers                      | Supported by all browsers                          |
# | Finding text     | Cannot directly locate element by text                | Can locate elements by text                        |
# | Traversing nodes | Limited traversal                                     | Full DOM traversal                                 |

# | Feature             | CSS Selector                         | XPath                                                       |
# | ------------------- | ------------------------------------ | ----------------------------------------------------------- |
# |   Speed             | Faster                               | Slower                                                      |
# |   Syntax            | Short, simple                        | Longer, complex                                             |
# |   Traversal         | Only parent → child                  | Parent → child → sibling → ancestor                         |
# |   Finding by text   | ❌ Cannot locate by text              | ✔ Can locate by text using `text()`                         |
# |   Browser support   | ✔ All modern browsers                | ✔ All modern browsers                                       |
# |   Ease of use       | ✔ Easy to learn and read             | ❌ Harder for beginners                                      |
# |   Performance       | ✔ Faster for large DOM               | ❌ Slightly slower                                           |
# |   Power             | ❌ Limited (cannot traverse backward) | ✔ Very powerful and flexible                                |
# |   Maintenance       | ✔ Easier to maintain                 | ❌ Can become complex and fragile                            |
# |   Best use          | Simple locators, IDs, classes        | Complex DOM, locating by text, sibling or parent navigation |


# | Feature        | Absolute XPath                     | Relative XPath                                                                                  |
# | -------------- | ---------------------------------- | ------------------------------------------------------------------------------------------------ |
# | Starts From    | Root `/html`                       | Anywhere `//`                                                                                     |
# | Syntax Example | `/html/body/div[2]/div/form/input` | `//input[@id='username']` , (//tag[@attribute='value'])[index] also index is 1-based not 0-based                       |
# | Fragility      | ❌ Very fragile                     | ✔ Flexible                                                                                     |
# | Maintenance    | ❌ Hard to maintain                 | ✔ Easy to maintain                                                                             |
# | Use Case       | Simple static pages                | Dynamic pages, attribute or text-based selection                                                   |
# | Speed          | Slightly faster                    | Slightly slower                                                                                   |

xpath1 = driver.find_element(By.XPATH, '//input[@placeholder="Enter Name"]')
print(xpath1)
print('Done')

xpath2 = driver.find_element(By.XPATH, '//label[@for="gender"]')
print(xpath2)
print("Done")

xpath3 = driver.find_element(By.XPATH, '//input[@value="sunday"]')
print(xpath3)
print("Done")

xpath4 = driver.find_element(By.XPATH, '//link[@rel="Stylesheet"]')
print(xpath4)
print("Done")

## to find inner text
xpath5 = driver.find_element(By.XPATH, '//a[text()="Home"]')
xpath6 = driver.find_element(By.XPATH, '//a[text()="Udemy Courses"]')
xpath7 = driver.find_element(By.XPATH, '//a[text()="Blog"]')
# xpath8 = driver.find_element(By.XPATH, '//a[text()="Playwright Practice"]') ## this wrong name as right name is PlaywrightPractice so it will show error this time
print(xpath5)
print("Done")
print(xpath6)
print("Done")
print(xpath7)
print("Done")
# print(xpath8)
# print("Done")


xpath9 = driver.find_element(By.XPATH,'//option[contains(text(),"Blue")]')
print(xpath9)
print("Done")


driver.quit()