from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

# Click on link
# driver.find_element(By.LINK_TEXT, "Digital downloads").click()
# driver.find_element(By.PARTIAL_LINK_TEXT, "Digital").click()

# Find number of link in a page
# links = driver.find_elements(By.TAG_NAME, 'a')
links = driver.find_elements(By.XPATH, '//a')
print("Total number of links:", len(links))

# Print all the link names
for link in links:
    print(link.text)