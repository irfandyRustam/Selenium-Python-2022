import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()

# Login
driver.find_element(By.ID, "txtUsername").send_keys("Admin")
driver.find_element(By.ID, "txtPassword").send_keys("admin123")
driver.find_element(By.ID, "btnLogin").click()
time.sleep(2)

# Admin > User Management > Users
admin = driver.find_element(By.XPATH, "//a[@id='menu_admin_viewAdminModule']")
userManagement = driver.find_element(By.XPATH, "//a[@id='menu_admin_UserManagement']")
users = driver.find_element(By.XPATH, "//a[@id='menu_admin_viewSystemUsers']")

# MouseHover
act = ActionChains(driver)
act.move_to_element(admin).move_to_element(userManagement).move_to_element(users).click().perform()