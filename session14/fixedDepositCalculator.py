import time
from session14 import XLUtils
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options

serv_obj = Service("C:\Drivers\chromedriver.exe")
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}    # disabled popup
chrome_options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(service=serv_obj, options=chrome_options)

driver.implicitly_wait(10)
driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html?classic=true")
driver.maximize_window()
# driver.find_element(By.XPATH, "//button[@id='wzrk-cancel']")    # close popup notification

file = "C:\SeleniumPractice\caldata.xlsx"
rows = XLUtils.getRowCount(file, "Sheet1")

for r in range(2, rows+1):
    # reading data from excel
    principalAmount = XLUtils.readData(file, "Sheet1", r, 1)
    rateOfInterest = XLUtils.readData(file, "Sheet1", r, 2)
    period1 = XLUtils.readData(file, "Sheet1", r, 3)
    period2 = XLUtils.readData(file, "Sheet1", r, 4)
    frequency = XLUtils.readData(file, "Sheet1", r, 5)
    expMaturityValue = XLUtils.readData(file, "Sheet1", r, 6)

    # passing data to the application
    driver.find_element(By.XPATH, "//input[@id='principal']").send_keys(principalAmount)
    driver.find_element(By.XPATH, "//input[@id='interest']").send_keys(rateOfInterest)
    driver.find_element(By.XPATH, "//input[@id='tenure']").send_keys(period1)
    periodDD = Select(driver.find_element(By.XPATH, "//select[@id='tenurePeriod']"))
    periodDD.select_by_visible_text(period2)
    frequencyDD = Select(driver.find_element(By.XPATH, "//select[@id='frequency']"))
    frequencyDD.select_by_visible_text(frequency)
    driver.find_element(By.XPATH, "//*[@id='fdMatVal']/div[2]/a[1]/img").click()    # calculate button
    actualMaturityValue = driver.find_element(By.XPATH, "//span[@id='resp_matval']/strong").text

    # Validation
    if float(expMaturityValue) == float(actualMaturityValue):
        print("Test Passed")
        XLUtils.writeData(file, "Sheet1", r, 8, "Pass")
        XLUtils.fillGreenColor(file, "Sheet1", r, 8)
    else:
        print("Test Failed")
        XLUtils.writeData(file, "Sheet1", r, 8, "Fail")
        XLUtils.fillRedColor(file, "Sheet1", r, 8)

    driver.find_element(By.XPATH, "//img[@class='PL5']").click()    # clear button
    time.sleep(2)

driver.quit()