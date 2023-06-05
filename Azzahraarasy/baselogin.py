import unittest
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By



def test_success_login(driver): # TestCase1
    baseUrl = "https://opensource-demo.orangehrmlive.com/"
    driver.get(baseUrl) 
    time.sleep(3)
    driver.find_element(By.NAME, "username").send_keys("Admin")
    driver.find_element(By.NAME, "password").send_keys("admin123")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

# Data Automation 
# First Name: Azzahra
# Middle Name: Arasy
# Last Name: Bagjamawada
# ID: 112233
# Gender: Female