from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://www.facebook.com/")
driver.maximize_window()

# --- css selectors locator ---
# tag & id
# driver.find_element(By.CSS_SELECTOR, "input#email").send_keys("abc")
# driver.find_element(By.CSS_SELECTOR, "#email").send_keys("abc")

# tag & class
# driver.find_element(By.CSS_SELECTOR, "input.inputtext").send_keys("abc@gmail.com")
# driver.find_element(By.CSS_SELECTOR, ".inputtext").send_keys("abc@gmail.com")

# tag & attribute
# driver.find_element(By.CSS_SELECTOR, "input[data-testid=royal_email]").send_keys("abc@gmail.com")
# driver.find_element(By.CSS_SELECTOR, "[data-testid=royal_email]").send_keys("abc@gmail.com")

# tag, class & attribute
# driver.find_element(By.CSS_SELECTOR, "input.inputtext[data-testid=royal_pass]").send_keys("xyz")
driver.find_element(By.CSS_SELECTOR, ".inputtext[data-testid=royal_pass]").send_keys("xyz")