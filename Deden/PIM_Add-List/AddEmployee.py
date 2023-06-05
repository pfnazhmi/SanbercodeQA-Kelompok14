import unittest
import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import baselogin

class TestPIMAdd(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_TC01(self):
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
        currentUrl = driver.current_url
        self.assertIn (currentUrl, baseUrl + "web/index.php/pim/viewEmployeeList")
        time.sleep(3)
        driver.find_element(By.XPATH, "//button[normalize-space()='Add']").click()
        currentUrl = driver.current_url
        self.assertIn (currentUrl, baseUrl + "web/index.php/pim/addEmployee")
        time.sleep(3)
        driver.find_element(By.NAME, "firstName").send_keys("Ameera")
        driver.find_element(By.NAME, "middleName").send_keys("Qince")
        driver.find_element(By.NAME, "lastName").send_keys("Ahmad")
        driver.find_element(By.CLASS_NAME, "employee-image").click()
        time.sleep(3)
        pyautogui.write(r"C:\Users\user\Documents\Final_Project\SanbercodeQA-Kelompok14\Deden\foto\Avatar-Profile-PNG-Photos.png")
        pyautogui.press("enter")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
    
    def test_TC02(self):
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
        currentUrl = driver.current_url
        self.assertIn (currentUrl, baseUrl + "web/index.php/pim/viewEmployeeList")
        time.sleep(3)
        driver.find_element(By.XPATH, "//button[normalize-space()='Add']").click()
        currentUrl = driver.current_url
        self.assertIn (currentUrl, baseUrl + "web/index.php/pim/addEmployee")
        time.sleep(3)
        driver.find_element(By.NAME, "firstName").send_keys("")
        driver.find_element(By.NAME, "middleName").send_keys("Qince")
        driver.find_element(By.NAME, "lastName").send_keys("Ahmad")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        error_message = driver.find_element(By.XPATH, "//span[@class='oxd-text oxd-text--span oxd-input-field-error-message oxd-input-group__message']").text
        self.assertIn("Required", error_message)
        time.sleep(3)
    
    def test_TC03(self):
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
        currentUrl = driver.current_url
        self.assertIn (currentUrl, baseUrl + "web/index.php/pim/viewEmployeeList")
        time.sleep(3)
        driver.find_element(By.XPATH, "//button[normalize-space()='Add']").click()
        currentUrl = driver.current_url
        self.assertIn (currentUrl, baseUrl + "web/index.php/pim/addEmployee")
        time.sleep(3)
        driver.find_element(By.NAME, "firstName").send_keys("Ameera")
        driver.find_element(By.NAME, "middleName").send_keys("Qince")
        driver.find_element(By.NAME, "lastName").send_keys("")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        error_message = driver.find_element(By.XPATH, "//span[@class='oxd-text oxd-text--span oxd-input-field-error-message oxd-input-group__message']").text
        self.assertIn("Required", error_message)
        time.sleep(3)

    def test_TC04(self):
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
        currentUrl = driver.current_url
        self.assertIn (currentUrl, baseUrl + "web/index.php/pim/viewEmployeeList")
        time.sleep(3)
        driver.find_element(By.XPATH, "//button[normalize-space()='Add']").click()
        currentUrl = driver.current_url
        self.assertIn (currentUrl, baseUrl + "web/index.php/pim/addEmployee")
        time.sleep(3)
        driver.find_element(By.NAME, "firstName").send_keys("Ameera")
        driver.find_element(By.NAME, "middleName").send_keys("Qince")
        driver.find_element(By.NAME, "lastName").send_keys("Ahmad")
        driver.find_element(By.CLASS_NAME, "employee-image").click()
        time.sleep(3)
        pyautogui.write(r"C:\Users\user\Documents\Final_Project\SanbercodeQA-Kelompok14\Deden\foto\Avatar_Profile_Invalid.jpg")
        pyautogui.press("enter")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        error_message = driver.find_element(By.XPATH, "//span[@class='oxd-text oxd-text--span oxd-input-field-error-message oxd-input-group__message']").text
        self.assertIn("Attachment Size Exceeded", error_message)
        time.sleep(5)

    def test_TC05(self):
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
        currentUrl = driver.current_url
        self.assertIn (currentUrl, baseUrl + "web/index.php/pim/viewEmployeeList")
        time.sleep(3)
        driver.find_element(By.XPATH, "//button[normalize-space()='Add']").click()
        currentUrl = driver.current_url
        self.assertIn (currentUrl, baseUrl + "web/index.php/pim/addEmployee")
        time.sleep(3)
        driver.find_element(By.NAME, "firstName").send_keys("Ameeraa")
        driver.find_element(By.NAME, "middleName").send_keys("Qince")
        driver.find_element(By.NAME, "lastName").send_keys("Ahmadd")
        driver.find_element(
            By.XPATH, "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']//form[@class='oxd-form']//div[@class='oxd-form-row user-form-header']/div[@class='oxd-switch-wrapper']//span"
            ).click()
        time.sleep(3)
        driver.find_element(
            By.XPATH, "//div[@id='app']/div[@class='oxd-layout']//form[@class='oxd-form']//div[@class='orangehrm-employee-form']/div[3]/div/div[1]/div//input"
            ).send_keys("Ameeraaaaaaabxx")
        driver.find_element(
            By.XPATH, "//div[@id='app']/div[@class='oxd-layout']//form[@class='oxd-form']//div[@class='oxd-form-row user-password-row']/div/div[@class='oxd-grid-item oxd-grid-item--gutters user-password-cell']/div//input[@type='password']"
            ).send_keys("Ameeraaa123")
        driver.find_element(
            By.XPATH, "//div[@id='app']/div[@class='oxd-layout']//form[@class='oxd-form']//div[@class='oxd-form-row user-password-row']/div/div[@class='oxd-grid-item oxd-grid-item--gutters']/div//input[@type='password']"
            ).send_keys("Ameeraaa123")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()

    def test_TC06(self):
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
        currentUrl = driver.current_url
        self.assertIn (currentUrl, baseUrl + "web/index.php/pim/viewEmployeeList")
        time.sleep(3)
        driver.find_element(By.XPATH, "//button[normalize-space()='Add']").click()
        currentUrl = driver.current_url
        self.assertIn (currentUrl, baseUrl + "web/index.php/pim/addEmployee")
        time.sleep(3)
        driver.find_element(By.NAME, "firstName").send_keys("Ameeraa")
        driver.find_element(By.NAME, "middleName").send_keys("Qince")
        driver.find_element(By.NAME, "lastName").send_keys("Ahmadd")
        driver.find_element(
            By.XPATH, "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']//form[@class='oxd-form']//div[@class='oxd-form-row user-form-header']/div[@class='oxd-switch-wrapper']//span"
            ).click()
        time.sleep(3)
        driver.find_element(
            By.XPATH, "//div[@id='app']/div[@class='oxd-layout']//form[@class='oxd-form']//div[@class='orangehrm-employee-form']/div[3]/div/div[1]/div//input"
            ).send_keys("Ame")
        driver.find_element(
            By.XPATH, "//div[@id='app']/div[@class='oxd-layout']//form[@class='oxd-form']//div[@class='oxd-form-row user-password-row']/div/div[@class='oxd-grid-item oxd-grid-item--gutters user-password-cell']/div//input[@type='password']"
            ).send_keys("Ameeraaa123")
        driver.find_element(
            By.XPATH, "//div[@id='app']/div[@class='oxd-layout']//form[@class='oxd-form']//div[@class='oxd-form-row user-password-row']/div/div[@class='oxd-grid-item oxd-grid-item--gutters']/div//input[@type='password']"
            ).send_keys("Ameeraaa123")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        error_message = driver.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']//form[@class='oxd-form']//div[@class='orangehrm-employee-form']/div[3]/div/div[1]/div/span[.='Should be at least 5 characters']").text
        self.assertIn("Should be at least 5 characters", error_message)
        time.sleep(3)

    def test_TC07(self):
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
        currentUrl = driver.current_url
        self.assertIn (currentUrl, baseUrl + "web/index.php/pim/viewEmployeeList")
        time.sleep(3)
        driver.find_element(By.XPATH, "//button[normalize-space()='Add']").click()
        currentUrl = driver.current_url
        self.assertIn (currentUrl, baseUrl + "web/index.php/pim/addEmployee")
        time.sleep(3)
        driver.find_element(By.NAME, "firstName").send_keys("Ameeraa")
        driver.find_element(By.NAME, "middleName").send_keys("Qince")
        driver.find_element(By.NAME, "lastName").send_keys("Ahmadd")
        driver.find_element(
            By.XPATH, "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']//form[@class='oxd-form']//div[@class='oxd-form-row user-form-header']/div[@class='oxd-switch-wrapper']//span"
            ).click()
        time.sleep(3)
        driver.find_element(
            By.XPATH, "//div[@id='app']/div[@class='oxd-layout']//form[@class='oxd-form']//div[@class='orangehrm-employee-form']/div[3]/div/div[1]/div//input"
            ).send_keys("Ameraaaaaxyz")
        driver.find_element(
            By.XPATH, "//div[@id='app']/div[@class='oxd-layout']//form[@class='oxd-form']//div[@class='oxd-form-row user-password-row']/div/div[@class='oxd-grid-item oxd-grid-item--gutters user-password-cell']/div//input[@type='password']"
            ).send_keys("Ameeraqince")
        driver.find_element(
            By.XPATH, "//div[@id='app']/div[@class='oxd-layout']//form[@class='oxd-form']//div[@class='oxd-form-row user-password-row']/div/div[@class='oxd-grid-item oxd-grid-item--gutters']/div//input[@type='password']"
            ).send_keys("Ameeraqince")
        time.sleep(3)
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        error_message = driver.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']//form[@class='oxd-form']//div[@class='oxd-form-row user-password-row']/div/div[@class='oxd-grid-item oxd-grid-item--gutters user-password-cell']/div/span[.='Your password must contain minimum 1 number']").text
        self.assertIn("Your password must contain minimum 1 number", error_message)
        time.sleep(3)

    def test_TC08(self):
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
        currentUrl = driver.current_url
        self.assertIn (currentUrl, baseUrl + "web/index.php/pim/viewEmployeeList")
        time.sleep(3)
        driver.find_element(By.XPATH, "//button[normalize-space()='Add']").click()
        currentUrl = driver.current_url
        self.assertIn (currentUrl, baseUrl + "web/index.php/pim/addEmployee")
        time.sleep(3)
        driver.find_element(By.NAME, "firstName").send_keys("Ameeraa")
        driver.find_element(By.NAME, "middleName").send_keys("Qince")
        driver.find_element(By.NAME, "lastName").send_keys("Ahmadd")
        driver.find_element(
            By.XPATH, "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']//form[@class='oxd-form']//div[@class='oxd-form-row user-form-header']/div[@class='oxd-switch-wrapper']//span"
            ).click()
        time.sleep(3)
        driver.find_element(
            By.XPATH, "//div[@id='app']/div[@class='oxd-layout']//form[@class='oxd-form']//div[@class='orangehrm-employee-form']/div[3]/div/div[1]/div//input"
            ).send_keys("Ameraaaaaxyz")
        driver.find_element(
            By.XPATH, "//div[@id='app']/div[@class='oxd-layout']//form[@class='oxd-form']//div[@class='oxd-form-row user-password-row']/div/div[@class='oxd-grid-item oxd-grid-item--gutters user-password-cell']/div//input[@type='password']"
            ).send_keys("Ameeraqince123")
        driver.find_element(
            By.XPATH, "//div[@id='app']/div[@class='oxd-layout']//form[@class='oxd-form']//div[@class='oxd-form-row user-password-row']/div/div[@class='oxd-grid-item oxd-grid-item--gutters']/div//input[@type='password']"
            ).send_keys("Ameeraqince")
        time.sleep(3)
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        error_message = driver.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']//form[@class='oxd-form']//div[@class='oxd-form-row user-password-row']/div/div[@class='oxd-grid-item oxd-grid-item--gutters']/div/span[.='Passwords do not match']").text
        self.assertIn("Passwords do not match", error_message)
        time.sleep(3)



if __name__ == '__main__':
    unittest.main()