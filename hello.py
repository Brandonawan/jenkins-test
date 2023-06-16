import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Set headless mode options
options = Options()
options.add_argument('-headless')

# Set up the Firefox driver service
service = Service(GeckoDriverManager().install())

# Set up the Firefox driver
driver = webdriver.Firefox(service=service, options=options)

base_url = "http://3.109.132.239:8080/"

# Maximize the browser window
driver.maximize_window()

def login():
    # Navigate to the app login page
    driver.get(base_url+"auth/login")

    # Find the username input element and enter the username
    username_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='username']"))).send_keys("ccadmin")

    # Find the password input element and enter the password
    password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='password']"))).send_keys("admin#123")

    # Find the login button and click it
    login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "submit"))).click()
    
    # Wait for the dashboard page to load
    dashboard_url = base_url+"dashboard"
    WebDriverWait(driver, 10).until(EC.url_to_be(dashboard_url))
    assert driver.current_url == dashboard_url
    print(f"✓ Login successful to: {dashboard_url}")

def dependency_tree():
    login()
    
    # Find the dependency tree link in the sidebar and click it
    dependency_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/dependency-tree']")))
    dependency_link.click()

    # Wait for the dependency tree page to load
    dependency_url = base_url + "dependency-tree"
    WebDriverWait(driver, 12).until(EC.url_to_be(dependency_url))
    assert driver.current_url == dependency_url
    print(f"✓ Dependency dashboard: {dependency_url}")

    # Find the file upload button element
    upload_button = driver.find_element(By.CSS_SELECTOR, "button[data-bs-target='#uploadModal']")
    upload_button.click()

    import os

    # Get the absolute path of the current script
    script_path = os.path.abspath(__file__)

    # Get the directory containing the script
    script_directory = os.path.dirname(script_path)

    # Specify the relative path to the file
    relative_path = 'csv/airtable-may-17.csv'

    # Combine the script directory and the relative path to get the absolute file path
    file_path = os.path.join(script_directory, relative_path)

    # Normalize the file path to handle any path separators
    file_path = os.path.normpath(file_path)

    # Print the absolute file path
    print(file_path)
    
    # Provide the file path to be uploaded
    # file_path = "csv/airtable-may-17.csv"

    # Wait for the file input element to be visible within the modal
    file_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#uploadModal input[type='file']"))
    )

    # Set the file path in the file input element
    file_input.send_keys(file_path)

    # Locate and interact with the submit button or form within the modal
    submit_button = driver.find_element(By.ID, "uploadbutton")
    submit_button.click()

    table = driver.find_element(By.ID, "datatables")
    rows = table.find_element(By.TAG_NAME, "tbody").find_elements(By.TAG_NAME, "tr")
    first_row = rows[0]

    link = first_row.find_element(By.TAG_NAME, "a")
    link.click()

    # Print "successful"
    print("successful")

    # Wait for the modal to appear
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.modal.fade.show')))

    # Find the close button using CSS selector
    close_button = driver.find_element(By.CSS_SELECTOR, 'div.modal.fade.show button.btn-close')

    # Click the close button
    close_button.click()

    # Print "Modal closed successfully"
    print("Modal closed successfully")

    # Find the delete button within the first row
    delete_button = first_row.find_element(By.CSS_SELECTOR, "button.btn.btn-sm.btn-danger")

    # Click the delete button
    delete_button.click()

    # Wait for the alert to be present
    wait = WebDriverWait(driver, 10)
    try:
        alert = wait.until(EC.alert_is_present())
        # Switch to the alert
        alert = driver.switch_to.alert
        # Accept the alert (click OK)
        alert.accept()
        print("Clicked OK on the alert")
    except TimeoutException:
        print("Alert did not appear within the specified time")

# Run the function
dependency_tree()

# Close the browser
driver.quit()