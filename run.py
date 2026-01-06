import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def run_robot():
    chrome_options = Options()
    chrome_options.add_argument("--headless=new") 
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), 
        options=chrome_options
    )

    try:
        print("--- Starting Automation ---")
        driver.get("http://125.22.246.228:1000/")
        
        # Login
        driver.find_element(By.NAME, "username").send_keys("kuppu")
        driver.find_element(By.NAME, "password").send_keys("Welcome@123!")
        
        login_button = driver.find_element(By.ID, "login-button") 
        login_button.click()
        
        time.sleep(7) 

        # FINAL SOLUTION FOR PUBLIC LINK
        # We use the absolute path to the public 'wwwroot' folder
        public_path = "C:\\home\\site\\wwwroot\\login_proof.png"
        
        driver.save_screenshot(public_path)
        print(f"SUCCESS: Image saved to {public_path}")

    except Exception as e:
        print(f"ERROR: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    run_robot()
       
