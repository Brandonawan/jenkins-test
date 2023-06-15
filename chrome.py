import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

base_url = "http://3.109.132.239:8080/"
# Set headless mode options
options = Options()
options.add_argument('-headless')

# Set up the Firefox driver service
service = Service(GeckoDriverManager().install())

# Set up the Firefox driver
driver = webdriver.Firefox(service=service, options=options)

# Maximize the browser window
driver.maximize_window()

# Navigate to the app login page
driver.get(base_url+"auth/login")

# Find the username input element and enter the username
username_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='username']"))).send_keys("ccadmin")

# Find the password input element and enter the password
password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='password']"))).send_keys("admin#123")

# Find the login button and click it
login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "submit")))
login_button.click()

# Wait for the dashboard page to load
dashboard_url = base_url+"dashboard"
WebDriverWait(driver, 10).until(EC.url_to_be(dashboard_url))
assert driver.current_url == dashboard_url
print(f"✓ Login successful to: {dashboard_url}")

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
