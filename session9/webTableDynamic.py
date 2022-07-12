import time
from selenium import webdriver
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
driver.find_element(By.XPATH, "//a[@id='menu_admin_viewAdminModule']").click()
driver.find_element(By.XPATH, "//a[@id='menu_admin_UserManagement']").click()
driver.find_element(By.XPATH, "//a[@id='menu_admin_viewSystemUsers']").click()

# Total rows in a table
rows = len(driver.find_elements(By.XPATH, "//table[@id='resultTable']//tbody/tr"))
print("Total number of rows in a table:", rows)
count = 0
for r in range(1, rows+1):
    status = driver.find_element(By.XPATH, "//table[@id='resultTable']//tr["+ str(r) +"]/td[5]").text
    if status == "Enabled":
        count += 1

print("Total number of users:", rows)
print("Number of enabled users:", count)
print("Number of disabled users:", (rows - count))

driver.close()