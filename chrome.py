import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

# Set up Firefox options
firefox_options = Options()
firefox_options.headless = True

# Set up Firefox WebDriver with the options
driver_service = FirefoxService(executable_path=GeckoDriverManager().install())
driver = webdriver.Firefox(service=driver_service, options=firefox_options)

# Open a website
driver.get('http://www.google.com/')

time.sleep(5)  # Let the page load

# Perform some actions
search_box = driver.find_element('name', 'q')
search_box.send_keys('Selenium 4')
search_box.submit()

time.sleep(5)  # Let the search results load

# Get the search results and print the titles
search_results = driver.find_elements('xpath', '//h3')
for result in search_results:
    print(result.text)

# Quit the WebDriver
driver.quit()
