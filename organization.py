import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys


class TestOrganization(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_success_edit_organization_general_information(self):
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
            "//div[@id='app']//header[@class='oxd-topbar']//nav[@role='navigation']/ul/li[3]",
        ).click()
        time.sleep(2)  # organization
        driver.find_element(
            By.XPATH,
            "//div[@id='app']//header[@class='oxd-topbar']//nav[@role='navigation']/ul//ul[@role='menu']/li[1]/a[@role='menuitem']",
        ).click()  # general information
        time.sleep(2)
        driver.find_element(
            By.XPATH,
            "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//div[@class='oxd-switch-wrapper']//span",
        ).click()  # edit button
        time.sleep(2)
        # Menghapus teks yang ada menggunakan kombinasi tombol keyboard
        inputOrganizationName = driver.find_element(
            By.XPATH,
            "//div[@id='app']//form[@class='oxd-form']/div[1]/div/div[1]/div//input",
        )
        inputOrganizationName.send_keys(Keys.CONTROL + "a")  # Memilih seluruh teks
        inputOrganizationName.send_keys(Keys.DELETE)  # Menghapus teks yang terpilih
        time.sleep(2)
        inputOrganizationName.send_keys("OrangeHRM")  # input organization name
        time.sleep(2)
        inputRegistrationNumber = driver.find_element(
            By.XPATH,
            "//div[@id='app']//form[@class='oxd-form']/div[2]/div/div[1]/div//input",
        )
        inputRegistrationNumber.send_keys(Keys.CONTROL + "a")  # Memilih seluruh teks
        inputRegistrationNumber.send_keys(Keys.DELETE)  # Menghapus teks yang terpilih
        time.sleep(2)
        inputRegistrationNumber.send_keys("1")  # input registration number
        driver.find_element(
            By.XPATH,
            "//div[@id='app']/div[@class='oxd-layout']//form[@class='oxd-form']/div[@class='oxd-form-actions']/button[@type='submit']",
        ).click()  # klik save
        time.sleep(1)
        driver.find_element(
            By.ID,
            "oxd-toaster_1",
        )  # notif success

    def test_failed_edit_organization_general_information(self):
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
            "//div[@id='app']//header[@class='oxd-topbar']//nav[@role='navigation']/ul/li[3]",
        ).click()
        time.sleep(2)  # organization
        driver.find_element(
            By.XPATH,
            "//div[@id='app']//header[@class='oxd-topbar']//nav[@role='navigation']/ul//ul[@role='menu']/li[1]/a[@role='menuitem']",
        ).click()  # general information
        time.sleep(2)
        driver.find_element(
            By.XPATH,
            "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//div[@class='oxd-switch-wrapper']//span",
        ).click()  # edit button
        time.sleep(2)
        # Menghapus teks yang ada menggunakan kombinasi tombol keyboard
        inputPhone = driver.find_element(
            By.XPATH,
            "//div[@id='app']//form[@class='oxd-form']/div[3]/div/div[1]/div//input",
        )
        inputPhone.send_keys(Keys.CONTROL + "a")  # Memilih seluruh teks
        inputPhone.send_keys(Keys.DELETE)  # Menghapus teks yang terpilih
        time.sleep(2)
        inputPhone.send_keys("asd")  # input phone
        driver.find_element(
            By.XPATH,
            "//div[@id='app']/div[@class='oxd-layout']//form[@class='oxd-form']/div[@class='oxd-form-actions']/button[@type='submit']",
        ).click()  # klik save
        time.sleep(1)
        driver.find_element(
            By.XPATH,
            "//div[@id='app']//form[@class='oxd-form']/div[3]/div/div[1]/div/span[.='Allows numbers and only + - / ( )']",
        )  # notif error

    def tearDown(self):
        self.browser.close()


if __name__ == "__main__":
    unittest.main()
