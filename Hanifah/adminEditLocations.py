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

    def test_success_admin_organization_edit_locations(self):
        # steps
        baseurl = "https://opensource-demo.orangehrmlive.com/"
        driver = self.browser  # buka web browser
        driver.get(baseurl)  # buka situs
        time.sleep(1)
        driver.find_element(By.NAME, "username").send_keys("Admin")  # username
        driver.find_element(By.NAME, "password").send_keys("admin123")  # isi password
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click() #login
        time.sleep(5)
        driver.find_element(By.XPATH, "//div[@id='app']//aside[@class='oxd-sidepanel']/nav[@role='navigation']//ul[@class='oxd-main-menu']//a[@href='/web/index.php/admin/viewAdminModule']").click() #menu admin
        time.sleep(3)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[3]").click() #organization
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[3]/ul/li[2]/a").click() #locations
        time.sleep(3)
        driver.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']//div[@role='table']/div[2]/div[1]/div[@role='row']/div[7]/div/button[2]/i").click() # click on pencil button for editLocations
        time.sleep(5)

        #Step EditLocations
        inputEditLocations = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div/div/div[2]/input").send_keys("Simpang") #input name Simpang
        inputCountry = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[4]/div/div[2]/div/div/div[1]").click() #click dropdown select country
        time.sleep(1)
        inputCountry = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[4]/div/div[2]/div/div/div[1]").click() #click country select Singapore
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[3]/button[2]").click() #click save
        time.sleep(1)
    
    def test_failed_admin_organization_edit_locations(self):
        # steps
        baseurl = "https://opensource-demo.orangehrmlive.com/"
        driver = self.browser  # buka web browser
        driver.get(baseurl)  # buka situs
        time.sleep(1)
        driver.find_element(By.NAME, "username").send_keys("Admin")  # username
        driver.find_element(By.NAME, "password").send_keys("admin123")  # isi password
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click() #login
        time.sleep(5)
        driver.find_element(By.XPATH, "//div[@id='app']//aside[@class='oxd-sidepanel']/nav[@role='navigation']//ul[@class='oxd-main-menu']//a[@href='/web/index.php/admin/viewAdminModule']").click() #menu admin
        time.sleep(3)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[3]").click() #organization
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[3]/ul/li[2]/a").click() #locations
        time.sleep(3)
        driver.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']//div[@role='table']/div[2]/div[1]/div[@role='row']/div[7]/div/button[2]/i").click() # click on pencil button for editLocations
        time.sleep(5)

        #Step EditLocations
        inputEditLocations = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div/div/div[2]/input").send_keys("Simpang") #input name Simpang
        inputCountry = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[4]/div/div[2]/div/div/div[1]").click() #click dropdown select country (not select any country)
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[3]/button[2]").click() #click save
        time.sleep(1)
        #validasi
        expectedURL = "https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewLocations"
        actualURL = driver.current_url
        self.assertEquals(expectedURL, actualURL)
    

    

    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()