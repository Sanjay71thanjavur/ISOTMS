import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def run_robot():
    # 1. SETUP CHROME FOR AZURE (No Monitor Mode)
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")  # Critical for Cloud servers
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")

    # Initialize Driver
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), 
        options=chrome_options
    )

    try:
        print("--- [Robot Start] Navigating to Site ---")
        
        # 2. TARGET WEBSITE
        driver.get("http://125.22.246.228:1000/")
        print(f"Connected to: {driver.title}")

        # 3. LOGIN SEQUENCE
        # Finding elements by NAME and ID based on your previous tasks
        driver.find_element(By.NAME, "username").send_keys("kuppu")
        driver.find_element(By.NAME, "password").send_keys("Welcome@123!")
        
        # Click the Login Button
        # Change By.ID to By.NAME or By.XPATH if your site uses a different tag
        login_button = driver.find_element(By.ID, "login-button") 
        login_button.click()
        
        print("Login clicked. Waiting for page to load...")
        time.sleep(7)  # Giving the server time to process the login

        # 4. CREATE THE PUBLIC LINK (Screenshot)
        # We go up 4 levels to reach the 'wwwroot' folder
        # From: site/wwwroot/App_Data/jobs/triggered/login-worker/
        # To:   site/wwwroot/
        public_filename = "login_proof.png"
        public_path = os.path.join("../../../../", public_filename)
        
        driver.save_screenshot(public_path)
        print(f"SUCCESS: Screenshot saved to {public_filename}")
        print(f"Public Link: https://isotmsautomation.azurewebsites.net/{public_filename}")

    except Exception as e:
        print(f"ERROR: Robot failed because: {e}")
        # Save error screenshot to help you debug
        driver.save_screenshot("../../../../error_log.png")
        
    finally:
        driver.quit()
        print("--- [Robot Finished] ---")

if __name__ == "__main__":
    run_robot()
       
