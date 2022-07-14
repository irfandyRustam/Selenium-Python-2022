from selenium import webdriver
from selenium.webdriver.chrome.service import Service

serv_obj = Service("C:\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

# capture cookies from the browser
cookies = driver.get_cookies()
print("Size of cookies:", len(cookies))

# print details of all cookies
# for c in cookies:
#     # print(c)
#     print(c.get('name'), ":", c.get('value'))

# add new cookie to the browser
driver.add_cookie({"name": "MyCookie", "value": "123456"})
cookies = driver.get_cookies()
print("Size of cookies after adding new one:", len(cookies))

# delete specific cookie from the browser
driver.delete_cookie("MyCookie")
cookies = driver.get_cookies()
print("Size of cookies after deleted one:", len(cookies))

# delete all the cookies
driver.delete_all_cookies()
cookies = driver.get_cookies()
print("Size of cookies after deleted all:", len(cookies))

driver.quit()