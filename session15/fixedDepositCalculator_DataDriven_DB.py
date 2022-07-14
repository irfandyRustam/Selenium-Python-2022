import time
import mysql.connector
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

serv_obj = Service("C:\Drivers\chromedriver.exe")
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}    # disabled popup
chrome_options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(service=serv_obj, options=chrome_options)
driver.implicitly_wait(10)
driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html?classic=true")
driver.maximize_window()

try:
    con = mysql.connector.connect(host="localhost", port=3306, user="root", passwd="root", database="mydb")
    curs = con.cursor()  # create cursor
    curs.execute("SELECT * FROM caldata")  # execute query through cursor

    for row in curs:
        # reading data from table db
        principalAmount = row[0]
        rateOfInterest = row[1]
        period1 = row[2]
        period2 = row[3]
        frequency = row[4]
        expMaturityValue = row[5]

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
        else:
            print("Test Failed")

        driver.find_element(By.XPATH, "//img[@class='PL5']").click()    # clear button
        time.sleep(2)
    con.close()  # close connection
except:
    print("Connection failed")

driver.quit()