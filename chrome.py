import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

# Set up Firefox options
firefox_options = Options()
firefox_options.headless = True  # Run Firefox in headless mode for better performance

# Set up Firefox WebDriver with the options
driver_service = FirefoxService(executable_path=GeckoDriverManager().install())
driver = webdriver.Firefox(service=driver_service, options=firefox_options)

# Set maximum wait time for explicit waits
wait = WebDriverWait(driver, 10)

base_url = "http://3.109.132.239:8080/" 
driver.get(f"{base_url}auth/login")

# Login
username_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='username']")))
username_input.send_keys("ccadmin")
password_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='password']")))
password_input.send_keys("admin#123")
login_button = wait.until(EC.element_to_be_clickable((By.ID, "submit")))
login_button.click()

# Wait for the dashboard page to load
dashboard_url = base_url + "dashboard"
wait.until(EC.url_to_be(dashboard_url))
assert driver.current_url == dashboard_url
print(f"✓ Login successful to: {dashboard_url}")

# Set the path to the chromedriver binar

# Find the wcagDb link in the sidebar and click it
wcagdb_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/wcagDB']")))
wcagdb_link.click()

# Wait for the wcagDb page to load
wcagdb_url = base_url+"wcagDB"
WebDriverWait(driver, 12).until(EC.url_to_be(wcagdb_url))
assert driver.current_url == wcagdb_url
print(f"✓ wcagDb dashboard: {wcagdb_url}")

# sleep for 5 seconds
time.sleep(3)

# Close the browser
driver.quit()
