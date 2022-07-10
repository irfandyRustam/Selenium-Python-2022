from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://money.rediff.com/gainers")
driver.maximize_window()

# self
# text_msg = driver.find_element(By.XPATH, "//a[contains(text(),'Transcorp Inter')]/self::a").text
# print(text_msg) #Transcorp Inter

# parent
# text_msg = driver.find_element(By.XPATH, "//a[contains(text(),'Transcorp Inter')]/parent::td").text
# print(text_msg)

# parent
# childs = driver.find_elements(By.XPATH, "//a[contains(text(),'Transcorp Inter')]/ancestor::tr/child::td")
# print(len(childs))  #5

# ancestor
# text_msg = driver.find_element(By.XPATH, "//a[contains(text(),'Transcorp Inter')]/ancestor::tr").text
# print(text_msg) #Transcorp Inter X 26.75 29.40 + 9.91

# descendant
# descendants = driver.find_elements(By.XPATH, "//a[contains(text(),'Transcorp Inter')]/ancestor::tr/descendant::*")
# print("Number of descendant nodes: ", len(descendants))   #7

# following
# followings = driver.find_elements(By.XPATH, "//a[contains(text(),'Transcorp Inter')]/ancestor::tr/following::*")
# print("Number of following nodes: ", len(followings))

# following-sibling
# followingSiblings = driver.find_elements(By.XPATH, "//a[contains(text(),'Transcorp Inter')]/ancestor::tr/following-sibling::tr")
# print("Number of following siblings: ", len(followingSiblings))

# preceding
# precedings = driver.find_elements(By.XPATH, "//a[contains(text(),'Transcorp Inter')]/ancestor::tr/preceding::tr")
# print("Number of preceding nodes: ", len(precedings))

# preceding-sibling
precedingSiblings = driver.find_elements(By.XPATH, "//a[contains(text(),'Transcorp Inter')]/ancestor::tr/preceding-sibling::tr")
print("Number of preceding siblings: ", len(precedingSiblings))

driver.close()