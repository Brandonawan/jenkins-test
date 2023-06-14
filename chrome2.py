import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Set the path to the ChromeDriver executable
chrome_driver_path = '/home/brandon/Downloads/chromedriver/chromedriver'

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument('--headless')  # Enable headless mode

# Set up Chrome WebDriver with the options
driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)

driver.get('http://www.google.com/')

time.sleep(7)  # Let the user actually see something!

print("Completed successfully!..")
driver.quit()
