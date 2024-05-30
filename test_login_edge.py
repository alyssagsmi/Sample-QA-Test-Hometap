import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Load my Hometap password from environment variables
password_value = os.getenv('HOMETAP_PASSWORD')

# Ensure the password is not None
if password_value is None:
    raise ValueError("Password environment variable 'HOMETAP_PASSWORD' is not set")

# Specify the path to the MSEdge WebDriver
driver_path = 'C:/Users/alyss/Downloads/msedgedriver/msedgedriver.exe'

# Set MSEdge WebDriver options
edge_options = webdriver.EdgeOptions()
edge_options.use_chromium = True

# Suppress the 'new user profile' popup and other distractions
edge_options.add_argument('--no-first-run')
edge_options.add_argument('--no-default-browser-check')
edge_options.add_argument('--disable-popup-blocking')
edge_options.add_argument('--disable-infobars')
edge_options.add_argument('--disable-extensions')

# Additional preferences to suppress popups
prefs = {
    "profile.default_content_setting_values.notifications": 2,  # Disable notifications
    "profile.default_content_setting_values.popups": 2,         # Disable popups
    "profile.default_content_setting_values.automatic_downloads": 1  # Allow automatic downloads
}
edge_options.add_experimental_option("prefs", prefs)

# Initialize the Edge driver with options
driver = webdriver.Edge(options=edge_options)

try:
    # Open the Hometap portal auth login page
    driver.get("https://portal.hometap.com/auth/login/")
    print("Opened the Hometap auth login page")

    # Wait for the email address field to be present
    email = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "id_username"))
    )
    print("Email field is present")
    email.send_keys("alyssagsmi@gmail.com")
    print("Entered email address")

    # Click the "Continue with email" button
    continue_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "next-btn"))
    )
    print("Continue button is clickable")
    continue_button.click()
    print("Clicked Continue button")

    # Increase wait time to allow for manual observation during development and debugging
    time.sleep(2)  # NOTE: Remove this line when fully automated!

    # Wait for the password field to be visible and enabled
    password = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "id_password"))
    )
    password = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "id_password"))
    )
    print("Password field is visible and enabled")
    password.send_keys(password_value)
    print("Entered password")

    # Click the "Login to your account" button
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "login-btn"))
    )
    print("Login button is clickable")
    login_button.click()
    print("Clicked Login button")

    # Wait for the dashboard to load
    WebDriverWait(driver, 20).until(
        EC.url_contains("dashboard")
    )
    print("Dashboard page loaded")

    # Verify login was successful by checking the URL or a dashboard element
    assert "dashboard" in driver.current_url or WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "button.htco-IconButton.Hamburger"))
    )

    print("Login test passed!")
except Exception as e:
    print("Login test failed:", e)

finally:
    # Close the browser
    WebDriverWait(driver, 10)
    driver.quit()
