from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://www.snapdeal.com/")
driver.get("https://www.amazon.com/")

driver.back()   # snapdeal
driver.forward()    # amazon
driver.refresh()

driver.quit()