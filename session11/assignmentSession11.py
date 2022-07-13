import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
act = ActionChains(driver)

# Double Click
field1 = driver.find_element(By.XPATH, "//input[@id='field1']")
field1.clear()
field1.send_keys("welcome")
button = driver.find_element(By.XPATH, "//button[normalize-space()='Copy Text']")
act.double_click(button).perform()  # double click action

# Drag and Drop
source = driver.find_element(By.XPATH, "//div[@id='draggable']")
target = driver.find_element(By.XPATH, "//div[@id='droppable']")
act.drag_and_drop(source, target).perform()

# Drag and Drop Images
john = driver.find_element(By.XPATH, "//h5[normalize-space()='Mr John']")
mary = driver.find_element(By.XPATH, "//h5[normalize-space()='Mary']")
trash = driver.find_element(By.XPATH, "//div[@id='trash']")
act.drag_and_drop(john, trash).perform()
time.sleep(2)
act.drag_and_drop(mary, trash).perform()

# Slider
slider = driver.find_element(By.XPATH, "//span[@class='ui-slider-handle ui-corner-all ui-state-default']")
act.drag_and_drop_by_offset(slider, 100, 0).perform()
print("Location of sliders after moving: ")
print(slider.location)

# Resizable
resizeBox = driver.find_element(By.XPATH, "//div[@class='ui-resizable-handle ui-resizable-se ui-icon ui-icon-gripsmall-diagonal-se']")
driver.execute_script("arguments[0].scrollIntoView();", slider)
time.sleep(1)
act.click_and_hold(resizeBox).move_by_offset(150, 100).perform()

driver.quit()