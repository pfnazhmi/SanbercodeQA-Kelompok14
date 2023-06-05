import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys


class TestUser(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_success_login(self): #TestCase1
        baseurl = "https://opensource-demo.orangehrmlive.com/"
        driver = self.browser 
        driver.get(baseurl)  
        time.sleep(3)
        driver.find_element(By.NAME, "username").send_keys("Admin")  
        time.sleep(1)
        driver.find_element(By.NAME, "password").send_keys("admin123")  
        time.sleep(1)
        driver.find_element(By.CLASS_NAME, "orangehrm-login-button").click()
        time.sleep(5)
        # PIM 
        driver.find_element(
        By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a").click()
        time.sleep(2) 
        driver.find_element(
        By.XPATH, "//div[@id='app']/div[@class='oxd-layout']//div[@role='table']/div[2]/div[1]/div[@role='row']/div[9]/div/button[1]/i").click()
        time.sleep(2) # icon trash
        driver.find_element(
        By.XPATH, '//*[@id="app"]/div[3]/div/div/div').click()
        time.sleep(2) # delete
        driver.find_element(
        By.XPATH, '//*[@id="app"]/div[3]/div/div/div/div[3]/button[2]').click()
        time.sleep(5) # success delete
        
def tearDown(self):
    self.browser.close()

if __name__ == "__main__":
    unittest.main()