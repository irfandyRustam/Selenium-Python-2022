import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://itera-qa.azurewebsites.net/home/automation")
driver.maximize_window()

# 1 - Select specific checkbox
# driver.find_element(By.XPATH, "//input[@id='monday']").click()

# 2 - Select all checkboxes
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox' and contains(@id, 'day')]")
print(len(checkboxes)) # 7

# approach 1
# for i in range(len(checkboxes)):
#     checkboxes[i].click()

# approach 2
for checkbox in checkboxes:
    checkbox.click()

# 3 - Select multiple checkboxes by choice
# for checkbox in checkboxes:
#     day = checkbox.get_attribute('id')
#     if day == 'monday' or day == 'sunday':
#         checkbox.click()

# 4 - Select last 2 checkboxes
# range(5, 7) --> 6,7
# total number of elements - 2 = starting index
# for i in range(len(checkboxes) - 2, len(checkboxes)):
#     checkboxes[i].click()

# 5 - Select first 2 checkboxes
# for i in range(len(checkboxes)):
#     if i<2:
#         checkboxes[i].click()

# 6 - Clearing all the checkboxes
for checkbox in checkboxes:
    if(checkbox.is_selected()):
        checkbox.click()

# driver.quit()