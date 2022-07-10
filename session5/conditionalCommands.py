from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://demo.nopcommerce.com/register")
driver.maximize_window()

# is_displayed(), is_enabled()
searchbox = driver.find_element(By.XPATH, "//input[@id='small-searchterms']")
print("Display status: ", searchbox.is_displayed()) #True
print("Enable status: ", searchbox.is_enabled())    #True

# is_selected() - for radio buttons and checkboxes
rdMale = driver.find_element(By.XPATH, "//input[@id='gender-male']")
rdFemale = driver.find_element(By.XPATH, "//input[@id='gender-female']")
print("Default radio button status: ")
print(rdMale.is_selected()) #False
print(rdFemale.is_selected())   #False

rdMale.click()  # select male radio button
print("After selecting male radio button: ")
print(rdMale.is_selected()) #True
print(rdFemale.is_selected())   #False

rdFemale.click()  # select female radio button
print("After selecting female radio button: ")
print(rdMale.is_selected()) #False
print(rdFemale.is_selected())   #True

driver.quit()