import unittest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service



class TestOrganization(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    #positive testing by deleting locations
    def test_success_admin_organization_delete_locations(self):
        # steps
        baseurl = "https://opensource-demo.orangehrmlive.com/"
        driver = self.browser  # buka web browser
        driver.get(baseurl)  # buka situs
        time.sleep(2)
        driver.find_element(By.NAME, "username").send_keys("Admin")  # username
        time.sleep(10)
        driver.maximize_window()
        driver.find_element(By.NAME, "password").send_keys("admin123")  # isi password
        time.sleep(10)
        driver.maximize_window()
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click() #login
        time.sleep(2)

       # stepsDeleteLocations
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a").click() #menu admin
        time.sleep(1) 
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[3]").click() #organization
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[3]/ul/li[2]/a").click() #locations
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]").click() #table of data
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div").click() #choose data
        time.sleep(1)
        driver.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']//div[@role='table']/div[2]/div[1]/div[@role='row']/div[7]/div/button[1]/i").click() #delete icon
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id='app']/div[3]/div/div/div").click() #popped up message to continue delete locations
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id='app']/div[3]/div/div/div/div[3]/button[2]").click() #confirmation click yes to delete locations
        time.sleep(1)
         #validasi
        expectedURL = "https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewLocations"
        actualURL = driver.current_url
        self.assertEquals(expectedURL, actualURL)
    

    def tearDown(self):
        self.browser.close()


if __name__ == "__main__":
    unittest.main()

