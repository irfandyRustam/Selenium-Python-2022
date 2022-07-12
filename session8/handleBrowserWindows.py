import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()

# windowID = driver.current_window_handle
# print(windowID) # CDwindow-46827BC915D891917BEADA65B677AD8B
#                 # CDwindow-E464889BFCBF3CC8A0C55046699D046A

driver.find_element(By.LINK_TEXT, "OrangeHRM, Inc").click()
windowIDs = driver.window_handles

# Approach 1
# parentWindowID = windowIDs[0]   # CDwindow-3CB7728E6827C0C6DF39E5DCBF8F5384
# childWindowID = windowIDs[1]    # CDwindow-F556BDA50075C33C44CCD63EFDAA3B52
# # print(parentWindowID, childWindowID)
#
# driver.switch_to.window(childWindowID)
# print("Title of the child window ", driver.title)
#
# driver.switch_to.window(parentWindowID)
# print("Title of the parent window ", driver.title)

# Approach 2
# for winID in windowIDs:
#     driver.switch_to.window(winID)
#     print(driver.title)

# Close specific browser windows
for winID in windowIDs:
    driver.switch_to.window(winID)
    if driver.title == 'OrangeHRM HR Software | Free & Open Source HR Software | HRMS | HRIS':
        driver.close()