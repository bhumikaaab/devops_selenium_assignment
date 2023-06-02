from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up Selenium webdriver
driver = webdriver.Chrome('C:/Users/I527383/Downloads/chromedriver_win32/chromedriver')

# Navigate to the website
driver.get("https://demowebshop.tricentis.com")

# Find and click the Register link
register_link = driver.find_element(By.LINK_TEXT, "Register")
register_link.click()

# Fill in the registration form
wait = WebDriverWait(driver, 10)
first_name_field = wait.until(EC.presence_of_element_located((By.ID, "FirstName")))
first_name_field.send_keys("Suzoo")

last_name_field = driver.find_element(By.ID, "LastName")
last_name_field.send_keys("Kim")

email_field = driver.find_element(By.ID, "Email")
email_field.send_keys("kimsuzoo678@example.com")

password_field = driver.find_element(By.ID, "Password")
password_field.send_keys("password678")

confirm_password_field = driver.find_element(By.ID, "ConfirmPassword")
confirm_password_field.send_keys("password678")

register_button = driver.find_element(By.CSS_SELECTOR, '[type="submit"][value="Register"]')
register_button.click()

time.sleep(5)

# Find the search input field
search_field = driver.find_element(By.ID, "small-searchterms")

# Clear the default value (if needed)
search_field.clear()

# Enter the search keyword
search_field.send_keys("laptop")

# Submit the search form
search_button = driver.find_element(By.CSS_SELECTOR, ".search-box-button")
search_button.click()

# Wait for the search results page to load
wait = WebDriverWait(driver, 10)
search_results = wait.until(EC.visibility_of_element_located((By.ID, "search-results")))

# Close the browser
driver.quit()
