import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# Enter input search
driver.find_element(By.XPATH, "//input[@id='Wikipedia1_wikipedia-search-input']").send_keys("Selenium")
driver.find_element(By.XPATH, "//input[@type='submit']").click()
time.sleep(2)

# Capture all links from search results
searchResults = driver.find_elements(By.XPATH, "//div[@id='Wikipedia1_wikipedia-search-results']//a")
for result in searchResults:
    result.click()

# Capture all windowIDs
windowIDs = driver.window_handles
print("Total of windowIDs:",len(windowIDs))
for winID in windowIDs:
    driver.switch_to.window(winID)
    print(driver.title)

# Close all browser window
driver.quit()