import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
from tabulate import tabulate
from termcolor import colored


# Set headless mode options
options = Options()
options.add_argument('-headless')

# Set up the Firefox driver service
service = Service(GeckoDriverManager().install())

# Set up the Firefox driver
driver = webdriver.Firefox(service=service, options=options)

base_url = "http://3.109.132.239:8080/"

driver.maximize_window()

results = {}

def login():
    # Navigate to the app login page
    driver.get(base_url+"auth/login")

    # Find the username input element and enter the username
    username_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='username']"))).send_keys("ccadmin")
    
    password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='password']"))).send_keys("admin#123")
    
    login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "submit"))).click()
    
    # Wait for the dashboard page to load
    dashboard_url = base_url+"dashboard"
    WebDriverWait(driver, 10).until(EC.url_to_be(dashboard_url))
    assert driver.current_url == dashboard_url
    print(colored("✓", "green"),f"Login successful to: {dashboard_url}")
    
    results['login'] = True
    
# def wcagdb():
#     login()
#     # Find the wcagDb link in the sidebar and click it
#     wcagdb_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/wcagDB']")))
#     wcagdb_link.click()

#     # Wait for the wcagDb page to load
#     wcagdb_url = base_url+"wcagDB"
#     WebDriverWait(driver, 12).until(EC.url_to_be(wcagdb_url))
#     assert driver.current_url == wcagdb_url
#     print(f"✓ wcagDb dashboard: {wcagdb_url}") 
    
#     results['wcagdb'] = True


def wcag_version_filters():
    login()
    # Find the wcagDb link in the sidebar and click it
    wcagdb_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/aiichecklist']")))
    wcagdb_link.click()

    # Wait for the wcagDb page to load
    aii_url = base_url + "aiichecklist"
    WebDriverWait(driver, 12).until(EC.url_to_be(aii_url))
    assert driver.current_url == aii_url
    # print(f"✓ Accessibility checklist dashboard: {aii_url}")
    print(colored("✓", "green"), f"Accessibility checklist dashboard: {aii_url}")

    time.sleep(3)

    # Find the "principleSelect" element and click it to select all principles
    principle_select_all = driver.find_element(By.ID, "principleSelect")
    principle_select_all.click()
    time.sleep(2)
    print(colored("✓", "green"), f"All principles selected")

    # Find the "guidelineSelect" element and click it to select all guidelines
    guideline_select_all = driver.find_element(By.ID, "guidelineSelect")
    guideline_select_all.click()
    time.sleep(2)
    print(colored("✓", "green"), f"All guidelines selected")
    
    results['wcag_version_filters'] = True
    
wcag_version_filters()


total_functions = 2   #Update the total number of functions being tested
passed_functions = sum(results.values())
test_coverage = (passed_functions / total_functions) * 100 if total_functions > 0 else 0

# Generate the report summary table
summary_data = []
for func, result in results.items():
    status = "Passed" if result else "Failed"
    summary_data.append([func, status])
summary_data.append(["Test Coverage", f"{test_coverage}%"])
# summary_data.append(["Test Coverage", colored(f'{test_coverage}', "green")%'])

# Print the report summary table
print(colored(f"---------- Test Report Summary ------------", "yellow"))
table_headers = ["Test Case", "Status"]
table = tabulate(summary_data, headers=table_headers, tablefmt="grid")
print(colored(f"{table}", "green"))

driver.quit()
print(colored("✓", "green"), f"Test completed successfully")
