# Test Case
# 1. Open Web Browser (Chrome/Firefox/Edge)
# 2. Open URL [https://opensource-demo.orangehrmlive.com/]
# 3. Enter username (Admin)
# 4. Enter password (admin123)
# 5. Click on Login
# 6. Capture title of the home page (Actual title)
# 7. Verify the title of the page : OrangeHRM (Expected)
# 8. Close browser

# ------- Selenium 3 -----------
from selenium import webdriver

# driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
# driver = webdriver.Chrome()
# driver.get("https://opensource-demo.orangehrmlive.com/")
# driver.find_element_by_name("txtUsername").send_keys("Admin")
# driver.find_element_by_id("txtPassword").send_keys("admin123")
# driver.find_element_by_id("btnLogin").click()
# act_title = driver.title
# exp_title = "OrangeHRM"
# if act_title == exp_title:
#     print("Login Test Passed")
# else:
#     print("Login Test Failed")
# driver.close()

# ------- Selenium 4 -----------
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
# driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.find_element(By.NAME, "txtUsername").clear()
driver.find_element(By.NAME, "txtUsername").send_keys("Admin")
driver.find_element(By.ID, "txtPassword").clear()
driver.find_element(By.ID, "txtPassword").send_keys("admin123")
driver.find_element(By.ID, "btnLogin").click()
act_title = driver.title
exp_title = "OrangeHRM"
if act_title == exp_title:
    print("Login Test Passed")
else:
    print("Login Test Failed")
driver.close()