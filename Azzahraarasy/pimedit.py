import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import baselogin

class TestUser(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_success_login(self): #TestCase1
        baseurl = "https://opensource-demo.orangehrmlive.com/"
        driver = self.browser 
        driver.get(baseurl)  
        time.sleep(3)
        baselogin.test_success_login(driver)
        driver.find_element(By.NAME, "username").send_keys("Admin")  
        time.sleep(30)
        driver.find_element(By.NAME, "password").send_keys("admin123")  
        time.sleep(30)
        driver.find_element(By.CLASS_NAME, "orangehrm-login-button").click()
        time.sleep(15)
        # PIM 
        driver.find_element(
        By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a',
        ).click()
        time.sleep(2)  
        driver.find_element(
        By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div',
        ).click()
        time.sleep(2) # icon pencil/edit
        driver.find_element(
        By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[1]/a'
        ).click()
        time.sleep(2) # personal details
        inputUsername = driver.find_element(
        By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/input',
        )
        inputUsername.send_keys(Keys.CONTROL + "a") 
        inputUsername.send_keys(Keys.DELETE)
        time.sleep(2)
        inputUsername.send_keys("azzahra")  # input first name
        time.sleep(2)
        inputUsername = driver.find_element(
        By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[1]/div/div/div[2]/div[2]/div[2]/input',
        )
        inputUsername.send_keys(Keys.CONTROL + "a") 
        inputUsername.send_keys(Keys.DELETE)
        time.sleep(2)
        inputUsername.send_keys("arasy")  # input middle name
        time.sleep(2)
        inputUsername = driver.find_element(
        By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[1]/div/div/div[2]/div[3]/div[2]/input',
        )
        inputUsername.send_keys(Keys.CONTROL + "a") 
        inputUsername.send_keys(Keys.DELETE)
        time.sleep(2)
        inputUsername.send_keys("bagjamawada")  # input last name
        time.sleep(3)
        inputUsername = driver.find_element(
        By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[2]/div/div/div[2]/input',
        )
        inputUsername.send_keys(Keys.CONTROL + "a") 
        inputUsername.send_keys(Keys.DELETE)
        time.sleep(2)
        inputUsername.send_keys("zahra")  # Input Nickname
        time.sleep(3)
        inputUsername = driver.find_element(
        By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[1]/div[2]/div/div[2]/input',
        )
        inputUsername.send_keys(Keys.CONTROL + "a") 
        inputUsername.send_keys("112233")  # ID
        driver.find_element(
        By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/label',
        ).click()  # Gender
        time.sleep(6)
        driver.find_element(
        By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button',
        ).click()  # Click Save
        time.sleep(6)
        driver.find_element(
        By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[10]/a',
        )  # Notif Success
        
        
    def test_success_login(self): #TestCase2
        baseurl = "https://opensource-demo.orangehrmlive.com/"
        driver = self.browser 
        driver.get(baseurl)  
        time.sleep(3)
        driver.find_element(By.NAME, "username").send_keys("Admin")  
        time.sleep(1)
        driver.find_element(By.NAME, "password").send_keys("admin123")  
        time.sleep(1)
        driver.find_element(By.CLASS_NAME, "orangehrm-login-button").click()
        time.sleep(30)
        # PIM 
        driver.find_element(
        By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a',
        ).click()
        time.sleep(2)  
        driver.find_element(
        By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div',
        ).click()
        time.sleep(2) # icon pencil/edit
        driver.find_element(
        By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[1]/a'
        ).click()
        time.sleep(2) # personal details
        inputUsername = driver.find_element(
        By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/input',
        )
        inputUsername.send_keys(Keys.CONTROL + "a") 
        inputUsername.send_keys(Keys.DELETE)
        time.sleep(2)
        inputUsername.send_keys("")  # input first name
        time.sleep(2)
        inputUsername = driver.find_element(
        By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[1]/div/div/div[2]/div[2]/div[2]/input',
        )
        inputUsername.send_keys(Keys.CONTROL + "a") 
        inputUsername.send_keys(Keys.DELETE)
        time.sleep(2)
        inputUsername.send_keys("")  # input middle name
        time.sleep(2)
        inputUsername = driver.find_element(
        By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[1]/div/div/div[2]/div[3]/div[2]/input',
        )
        inputUsername.send_keys(Keys.CONTROL + "a") 
        inputUsername.send_keys(Keys.DELETE)
        time.sleep(2)
        inputUsername.send_keys("")  # input last name
        time.sleep(3)
        inputUsername = driver.find_element(
        By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[2]/div/div/div[2]/input',
        )
        inputUsername.send_keys(Keys.CONTROL + "a") 
        inputUsername.send_keys(Keys.DELETE)
        time.sleep(2)
        inputUsername.send_keys("zahra")  # Input Nickname
        time.sleep(3)
        inputUsername = driver.find_element(
        By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[1]/div[2]/div/div[2]/input',
        )
        inputUsername.send_keys(Keys.CONTROL + "a") 
        inputUsername.send_keys("112233")  # ID
        driver.find_element(
        By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/label',
        ).click()  # Gender
        time.sleep(6)
        driver.find_element(
        By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button',
        ).click()  # Click Save
        time.sleep(6)

    
    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()