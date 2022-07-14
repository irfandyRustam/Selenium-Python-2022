import time
import os
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)
# driver.get("https://demo.nopcommerce.com/")
# driver.maximize_window()

# regLink = Keys.CONTROL + Keys.RETURN
# driver.find_element(By.LINK_TEXT, "Register").send_keys(regLink)

# New Tab - Selenium 4 : Open a new tab and switch to a new tab
driver.get("https://demo.nopcommerce.com/")
driver.switch_to.new_window('window')   # tab - open new tab in same window # window - open a new separate browser window
driver.get("https://opensource-demo.orangehrmlive.com/")
