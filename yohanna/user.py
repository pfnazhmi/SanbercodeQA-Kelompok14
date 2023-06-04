import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from userLocator import elem
from userData import dataInput


class TestUser(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_success_edit_user_change_username_user_role(self):
        # steps
        driver = self.browser  # buka web browser
        driver.get(dataInput.baseurl)  # buka situs
        time.sleep(3)
        driver.find_element(By.NAME, elem.username).send_keys(
            dataInput.validUser
        )  # username
        time.sleep(1)
        driver.find_element(By.NAME, elem.password).send_keys(
            dataInput.validPass
        )  # isi password
        time.sleep(1)
        driver.find_element(By.CLASS_NAME, elem.loginButton).click()
        time.sleep(5)
        # user
        driver.find_element(
            By.XPATH,
            elem.menuAdmin,
        ).click()
        time.sleep(2)  # menu admin
        driver.find_element(
            By.XPATH,
            elem.userManagementDropdown,
        ).click()
        time.sleep(2)  # menu user management
        driver.find_element(
            By.XPATH,
            elem.usersOption,
        ).click()  # users
        time.sleep(2)
        driver.find_element(
            By.XPATH,
            elem.editButton,
        ).click()  # edit toggle
        time.sleep(2)
        # Menghapus teks yang ada menggunakan kombinasi tombol keyboard
        inputUsername = driver.find_element(
            By.XPATH,
            elem.usernameEdit,
        )
        inputUsername.send_keys(Keys.CONTROL + "a")  # Memilih seluruh teks
        inputUsername.send_keys(Keys.DELETE)  # Menghapus teks yang terpilih
        time.sleep(2)
        inputUsername.send_keys(dataInput.validUsername)  # input username
        time.sleep(2)
        driver.find_element(
            By.XPATH,
            elem.userRole,
        ).click()  # option user role
        time.sleep(2)
        driver.find_element(
            By.XPATH,
            elem.userRoleChoose,
        ).click()  # choose user role
        time.sleep(2)
        driver.find_element(
            By.XPATH,
            elem.saveButton,
        ).click()  # klik save
        time.sleep(1)
        driver.find_element(
            By.XPATH,
            elem.notifSuccess,
        )  # notif success

    def test_success_edit_user_change_password(self):
        # steps
        driver = self.browser  # buka web browser
        driver.get(dataInput.baseurl)  # buka situs
        time.sleep(3)
        driver.find_element(By.NAME, elem.username).send_keys(
            dataInput.validUser
        )  # username
        time.sleep(1)
        driver.find_element(By.NAME, elem.password).send_keys(
            dataInput.validPass
        )  # isi password
        time.sleep(1)
        driver.find_element(By.CLASS_NAME, elem.loginButton).click()
        time.sleep(5)
        # user
        driver.find_element(
            By.XPATH,
            elem.menuAdmin,
        ).click()
        time.sleep(2)  # menu admin
        driver.find_element(
            By.XPATH,
            elem.userManagementDropdown,
        ).click()
        time.sleep(2)  # menu user management
        driver.find_element(
            By.XPATH,
            elem.usersOption,
        ).click()  # users
        time.sleep(2)
        driver.find_element(
            By.XPATH,
            elem.editButton,
        ).click()  # edit button / pencil icon
        time.sleep(2)
        driver.find_element(
            By.XPATH,
            elem.checkboxChangePassword,
        ).click()  # checkbox change password
        time.sleep(2)
        driver.find_element(
            By.XPATH,
            elem.passwordChange,
        ).send_keys(
            dataInput.validPassChange
        )  # input password
        time.sleep(2)
        driver.find_element(
            By.XPATH,
            elem.confirmPassChange,
        ).send_keys(
            dataInput.validConfirmPassChange
        )  # input confirm password
        time.sleep(2)
        driver.find_element(
            By.XPATH,
            elem.saveButton,
        ).click()  # klik save
        time.sleep(1)
        driver.find_element(
            By.XPATH,
            elem.notifSuccess,
        )  # notif success

    def test_failed_edit_user_invalid_username(self):
        # steps
        driver = self.browser  # buka web browser
        driver.get(dataInput.baseurl)  # buka situs
        time.sleep(3)
        driver.find_element(By.NAME, elem.username).send_keys(
            dataInput.validUser
        )  # username
        time.sleep(1)
        driver.find_element(By.NAME, elem.password).send_keys(
            dataInput.validPass
        )  # isi password
        time.sleep(1)
        driver.find_element(By.CLASS_NAME, elem.loginButton).click()
        time.sleep(5)
        # user
        driver.find_element(
            By.XPATH,
            elem.menuAdmin,
        ).click()
        time.sleep(2)  # menu admin
        driver.find_element(
            By.XPATH,
            elem.userManagementDropdown,
        ).click()
        time.sleep(2)  # menu user management
        driver.find_element(
            By.XPATH,
            elem.usersOption,
        ).click()  # users
        time.sleep(2)
        driver.find_element(
            By.XPATH,
            elem.editButton,
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
        )  # showing error message

    def test_failed_edit_user_confirm_password_not_match(self):
        # steps
        driver = self.browser  # buka web browser
        driver.get(dataInput.baseurl)  # buka situs
        time.sleep(3)
        driver.find_element(By.NAME, elem.username).send_keys(
            dataInput.validUser
        )  # username
        time.sleep(1)
        driver.find_element(By.NAME, elem.password).send_keys(
            dataInput.validPass
        )  # isi password
        time.sleep(1)
        driver.find_element(By.CLASS_NAME, elem.loginButton).click()
        time.sleep(5)
        # user
        driver.find_element(
            By.XPATH,
            elem.menuAdmin,
        ).click()
        time.sleep(2)  # menu admin
        driver.find_element(
            By.XPATH,
            elem.userManagementDropdown,
        ).click()
        time.sleep(2)  # menu user management
        driver.find_element(
            By.XPATH,
            elem.usersOption,
        ).click()  # users
        time.sleep(2)
        driver.find_element(
            By.XPATH,
            elem.editButton,
        ).click()  # edit button / pencil icon
        time.sleep(2)
        driver.find_element(
            By.XPATH,
            "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//form[@class='oxd-form']/div[@class='oxd-form-row']/div/div[5]//i",
        ).click()  # checkbox change password
        time.sleep(2)
        driver.find_element(
            By.XPATH,
            "//div[@id='app']//form[@class='oxd-form']/div[@class='oxd-form-row user-password-row']/div/div[@class='oxd-grid-item oxd-grid-item--gutters user-password-cell']/div//input[@type='password']",
        ).send_keys(
            "12345678"
        )  # input password
        time.sleep(2)
        driver.find_element(
            By.XPATH,
            "//div[@id='app']//form[@class='oxd-form']/div[@class='oxd-form-row user-password-row']/div/div[@class='oxd-grid-item oxd-grid-item--gutters']/div//input[@type='password']",
        ).send_keys(
            "87654321"
        )  # input confirm password
        time.sleep(2)
        driver.find_element(
            By.XPATH,
            "//div[@id='app']/div[@class='oxd-layout']//form[@class='oxd-form']/div[@class='oxd-form-actions']/button[@type='submit']",
        ).click()  # klik save
        time.sleep(1)
        driver.find_element(
            By.XPATH,
            "//div[@id='app']//form[@class='oxd-form']/div[@class='oxd-form-row user-password-row']/div/div[@class='oxd-grid-item oxd-grid-item--gutters']/div/span[.='Passwords do not match']",
        )  # showing error message

    def test_failed_edit_user_error_message_not_match(self):
        # steps
        driver = self.browser  # buka web browser
        driver.get(dataInput.baseurl)  # buka situs
        time.sleep(3)
        driver.find_element(By.NAME, elem.username).send_keys(
            dataInput.validUser
        )  # username
        time.sleep(1)
        driver.find_element(By.NAME, elem.password).send_keys(
            dataInput.validPass
        )  # isi password
        time.sleep(1)
        driver.find_element(By.CLASS_NAME, elem.loginButton).click()
        time.sleep(5)
        # user
        driver.find_element(
            By.XPATH,
            elem.menuAdmin,
        ).click()
        time.sleep(2)  # menu admin
        driver.find_element(
            By.XPATH,
            elem.userManagementDropdown,
        ).click()
        time.sleep(2)  # menu user management
        driver.find_element(
            By.XPATH,
            elem.usersOption,
        ).click()  # users
        time.sleep(2)
        driver.find_element(
            By.XPATH,
            elem.editButton,
        ).click()  # edit button / pencil icon
        time.sleep(2)
        driver.find_element(
            By.XPATH,
            "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//form[@class='oxd-form']/div[@class='oxd-form-row']/div/div[5]//i",
        ).click()  # checkbox change password
        time.sleep(2)
        driver.find_element(
            By.XPATH,
            "//div[@id='app']//form[@class='oxd-form']/div[@class='oxd-form-row user-password-row']/div/div[@class='oxd-grid-item oxd-grid-item--gutters user-password-cell']/div//input[@type='password']",
        ).send_keys(
            "1234567"
        )  # input password
        time.sleep(2)
        driver.find_element(
            By.XPATH,
            "//div[@id='app']//form[@class='oxd-form']/div[@class='oxd-form-row user-password-row']/div/div[@class='oxd-grid-item oxd-grid-item--gutters']/div//input[@type='password']",
        ).send_keys(
            "1234567"
        )  # input confirm password
        time.sleep(2)
        driver.find_element(
            By.XPATH,
            "//div[@id='app']/div[@class='oxd-layout']//form[@class='oxd-form']/div[@class='oxd-form-actions']/button[@type='submit']",
        ).click()  # klik save
        time.sleep(1)
        expected_text = "Should have at least 8 characters"
        error_message = driver.find_element(
            By.XPATH,
            "//div[@id='app']//form[@class='oxd-form']/div[@class='oxd-form-row user-password-row']/div/div[@class='oxd-grid-item oxd-grid-item--gutters user-password-cell']/div/span[.='Should have at least 7 characters']",
        )
        error_message.text == expected_text
        # error_message.is_displayed() and "Should have at least 7 characters" in error_message.text  # showing error message

    def test_success_delete_user(self):
        # steps
        driver = self.browser  # buka web browser
        driver.get(dataInput.baseurl)  # buka situs
        time.sleep(3)
        driver.find_element(By.NAME, elem.username).send_keys(
            dataInput.validUser
        )  # username
        time.sleep(1)
        driver.find_element(By.NAME, elem.password).send_keys(
            dataInput.validPass
        )  # isi password
        time.sleep(1)
        driver.find_element(By.CLASS_NAME, elem.loginButton).click()
        time.sleep(5)
        # user
        driver.find_element(
            By.XPATH,
            elem.menuAdmin,
        ).click()
        time.sleep(2)  # menu admin
        driver.find_element(
            By.XPATH,
            elem.userManagementDropdown,
        ).click()
        time.sleep(2)  # menu user management
        driver.find_element(
            By.XPATH,
            elem.usersOption,
        ).click()  # users
        time.sleep(2)
        driver.find_element(
            By.XPATH,
            "//div[@id='app']/div[@class='oxd-layout']//div[@role='table']/div[2]/div[3]/div[@role='row']/div[6]/div/button[2]/i",
        ).click()  # delete button / trash icon
        time.sleep(2)
        driver.find_element(
            By.XPATH,
            "//div[@id='app']/div[@role='dialog']//div[@role='document']/div[@class='orangehrm-modal-footer']/button[2]",
        ).click()  # confirmation delete (yes,delete)
        time.sleep(2)
        driver.find_element(
            By.XPATH,
            "//div[@id='oxd-toaster_1']/div//p[@class='oxd-text oxd-text--p oxd-text--toast-title oxd-toast-content-text']",
        )  # notif success

    def test_success_delete_list_user(self):
        # steps
        driver = self.browser  # buka web browser
        driver.get(dataInput.baseurl)  # buka situs
        time.sleep(3)
        driver.find_element(By.NAME, elem.username).send_keys(
            dataInput.validUser
        )  # username
        time.sleep(1)
        driver.find_element(By.NAME, elem.password).send_keys(
            dataInput.validPass
        )  # isi password
        time.sleep(1)
        driver.find_element(By.CLASS_NAME, elem.loginButton).click()
        time.sleep(5)
        # user
        driver.find_element(
            By.XPATH,
            elem.menuAdmin,
        ).click()
        time.sleep(2)  # menu admin
        driver.find_element(
            By.XPATH,
            elem.userManagementDropdown,
        ).click()
        time.sleep(2)  # menu user management
        driver.find_element(
            By.XPATH,
            elem.usersOption,
        ).click()  # users
        time.sleep(2)
        driver.find_element(
            By.XPATH,
            "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//div[@role='table']/div[2]/div[2]/div[@role='row']/div[1]//i",
        ).click()  # checklist data user 1
        time.sleep(2)
        driver.find_element(
            By.XPATH,
            "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//div[@role='table']/div[2]/div[3]/div[@role='row']/div[1]//i",
        ).click()  # checklist data user 2
        time.sleep(2)
        driver.find_element(
            By.XPATH,
            "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']//button[@type='button']",
        ).click()  # click button delete selected
        time.sleep(2)
        driver.find_element(
            By.XPATH,
            "//div[@id='app']/div[@role='dialog']//div[@role='document']/div[@class='orangehrm-modal-footer']/button[2]",
        ).click()  # confirmation delete (yes,delete)
        time.sleep(2)
        driver.find_element(
            By.XPATH,
            "//div[@id='oxd-toaster_1']/div//p[@class='oxd-text oxd-text--p oxd-text--toast-title oxd-toast-content-text']",
        ).text == "successfully Deleted"  # notif success

    def tearDown(self):
        self.browser.close()


if __name__ == "__main__":
    unittest.main()
