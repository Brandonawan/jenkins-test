import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://the-internet.herokuapp.com/upload")
driver.find_element(By.ID,"file-upload").send_keys("selenium-snapshot.png")
driver.find_element(By.ID,"file-submit").submit()
names = ["brandon", "james"]
index_names = enumerate(names)
index_names_list = list(index_names)
print(index_names_list)

digits = [1.2, 3.5, 6.7, 10.3]
round_digits = map(round, digits)
print(list(round_digits))
if(driver.page_source.find("File Uploaded!")):
    print("file upload success")
else:
    print("file upload not successful")
driver.quit()





