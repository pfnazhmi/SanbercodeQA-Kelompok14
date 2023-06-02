import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys


class TestUser(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_success_edit_user(self): #TestCase1
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
        
 # menu pim
        driver.find_element(
            By.XPATH,
            "//div[@id='app']//aside[@class='oxd-sidepanel']/nav[@role='navigation']//ul[@class='oxd-main-menu']//a[@href='/web/index.php/admin/viewAdminModule']/span[.='Admin']",
        ).click()
        time.sleep(2)  # menu admin
        driver.find_element(
            By.XPATH,
            "//div[@id='app']//header[@class='oxd-topbar']//nav[@role='navigation']/ul/li[1]/span[@class='oxd-topbar-body-nav-tab-item']",
        ).click()
        time.sleep(2)  # menu user management
        driver.find_element(
            By.XPATH,
            "//div[@id='app']//header[@class='oxd-topbar']//nav[@role='navigation']/ul//ul[@role='menu']/li",
        ).click()  # users
        time.sleep(2)
        driver.find_element(
            By.XPATH,
            "//div[@id='app']/div[@class='oxd-layout']//div[@role='table']/div[2]/div[1]/div[@role='row']/div[6]/div/button[2]/i",
        ).click()  # edit button / pencil icon
        time.sleep(2)
        # Menghapus teks yang ada menggunakan kombinasi tombol keyboard
        inputUsername = driver.find_element(
            By.XPATH,
            "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//form[@class='oxd-form']/div[@class='oxd-form-row']/div/div[4]/div/div[2]/input",
        )
        inputUsername.send_keys(Keys.CONTROL + "a")  # Memilih seluruh teks
        inputUsername.send_keys(Keys.DELETE)  # Menghapus teks yang terpilih
        time.sleep(2)
        inputUsername.send_keys("yohannams")  # input username
        time.sleep(2)
        driver.find_element(
            By.XPATH,
            "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//form[@class='oxd-form']/div[@class='oxd-form-row']/div/div[1]/div/div[2]/div[@class='oxd-select-wrapper']/div//i",
        ).click()  # option user role
        time.sleep(2)
        driver.find_element(
            By.XPATH,
            "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//form[@class='oxd-form']/div[@class='oxd-form-row']//div[@role='listbox']/div[3]/span[.='ESS']",
        ).click()  # choose user role
        time.sleep(2)
        driver.find_element(
            By.XPATH,
            "//div[@id='app']/div[@class='oxd-layout']//form[@class='oxd-form']/div[@class='oxd-form-actions']/button[@type='submit']",
        ).click()  # klik save
        time.sleep(1)
        driver.find_element(
            By.XPATH,
            "//div[@id='app']/div[@class='oxd-layout']//form[@class='oxd-form']/div[@class='oxd-form-actions']/button[@type='submit']",
        )  # notif success

    def test_failed_edit_user_invalid_username(self):
        # steps
        baseurl = "https://opensource-demo.orangehrmlive.com/"
        driver = self.browser  # buka web browser
        driver.get(baseurl)  # buka situs
        time.sleep(3)
        driver.find_element(By.NAME, "username").send_keys("Admin")  # username
        time.sleep(1)
        driver.find_element(By.NAME, "password").send_keys("admin123")  # isi password
        time.sleep(1)
        driver.find_element(By.CLASS_NAME, "orangehrm-login-button").click()
        time.sleep(5)
        # user
        driver.find_element(
            By.XPATH,
            "//div[@id='app']//aside[@class='oxd-sidepanel']/nav[@role='navigation']//ul[@class='oxd-main-menu']//a[@href='/web/index.php/admin/viewAdminModule']/span[.='Admin']",
        ).click()
        time.sleep(2)  # menu admin
        driver.find_element(
            By.XPATH,
            "//div[@id='app']//header[@class='oxd-topbar']//nav[@role='navigation']/ul/li[1]/span[@class='oxd-topbar-body-nav-tab-item']",
        ).click()
        time.sleep(2)  # menu user management
        driver.find_element(
            By.XPATH,
            "//div[@id='app']//header[@class='oxd-topbar']//nav[@role='navigation']/ul//ul[@role='menu']/li",
        ).click()  # users
        time.sleep(2)
        driver.find_element(
            By.XPATH,
            "//div[@id='app']/div[@class='oxd-layout']//div[@role='table']/div[2]/div[1]/div[@role='row']/div[6]/div/button[2]/i",
        ).click()  # edit button / pencil icon
        time.sleep(2)
        # Menghapus teks yang ada menggunakan kombinasi tombol keyboard
        inputUsername = driver.find_element(
            By.XPATH,
            "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//form[@class='oxd-form']/div[@class='oxd-form-row']/div/div[4]/div/div[2]/input",
        )
        inputUsername.send_keys(Keys.CONTROL + "a")  # Memilih seluruh teks
        inputUsername.send_keys(Keys.DELETE)  # Menghapus teks yang terpilih
        time.sleep(2)
        inputUsername.send_keys("a")  # input username
        time.sleep(2)
        driver.find_element(
            By.XPATH,
            "//div[@id='app']/div[@class='oxd-layout']//form[@class='oxd-form']/div[@class='oxd-form-actions']/button[@type='submit']",
        ).click()  # klik save
        time.sleep(1)
        driver.find_element(
            By.XPATH,
            "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//form[@class='oxd-form']/div[@class='oxd-form-row']//span[.='Should be at least 5 characters']",
        )  # showing error failed
        
    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()