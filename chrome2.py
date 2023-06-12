import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service


# Set the path to the ChromeDriver executable
chrome_driver_path = '/usr/bin/chromedriver'

# Set up ChromeDriver service
service = Service(chrome_driver_path)

# Set up Chrome WebDriver with the service
driver = webdriver.Chrome(service=service) # Optional argument, if not specified will search path.

driver.get('http://www.google.com/')

time.sleep(2) # Let the user actually see something!

driver.quit()