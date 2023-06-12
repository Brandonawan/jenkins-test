from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Set the path to the ChromeDriver executable
chrome_driver_path = '/usr/bin/chromedriver'

# Set up ChromeDriver service
service = Service(chrome_driver_path)

# Set up Chrome WebDriver with the service
driver = webdriver.Chrome(service=service)

# Navigate to the website you want to test
driver.get('https://www.example.com')

# Perform your Selenium actions
# ...

# Quit the driver
driver.quit()
