import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import baselogin

class TestPIMList(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_TC09(self):
        baseUrl = "https://opensource-demo.orangehrmlive.com/"
        driver = self.browser 
        driver.get(baseUrl) 
        baselogin.test_success_login(driver)
        currentUrl = driver.current_url
        self.assertIn (currentUrl, baseUrl + "web/index.php/dashboard/index")
        time.sleep(3)
        driver.find_element(
            By.XPATH,
            "//div[@id='app']//aside[@class='oxd-sidepanel']/nav[@role='navigation']//ul[@class='oxd-main-menu']//a[@href='/web/index.php/pim/viewPimModule']/span[.='PIM']",
        ).click()
        time.sleep(3)
        driver.find_element(
            By.XPATH,
            "//input[@placeholder='Type for hints...']",).send_keys("ameera")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(3)
        valid_message = driver.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']//div[@role='table']/div[2]//div[@role='row']/div[3]/div[.='Ameera Qince']").text
        self.assertIn("Ameera Qince", valid_message)
        time.sleep(3)
    
    def test_TC10(self):
        baseUrl = "https://opensource-demo.orangehrmlive.com/"
        driver = self.browser 
        driver.get(baseUrl) 
        baselogin.test_success_login(driver)
        currentUrl = driver.current_url
        self.assertIn (currentUrl, baseUrl + "web/index.php/dashboard/index")
        time.sleep(3)
        driver.find_element(
            By.XPATH,
            "//div[@id='app']//aside[@class='oxd-sidepanel']/nav[@role='navigation']//ul[@class='oxd-main-menu']//a[@href='/web/index.php/pim/viewPimModule']/span[.='PIM']",
        ).click()
        time.sleep(3)
        driver.find_element(
            By.XPATH,
            "//input[@placeholder='Type for hints...']",).send_keys("bukanameera")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(3)
        error_message = driver.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/span[@class='oxd-text oxd-text--span']").text
        self.assertIn("No Records Found", error_message)
        time.sleep(3)

    def test_TC11(self):
        baseUrl = "https://opensource-demo.orangehrmlive.com/"
        driver = self.browser 
        driver.get(baseUrl) 
        baselogin.test_success_login(driver)
        currentUrl = driver.current_url
        self.assertIn (currentUrl, baseUrl + "web/index.php/dashboard/index")
        time.sleep(3)
        driver.find_element(
            By.XPATH,
            "//div[@id='app']//aside[@class='oxd-sidepanel']/nav[@role='navigation']//ul[@class='oxd-main-menu']//a[@href='/web/index.php/pim/viewPimModule']/span[.='PIM']",
        ).click()
        time.sleep(3)
        driver.find_element(
            By.XPATH,
            "//input[@placeholder='Type for hints...']",).send_keys("")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(3)
        valid_message = driver.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']//div[@role='table']/div[1]/div[@role='row']/div[9]").text
        self.assertIn("Actions", valid_message)
        time.sleep(3)

    def test_TC12(self):
        baseUrl = "https://opensource-demo.orangehrmlive.com/"
        driver = self.browser 
        driver.get(baseUrl) 
        baselogin.test_success_login(driver)
        currentUrl = driver.current_url
        self.assertIn (currentUrl, baseUrl + "web/index.php/dashboard/index")
        time.sleep(3)
        driver.find_element(
            By.XPATH,
            "//div[@id='app']//aside[@class='oxd-sidepanel']/nav[@role='navigation']//ul[@class='oxd-main-menu']//a[@href='/web/index.php/pim/viewPimModule']/span[.='PIM']",
        ).click()
        time.sleep(3)
        driver.find_element(
            By.XPATH,
            "//div[@id='app']//div[@class='oxd-table-filter']/div[@class='oxd-table-filter-area']/form[@class='oxd-form']/div[@class='oxd-form-row']/div/div[2]//input",
            ).send_keys("0234")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(3)
        valid_message = driver.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']//div[@role='table']/div[2]//div[@role='row']/div[2]/div[.='0234']").text
        self.assertIn("0234", valid_message)
        time.sleep(3)

    def test_TC13(self):
        baseUrl = "https://opensource-demo.orangehrmlive.com/"
        driver = self.browser 
        driver.get(baseUrl) 
        baselogin.test_success_login(driver)
        currentUrl = driver.current_url
        self.assertIn (currentUrl, baseUrl + "web/index.php/dashboard/index")
        time.sleep(3)
        driver.find_element(
            By.XPATH,
            "//div[@id='app']//aside[@class='oxd-sidepanel']/nav[@role='navigation']//ul[@class='oxd-main-menu']//a[@href='/web/index.php/pim/viewPimModule']/span[.='PIM']",
        ).click()
        time.sleep(3)
        driver.find_element(
            By.XPATH,
            "//div[@id='app']//div[@class='oxd-table-filter']/div[@class='oxd-table-filter-area']/form[@class='oxd-form']/div[@class='oxd-form-row']/div/div[2]//input",
            ).send_keys("000")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(3)
        error_message = driver.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/span[@class='oxd-text oxd-text--span']").text
        self.assertIn("No Records Found", error_message)
        time.sleep(3)

    def test_TC14(self):
        baseUrl = "https://opensource-demo.orangehrmlive.com/"
        driver = self.browser 
        driver.get(baseUrl) 
        baselogin.test_success_login(driver)
        currentUrl = driver.current_url
        self.assertIn (currentUrl, baseUrl + "web/index.php/dashboard/index")
        time.sleep(3)
        driver.find_element(
            By.XPATH,
            "//div[@id='app']//aside[@class='oxd-sidepanel']/nav[@role='navigation']//ul[@class='oxd-main-menu']//a[@href='/web/index.php/pim/viewPimModule']/span[.='PIM']",
        ).click()
        time.sleep(3)
        driver.find_element(
            By.XPATH,
            "//div[@id='app']//div[@class='oxd-table-filter']/div[@class='oxd-table-filter-area']/form[@class='oxd-form']/div[@class='oxd-form-row']/div/div[3]/div//div[@class='oxd-select-text-input']",
            ).click()
        time.sleep(3)
        driver.find_element(
            By.XPATH,
            "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[3]/div/div[2]/div/div[2]/div[5]/span",
            ).click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(3)
        valid_message = driver.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']//div[@role='table']/div[2]//div[@role='row']/div[6]/div[.='Full-Time Permanent']").text
        self.assertIn("Full-Time Permanent", valid_message)
        time.sleep(3)
    
    def onlytest_TC15(self):
        baseUrl = "https://opensource-demo.orangehrmlive.com/"
        driver = self.browser 
        driver.get(baseUrl) 
        baselogin.test_success_login(driver)
        currentUrl = driver.current_url
        self.assertIn (currentUrl, baseUrl + "web/index.php/dashboard/index")
        time.sleep(3)
        driver.find_element(
            By.XPATH,
            "//div[@id='app']//aside[@class='oxd-sidepanel']/nav[@role='navigation']//ul[@class='oxd-main-menu']//a[@href='/web/index.php/pim/viewPimModule']/span[.='PIM']",
        ).click()
        time.sleep(3)
        driver.find_element(
            By.XPATH,
            "//div[@id='app']//div[@class='oxd-table-filter']/div[@class='oxd-table-filter-area']/form[@class='oxd-form']/div[@class='oxd-form-row']/div/div[4]/div//div[@class='oxd-select-text-input']",
            ).click()
        time.sleep(3)
        driver.find_element(
            By.XPATH,
            "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[4]/div/div[2]/div/div[2]/div[2]/span",
            ).click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(3)
        valid_message = driver.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']//div[@role='table']/div[2]/div[1]/div[@role='row']/div[7]/div[.='Human Resources']").text
        self.assertIn("Human Resources", valid_message)
        time.sleep(3)

    def test_TC16(self):
        baseUrl = "https://opensource-demo.orangehrmlive.com/"
        driver = self.browser 
        driver.get(baseUrl) 
        baselogin.test_success_login(driver)
        currentUrl = driver.current_url
        self.assertIn (currentUrl, baseUrl + "web/index.php/dashboard/index")
        time.sleep(3)
        driver.find_element(
            By.XPATH,
            "//div[@id='app']//aside[@class='oxd-sidepanel']/nav[@role='navigation']//ul[@class='oxd-main-menu']//a[@href='/web/index.php/pim/viewPimModule']/span[.='PIM']",
        ).click()
        time.sleep(3)
        driver.find_element(
            By.XPATH,
            "//div[@id='app']//div[@class='oxd-table-filter']/div[@class='oxd-table-filter-area']/form[@class='oxd-form']/div[@class='oxd-form-row']/div/div[5]/div//input[@placeholder='Type for hints...']",
            ).send_keys("suraj")
        time.sleep(3)
        driver.find_element(By.CLASS_NAME, "oxd-autocomplete-option").click()
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(5)
        valid_message = driver.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']//div[@role='table']/div[1]/div[@role='row']/div[9]").text
        self.assertIn("Actions", valid_message)
        time.sleep(2)

    def test_TC17(self):
        baseUrl = "https://opensource-demo.orangehrmlive.com/"
        driver = self.browser 
        driver.get(baseUrl) 
        baselogin.test_success_login(driver)
        currentUrl = driver.current_url
        self.assertIn (currentUrl, baseUrl + "web/index.php/dashboard/index")
        time.sleep(3)
        driver.find_element(
            By.XPATH,
            "//div[@id='app']//aside[@class='oxd-sidepanel']/nav[@role='navigation']//ul[@class='oxd-main-menu']//a[@href='/web/index.php/pim/viewPimModule']/span[.='PIM']",
        ).click()
        time.sleep(3)
        driver.find_element(
            By.XPATH,
            "//div[@id='app']//div[@class='oxd-table-filter']/div[@class='oxd-table-filter-area']/form[@class='oxd-form']/div[@class='oxd-form-row']/div/div[5]/div//input[@placeholder='Type for hints...']",
            ).send_keys("mulyana")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(5)
        error_message = driver.find_element(By.XPATH, "//div[@id='app']//div[@class='oxd-table-filter']/div[@class='oxd-table-filter-area']/form[@class='oxd-form']/div[@class='oxd-form-row']/div/div[5]/div/span[.='Invalid']").text
        self.assertIn("Invalid", error_message)
        time.sleep(2)
    
    def test_TC18(self):
        baseUrl = "https://opensource-demo.orangehrmlive.com/"
        driver = self.browser 
        driver.get(baseUrl) 
        baselogin.test_success_login(driver)
        currentUrl = driver.current_url
        self.assertIn (currentUrl, baseUrl + "web/index.php/dashboard/index")
        time.sleep(3)
        driver.find_element(
            By.XPATH,
            "//div[@id='app']//aside[@class='oxd-sidepanel']/nav[@role='navigation']//ul[@class='oxd-main-menu']//a[@href='/web/index.php/pim/viewPimModule']/span[.='PIM']",
        ).click()
        time.sleep(3)
        driver.find_element(
            By.XPATH,
            "//div[@id='app']//div[@class='oxd-table-filter']/div[@class='oxd-table-filter-area']/form[@class='oxd-form']/div[@class='oxd-form-row']/div/div[6]/div//div[@class='oxd-select-text-input']",
            ).click()
        time.sleep(3)
        driver.find_element(
            By.XPATH,
            "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[6]/div/div[2]/div/div[2]/div[17]/span",
            ).click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(3)
        valid_message = driver.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']//div[@role='table']/div[2]/div[1]/div[@role='row']/div[5]/div[.='QA Engineer']").text
        self.assertIn("QA Engineer", valid_message)
        time.sleep(3)
    
    def test_TC19(self):
        baseUrl = "https://opensource-demo.orangehrmlive.com/"
        driver = self.browser 
        driver.get(baseUrl) 
        baselogin.test_success_login(driver)
        currentUrl = driver.current_url
        self.assertIn (currentUrl, baseUrl + "web/index.php/dashboard/index")
        time.sleep(3)
        driver.find_element(
            By.XPATH,
            "//div[@id='app']//aside[@class='oxd-sidepanel']/nav[@role='navigation']//ul[@class='oxd-main-menu']//a[@href='/web/index.php/pim/viewPimModule']/span[.='PIM']",
        ).click()
        time.sleep(3)
        driver.find_element(
            By.XPATH,
            "//div[@id='app']//div[@class='oxd-table-filter']/div[@class='oxd-table-filter-area']/form[@class='oxd-form']/div[@class='oxd-form-row']/div/div[7]/div//div[@class='oxd-select-text-input']",
            ).click()
        time.sleep(3)
        driver.find_element(
            By.XPATH,
            "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[7]/div/div[2]/div/div[2]/div[6]/span",
            ).click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(3)
        valid_message = driver.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']//div[@role='table']/div[2]/div[1]/div[@role='row']/div[7]/div[.='Quality Assurance']").text
        self.assertIn("Quality Assurance", valid_message)
        time.sleep(3)
        #TC20 Resset Button
        driver.find_element(By.XPATH, "//button[@type='reset']").click()
        time.sleep(2)

if __name__ == '__main__':
    unittest.main()