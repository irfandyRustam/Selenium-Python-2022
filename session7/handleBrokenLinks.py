# we need to install requests package through File > Settings > ProjectInterpreter > Search for "requests" package
import requests as requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("http://www.deadlinkcity.com/")
driver.maximize_window()

allLinks = driver.find_elements(By.TAG_NAME, 'a')
countBroken = 0
countValid = 0
for link in allLinks:
    url = link.get_attribute('href')
    try:
        res = requests.head(url)
    except:
        None
    if res.status_code >= 400:
        print(url, " is a broken link")
        countBroken += 1
    else:
        print(url, " is a valid link")
        countValid += 1

print("Total number of broken links:", countBroken)
print("Total number of valid links:", countValid)
driver.quit()