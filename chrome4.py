from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager

# Set headless mode options
options = Options()
options.headless = True

# Set up the Firefox driver
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)

# Your test code here
# For example, navigating to a website and printing its title
driver.get("https://www.example.com")
print(driver.title)

# Close the browser
driver.quit()
