from datetime import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Function to sign in to Gmail
def sign_in_gmail(driver, email, password):
    # Open the Gmail login page
    driver.get("")

    try:
        # Find and fill in the email field
        email_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "identifierId")))
        email_field.send_keys(email)
        email_field.send_keys(Keys.RETURN)

        # Find and fill in the password field
        password_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "Passwd")))
        password_field.send_keys(password)
        password_field.send_keys(Keys.RETURN)

        print("Signed in to Gmail successfully.")
    except Exception as e:
        print(f"Failed to sign in to Gmail: {e}")

# Function to send an email with attachment
def send_email_with_attachment(driver, recipient, subject, message, file_path):
    try:
        # Click on the compose button
        compose_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='T-I T-I-KE L3']")))
        compose_button.click()

        # Fill in the recipient field
        recipient_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[aria-label='To recipients']")))
        recipient_field.send_keys(recipient_email)

        subject_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "subjectbox")))
        subject_field.send_keys(subject)

        message_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@role='textbox']")))
        message_field.send_keys(message)

        # Attach the file using JavaScript
        attach_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@command='Files']")))
        attach_button.click()
        time.sleep(2)  # Give some time for the attachment dialog to open

        # Execute JavaScript to set the file input value
        driver.execute_script(f"document.querySelector('input[type=file]').style.display='block';")
        file_input = driver.find_element_by_css_selector('input[type=file]')
        file_input.send_keys(file_path)

        # Click on the send button
        send_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Send']")))
        send_button.click()

        print("Email with attachment sent successfully.")
    except Exception as e:
        print(f"Failed to send email with attachment: {e}")

# Example usage
if __name__ == "__main__":
    try:
        # Specify the path to the ChromeDriver executable
        chromedriver_path = ChromeDriverManager().install()

        # Set Chrome options to disable automation detection
        chrome_options = Options()
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")

        # Initialize the WebDriver for Chrome with options and the specified path
        driver = webdriver.Chrome(executable_path=chromedriver_path, options=chrome_options)

        # Credentials for signing in
        email = ""
        password = ""

        # Recipient email address, subject, message, and file path
        recipient_email = ""
        subject = "Test Email with Attachment"
        message = "This is a test email sent with attachment using Selenium."
        file_path = "C:auto.xlsx"

        # Sign in to Gmail
        sign_in_gmail(driver, email, password)

        # Send email with attachment
        send_email_with_attachment(driver, recipient_email, subject, message, file_path)

        # Give some time for the email to be sent
        time.sleep(5)

    except Exception as e:
        print(f"An error occurred: {e}")
