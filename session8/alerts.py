import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()

# open alert window
driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Prompt']").click()
time.sleep(5)

alertWindow = driver.switch_to.alert
print(alertWindow.text)
alertWindow.send_keys("welcome")
# alertWindow.accept()    # close alert window by using OK button
alertWindow.dismiss()   # close alert window by using Cancel button