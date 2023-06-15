from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

# Set headless mode options
options = Options()
options.headless = True

# Set up the Firefox driver service
service = Service(GeckoDriverManager().install())

# Set the path to the Firefox binary
firefox_binary_path = '/usr/bin/firefox'  # Replace with the actual path to the Firefox binary
options.binary_location = firefox_binary_path

# Set up the Firefox driver
driver = webdriver.Firefox(service=service, options=options)

# Your test code here
# For example, navigating to a website and printing its title
driver.get("https://www.example.com")
print(driver.title)

# Close the browser
driver.quit()
