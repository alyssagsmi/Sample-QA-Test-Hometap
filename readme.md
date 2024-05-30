# Test Hometap Login - MS Edge

Hello, World!
This project is a Selenium automation script for logging into the Hometap dashboard using Microsoft Edge.

## Prerequisites
(Instructions given for Windows 11 Pro)

- Python 3.x
- Selenium
- Microsoft Edge WebDriver

## Setup Instructions

1. **Install Selenium:**
   ```sh
   pip install selenium

2. **Download Microsoft Edge Driver**
- Extract and place the driver executable in a known location (e.g., C:/path/to/driver).

3. **Set Environment Variables**
- Set the HOMETAP_PASSWORD environment variable with your Hometap password:
- Copy code
    ```sh
    setx HOMETAP_PASSWORD "your_password_here"

4.**Run the Script**
- Open a terminal and navigate to your project directory.
- Copy code and run the script
    ```sh
    python test_login_edge.py


**Notes:**
-Increase wait times during development and debugging as needed.

-Ensure the correct locators for the email and password fields.

-Suppress pop-ups in the Edge browser with appropriate options.