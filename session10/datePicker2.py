import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

serv_obj = Service("C:\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()

# Date of Birth
driver.find_element(By.XPATH, "//input[@id='dob']").click() # open datepicker

# Select month
datepickerMonth = Select(driver.find_element(By.XPATH, "//select[@aria-label='Select month']"))
datepickerMonth.select_by_visible_text("Dec")

# Select year
datepickerYear = Select(driver.find_element(By.XPATH, "//select[@aria-label='Select year']"))
datepickerYear.select_by_visible_text("1999")

# Select date - using for loop
dates = driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")
for date in dates:
    if date.text == "25":
        date.click()
        break

# Select date - using dynamic xpath
# driver.find_element(By.XPATH, "//td[@data-handler='selectDay']/a[@data-date='25']").click()