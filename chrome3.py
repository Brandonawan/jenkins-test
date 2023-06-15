import time
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

# Set the Firefox driver to headless mode
options = webdriver.FirefoxOptions()
options.add_argument('-headless')

# Create a new Firefox browser instance
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)

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