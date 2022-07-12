# 1) Count number of rows & columns
# 2) Read specific row & column data
# 3) Read all the rows & columns data
# 4) Read data based on condition (ex: List books name whose author is Mukesh)

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# 1) Count number of rows & columns
rowsNo = len(driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr"))
columnsNo = len(driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr[1]/th"))
print("Rows:", rowsNo, " Columns:", columnsNo)   # Rows: 7  Columns: 4

# 2) Read specific row & column data
# data = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[5]/td[1]").text
# print(data)

# 3) Read all the rows & columns data
# print("Printing all the rows and columns data ..")
# for r in range(2, rowsNo+1):
#     for c in range(1, columnsNo+1):
#         data = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
#         print(data, end='   ')
#     print()

# 4) Read data based on condition (ex: List books name whose author is Mukesh)
for r in range(2, rowsNo+1):
    authorName = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[" + str(r) + "]/td[2]").text
    if authorName == "Mukesh":
        bookName = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[" + str(r) + "]/td[1]").text
        price = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[" + str(r) + "]/td[4]").text
        print(bookName, "\t", authorName, "\t", price)

driver.quit()