import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class TestAdd(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        
    def testUseSucces(self): 
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

        wait = WebDriverWait(browser, 10)
        wait.until(EC.url_contains(
            "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"))
        time.sleep(2)

        browser.find_element(By.XPATH,"//*[@href='/web/index.php/admin/viewAdminModule']").click() #klik admin
        time.sleep(1)

        browser.find_element(By.XPATH,"//button[@class='oxd-button oxd-button--medium oxd-button--secondary']").click()# klik button add
        time.sleep(2)

        browser.find_element(By.XPATH,"//div[contains(@class, 'oxd-select-text oxd-select-text--active')]").click()# user role
        time.sleep(1)

        browser.find_element(By.XPATH,f"//div[.//span[contains(text(), 'Admin')]]").click()# klik option admin
        time.sleep(1)

        elements = browser.find_elements(By.XPATH, f"//div[@class='oxd-select-text oxd-select-text--active']")# isi status
        sec_element = elements[1]
        sec_element.click()
        time.sleep(1)

        browser.find_element(By.XPATH,"//div[span[text()='Enabled']]").click()# klik option enabled
        time.sleep(1)

        browser.find_element(By.XPATH,"//input[contains(@placeholder, 'Type for hints...')] ").send_keys("Ganesh") # input employee
        time.sleep(4)

        browser.find_element(By.XPATH,"//div[contains(@class, 'oxd-autocomplete-option')]").click()# klik
        time.sleep(1)

        browser.find_element(By.XPATH,"//input[contains(@class, 'oxd-input oxd-input--active') and not(@placeholder)] ").send_keys("samudra") # isi username
        time.sleep(3)

        browser.find_element(By.XPATH,"//input[@class ='oxd-input oxd-input--active' and @type ='password']").send_keys("Ayang!123") # isi password
        time.sleep(2)

        elementsPass = browser.find_element(By.XPATH,"//input[@class,'oxd-input oxd-input--active' and @type, 'password']")# isi status
        elementsPass.send_keys("Ayang!123")
        time.sleep(2)

        browser.find_element(By.XPATH,"//button[@class='oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space']").click()# klik button add
        time.sleep(2)

    def tearDown(self): 
        self.browser.close() 

if __name__ == "_main_": 
    unittest.main()