import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType

def login_task():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    # This automatically finds and downloads the right driver for the server
    driver_path = ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()
    service = Service(driver_path)
    
    driver = webdriver.Chrome(service=service, options=options)

    try:
        print("Navigating to Portal...")
        driver.get("http://125.22.246.228:1000/")
        
        # Entering your credentials
        driver.find_element("name", "username").send_keys("kuppu")
        driver.find_element("name", "password").send_keys("Welcome@123!")
        driver.find_element("xpath", "//input[@type='submit']").click()
        
        print("Success! Current Title:", driver.title)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    login_task()

       
