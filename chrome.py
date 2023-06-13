from selenium import webdriver

# Set the path to the ChromeDriver executable
chrome_driver_path = '/usr/bin/chromedriver'

# Set up Chrome WebDriver
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# Navigate to the website you want to test
driver.get('https://www.example.com')

# Perform your Selenium actions
# ...

print("Completed successfully!..")

# Quit the driver
driver.quit()
