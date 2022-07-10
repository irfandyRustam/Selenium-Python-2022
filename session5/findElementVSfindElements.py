from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://demo.nopcommerce.com/")

# ---- find_element() - return single webElement ------
# 1) Locator matching with single webElement
# element = driver.find_element(By.XPATH, "//input[@id='small-searchterms']")
# element.send_keys("Apple MacBook Pro 13-inch")

# 2) Locator matching with multiple webElements
# element = driver.find_element(By.XPATH, "//div[@class='footer']//a")
# print(element.text) # print first link from the footer "Sitemap"

# 3) Element not available then throw NoSuchElementException
# loginElement = driver.find_element(By.LINK_TEXT, "Log")
# loginElement.click()

# ---- find_elements() - return multiple webElements ------
# 1) Locator matching with single webElement
# elements = driver.find_elements(By.XPATH, "//input[@id='small-searchterms']")
# print(len(elements))    # 1
# elements[0].send_keys("Apple MacBook Pro 13-inch")

# 2) Locator matching with multiple webElements
# elements = driver.find_elements(By.XPATH, "//div[@class='footer']//a")
# print(len(elements))    # 23
# # print(elements[0].text) # Sitemap
# for ele in elements:
#     print(ele.text)

# 3) Element not available - zero
elements = driver.find_elements(By.LINK_TEXT, "Log")
print("elements returned: ", len(elements))

driver.quit()