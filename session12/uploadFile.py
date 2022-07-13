import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)
driver.get("https://www.monster.com.my/")
driver.maximize_window()

driver.find_element(By.XPATH, "//span[text()='Upload Resume']/parent::a").click()
driver.find_element(By.XPATH, "(//input[@id='file-upload'])[1]").send_keys("C:\Sample.pdf")
print("Upload success")