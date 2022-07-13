import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)
driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")
driver.maximize_window()

minSlider = driver.find_element(By.XPATH, "//span[1]")
maxSlider = driver.find_element(By.XPATH, "//span[2]")

print("Location of sliders before moving: ")
print(minSlider.location)   # {'x': 59, 'y': 250}
print(maxSlider.location)   # {'x': 545, 'y': 250}

act = ActionChains(driver)
act.drag_and_drop_by_offset(minSlider, 100, 0).perform()
act.drag_and_drop_by_offset(maxSlider, -100, 0).perform()

print("Location of sliders after moving: ")
print(minSlider.location)   # {'x': 59, 'y': 250}
print(maxSlider.location)   # {'x': 545, 'y': 250}