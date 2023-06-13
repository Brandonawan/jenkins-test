# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# # Set up the Chrome WebDriver (you can use other browsers as well)
# # driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')
# driver = webdriver.Chrome('/usr/bin/chromedriver')


# # Navigate to the website you want to test
# driver.get('https://www.example.com')

# driver.quit()


names = ["brandon", "james"]
index_names = enumerate(names)
index_names_list = list(index_names)
print(index_names_list)

digits = [1.2, 3.5, 6.7, 10.3]
round_digits = map(round, digits)
print(list(round_digits))


