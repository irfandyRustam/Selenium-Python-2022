# Test Case
# 1. Open Web Browser (Chrome/Firefox/Edge)
# 2. Open URL [https://admin-demo.nopcommerce.com/login]
# 3. Enter username (admin@yourstore.com)
# 4. Enter password (admin)
# 5. Click on Login
# 6. Capture title of the dashboard page (Actual title)
# 7. Verify the title of the page : “Dashboard / nopCommerce administration” (Expected)
# 8. Close browser

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
# driver = webdriver.Chrome()
driver.get("https://admin-demo.nopcommerce.com/login")
driver.find_element(By.ID, "Email").clear()
driver.find_element(By.ID, "Email").send_keys("admin@yourstore.com")
driver.find_element(By.ID, "Password").clear()
driver.find_element(By.ID, "Password").send_keys("admin")
driver.find_element(By.XPATH, "//button[@type='submit']").click()
act_title = driver.title
exp_title = "Dashboard / nopCommerce administration"
if act_title == exp_title:
    print("Login Test Passed")
else:
    print("Login Test Failed")
driver.close()