import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

currentDir = os.getcwd()
# driver.save_screenshot("C:\\Users\\admin\\PycharmProjects\\SeleniumPython2022\\session13\\homepage.png")
driver.save_screenshot(currentDir + "\\homepage.png")
# driver.get_screenshot_as_file(currentDir + "\\homepage.png")
# driver.get_screenshot_as_png()    # driver.get_screenshot_as_base64()

driver.quit()