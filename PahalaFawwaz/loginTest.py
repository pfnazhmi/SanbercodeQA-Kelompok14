import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class TestLogin(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        
    def testLoginSucces(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login") # buka situs
        time.sleep(3)
        browser.find_element(By.NAME,"username").send_keys("Admin") # isi email
        time.sleep(1)
        browser.find_element(By.NAME,"password").send_keys("admin123") # isi password
        time.sleep(1)
        browser.find_element(By.XPATH,"//button[@type='submit']").click() # klik tombol sign in
        time.sleep(1)

        # validasi
        wait = WebDriverWait(browser, 10)
        wait.until(EC.url_contains(
            "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"))

        response_data = browser.current_url
        self.assertEqual(response_data, "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")

    def testLoginFailedWithNulllInput(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login") # buka situs
        time.sleep(3)
        browser.find_element(By.XPATH,"//button[@type='submit']").click() # klik tombol sign in
        time.sleep(1)

        # validasi
        response_data = browser.find_element(By.XPATH,"//div[contains(@class, 'oxd-input-group oxd-input-field-bottom-space') and span[contains(@class, 'oxd-text oxd-text--span oxd-input-field-error-message oxd-input-group__message')]]").text
        
        self.assertIn('Required', response_data)

    def testFailedWithWrongInput(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login") # buka situs
        time.sleep(3)
        browser.find_element(By.NAME,"username").send_keys("pal") # isi email
        time.sleep(1)
        browser.find_element(By.NAME,"password").send_keys("oeoe") # isi password
        time.sleep(1)
        browser.find_element(By.XPATH,"//button[@type='submit']").click() # klik tombol sign in
        time.sleep(1)
        # validasi
        response_data = browser.find_element(By.XPATH,"//div[contains(@role, 'alert')]").text
        
        self.assertIn('Invalid credentials', response_data)

    def tearDown(self): 
        self.browser.close() 

if __name__ == "_main_": 
    unittest.main()