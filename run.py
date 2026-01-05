import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType
from selenium.webdriver.common.by import By

def quick_session():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    driver_path = ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service, options=options)

    try:
        driver.get("http://125.22.246.228:1000/")
        
        # 1. Auto Login
        driver.find_element(By.NAME, "username").send_keys("kuppu")
        driver.find_element(By.NAME, "password").send_keys("Welcome@123!")
        driver.find_element(By.XPATH, "//button[contains(., 'Sign In')]").click()
        print("Logged In")
        
        time.sleep(2) # Short pause to let the page load

        # 2. Auto Logout
        # Using a very common XPATH to find the logout link/button
        driver.find_element(By.XPATH, "//a[contains(text(), 'Logout') or contains(text(), 'Sign Out')]").click()
        print("Logged Out Successfully")
        
    except Exception as e:
        print(f"Error: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    quick_session()
       
