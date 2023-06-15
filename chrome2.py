import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

# Set up Chrome options
chrome_options = Options()
chrome_options.headless = True  # Enable headless mode

# Set up Chrome WebDriver with the options
driver_service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(options=chrome_options)

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

