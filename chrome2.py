import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Set the path to the ChromeDriver executable
# chrome_driver_path = '/usr/bin/chromedriver'

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument('--headless')  # Enable headless mode

chrome_driver_path = '/home/brandon/Downloads/chromedriver/chromedriver'
# Set up ChromeDriver service
service = Service(chrome_driver_path)

# Set up Chrome WebDriver with the service and options
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get('http://www.google.com/')

time.sleep(7)  # Let the user actually see something!

print("Completed successfully!..")
driver.quit()
