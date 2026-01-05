import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

def login_task():
    # 1. Setup Headless Chrome for Server
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    # 2. Specify paths to the files you uploaded
    # These must match the folders you dragged into GitHub
    chrome_bin = os.path.join(os.getcwd(), "chrome-linux/chrome")
    driver_bin = os.path.join(os.getcwd(), "chromedriver")
    
    options.binary_location = chrome_bin
    service = Service(executable_path=driver_bin)
    driver = webdriver.Chrome(service=service, options=options)

    try:
        print("Opening Portal...")
        driver.get("http://125.22.246.228:1000/")
        time.sleep(3) # Wait for page to load

        # 3. Enter Credentials
        # Note: I used common 'name' tags. If these fail, we will check the 'Inspect' tags.
        print("Entering credentials...")
        driver.find_element(By.NAME, "username").send_keys("kuppu")
        driver.find_element(By.NAME, "password").send_keys("Welcome@123!")
        
        # 4. Click Login (usually an input with type 'submit' or id 'login')
        driver.find_element(By.XPATH, "//input[@type='submit']").click()
        
        print("Login complete. Current Page Title:", driver.title)
        time.sleep(5)
        
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()
        print("Browser closed.")

if __name__ == "__main__":
    login_task()
