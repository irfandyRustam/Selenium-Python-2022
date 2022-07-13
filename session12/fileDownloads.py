import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

location = os.getcwd()  # get current directory path
def chrome_setup():
    from selenium.webdriver.chrome.service import Service
    serv_obj = Service("C:\Drivers\chromedriver.exe")
    preferences = {"download.default_directory": location}
    ops = webdriver.ChromeOptions()
    ops.add_extension("AdBlock5.0.2.0.crx")   # install AdBlock extension to disable ads
    ops.add_experimental_option("prefs", preferences)   # Download files in desired location
    driver = webdriver.Chrome(service=serv_obj, options=ops)
    return driver

def edge_setup():
    from selenium.webdriver.edge.service import Service
    serv_obj = Service("C:\Drivers\msedgedriver.exe")
    preferences = {"download.default_directory": location}
    ops = webdriver.EdgeOptions()
    ops.add_extension("AdBlock5.0.2.0.crx")  # install AdBlock extension to disable ads
    ops.add_experimental_option("prefs", preferences)   # Download files in desired location
    driver = webdriver.Edge(service=serv_obj, options=ops)
    return driver

def firefox_setup():
    from selenium.webdriver.firefox.service import Service
    serv_obj = Service("C:\Drivers\geckodriver.exe")
    ops = webdriver.FirefoxOptions()
    ops.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/msword") # list of MIME types to save to disk without asking what to use to open the file
    ops.set_preference("browser.download.manager.showWhenStarting", False)
    ops.set_preference("browser.download.folderList", 2) # 0-desktop 1-downloads folder 2-desired location
    ops.set_preference("browser.download.dir", location)
    # ops.set_preference("pdfjs.disabled", True) # disable the built-in PDF viewer
    driver = webdriver.Firefox(service=serv_obj, options=ops)
    return driver

# Automation Code
# driver = chrome_setup()
# driver = edge_setup()
driver = firefox_setup()
driver.install_addon("adblock_for_firefox-5.0.2.xpi", temporary=True)   # install addon for firefox

driver.implicitly_wait(10)
driver.get("https://filesamples.com/formats/doc")
driver.maximize_window()

# close child window (adblock extension page)
parent = driver.window_handles[0]
child = driver.window_handles[1]
driver.switch_to.window(child)
driver.close()

# Click Download Button
time.sleep(2)
driver.switch_to.window(parent)
downloadBtn = driver.find_element(By.XPATH, "(//a[@class='btn btn-primary pull-right'][normalize-space()='Download'])[1]")
driver.execute_script("arguments[0].scrollIntoView();", downloadBtn)
downloadBtn.click()

print("Download Success")
# driver.quit()