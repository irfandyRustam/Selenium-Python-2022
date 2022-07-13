import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.maximize_window()

act = ActionChains(driver)
rome = driver.find_element(By.XPATH, "//div[@id='box6']")
italy = driver.find_element(By.XPATH, "//div[@id='box106']")
act.drag_and_drop(rome, italy).perform()

washington = driver.find_element(By.XPATH, "//div[@id='box3']")
US = driver.find_element(By.XPATH, "//div[@id='box103']")
act.drag_and_drop(washington, US).perform()