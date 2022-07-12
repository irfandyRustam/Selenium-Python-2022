import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()

driver.switch_to.frame(0)   # switch to frame

# 07/13/2022 - mm/dd/yyyy
# driver.find_element(By.XPATH, "//input[@id='datepicker']").send_keys("11/24/2022")

year = "2023"
month = "June"
date = "15"
driver.find_element(By.XPATH, "//input[@id='datepicker']").click()  # open datepicker

while True:
    mon = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
    yr = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text

    if mon == month and yr == year:
        break
    else:
        driver.find_element(By.XPATH, "//span[@class='ui-icon ui-icon-circle-triangle-e']").click() # Next arrow
        # driver.find_element(By.XPATH, "//span[@class='ui-icon ui-icon-circle-triangle-w']").click()  # Previous arrow

# Select date - using for loop
dates = driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")
for ele in dates:
    if ele.text == date:
        ele.click()
        break

# Select date - using dynamic xpath
# time.sleep(2)
# driver.find_element(By.XPATH, "//td[@data-handler='selectDay']/a[@data-date='" + date + "']").click()