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
    print(f"✓ Login successful to: {dashboard_url}")
    
    results['login'] = True
    
def wcagdb():
    login()
    # Find the wcagDb link in the sidebar and click it
    wcagdb_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/wcagDB']")))
    wcagdb_link.click()

    # Wait for the wcagDb page to load
    wcagdb_url = base_url+"wcagDB"
    WebDriverWait(driver, 12).until(EC.url_to_be(wcagdb_url))
    assert driver.current_url == wcagdb_url
    print(f"✓ wcagDb dashboard: {wcagdb_url}") 
    
    results['wcagdb'] = True
    
wcagdb()

# total_functions = 2   Update the total number of functions being tested
# passed_functions = sum(results.values())
# test_coverage = (passed_functions / total_functions) * 100 if total_functions > 0 else 0

# # Generate the report summary table
# summary_data = []
# for func, result in results.items():
#     status = "Passed" if result else "Failed"
#     summary_data.append([func, status])
# summary_data.append(["Test Coverage", f"{test_coverage}%"])

# # Print the report summary table
# print("---------- Test Report Summary ----------")
# table_headers = ["Test Case", "Status"]
# table = tabulate(summary_data, headers=table_headers, tablefmt="grid")
# print(table)

# driver.quit()

# Perform the tests
results = {}
total_functions = 2
passed_functions = sum(results.values())
test_coverage = (passed_functions / total_functions) * 100 if total_functions > 0 else 0

summary_data = []
for func, result in results.items():
    status = "Passed" if result else "Failed"
    summary_data.append([func, status])
summary_data.append(["Test Coverage", f"{test_coverage:.2f}%"])

# Define the HTML template for the report
html_template = """
<!DOCTYPE html>
<html>
<head>
    <style>
        table {{
            border-collapse: collapse;
            width: 100%;
        }}

        th, td {{
            padding: 8px;
            text-align: left;
            border-bottom: 1px solid #ddd;
        }}

        th {{
            background-color: #f2f2f2;
        }}

        .passed {{
            color: green;
        }}

        .failed {{
            color: red;
        }}

        .coverage {{
            font-weight: bold;
        }}
    </style>
</head>
<body>
    <h2>Test Report Summary</h2>
    <table>
        <tr>
            <th>Test Case</th>
            <th>Status</th>
        </tr>
        {table_data}
    </table>
</body>
</html>
"""

# Generate the HTML table rows for the report summary
table_rows = ""
for func, result in summary_data:
    status_class = "passed" if result == "Passed" else "failed"
    table_row = f"<tr><td>{func}</td><td class='{status_class}'>{result}</td></tr>"
    table_rows += table_row

# Generate the HTML report
html_report = html_template.format(table_data=table_rows)

# Save the HTML report to a file
report_file_path = "test_report.html"
with open(report_file_path, "w") as report_file:
    report_file.write(html_report)

# Print a message with the file path
print("Test report saved to:", report_file_path)