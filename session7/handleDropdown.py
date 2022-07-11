from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

serv_obj = Service("C:\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://www.opencart.com/index.php?route=account/register")
driver.maximize_window()

# ddCountry_ele = driver.find_element(By.XPATH, "//select[@id='input-country']")
ddCountry = Select(driver.find_element(By.XPATH, "//select[@id='input-country']"))

# Select option from dropdown
# ddCountry.select_by_visible_text("India")
# ddCountry.select_by_value("10") #Argentina
# ddCountry.select_by_index(13) #Australia

# Capture all the options and print them
allOptions = ddCountry.options
print("Total number of options:", len(allOptions))
# for opt in allOptions:
#     print(opt.text)

# Select option from dropdown without using built-in methods
# for opt in allOptions:
#     if opt.text == "India":
#         opt.click()
#         break

optionsAll = driver.find_elements(By.XPATH, "//*[@id='input-country']/option")
print(len(optionsAll))