import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

web = "https://x.com/"

# Set up Chrome options
chrome_options = Options()
#chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# Initialize WebDriver
driver = webdriver.Chrome(options=chrome_options)
driver.get(web)
driver.maximize_window()

# wait for the page to load
wait = WebDriverWait(driver, 20)

try:
    # Wait for the sign-in button to be clickable
    sign_in_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@data-testid="loginButton"]')))
    sign_in_button.click()

    # Wait for the username field to be visible
    username = wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@autocomplete="username"]')))
    username.send_keys("kupcbart@gmail.com")  # Write Email Here

    # Click the "Next" button
    next_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//div/button/div/span/span[text()="Next"]')))
    next_button.click()

    # Wait for the password field to be visible
    password = wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@autocomplete="current-password"]')))
    password.send_keys("Coronavirus11")  # Write Password Here

    # Click the "Log in" button
    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//div/button/div/span/span[text()="Log in"]')))
    login_button.click()

finally:
    # closing driver
    time.sleep(5)  # wait for a few seconds to observe the result if not headless
    driver.quit()
