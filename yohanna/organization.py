import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from organizationLocator import elem
from organizationData import dataInput


class TestOrganization(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_success_edit_organization_general_information(self):
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
            elem.organizationDropdown,
        ).click()
        time.sleep(2)  # organization
        driver.find_element(
            By.XPATH,
            elem.generalInformationOption,
        ).click()  # general information
        time.sleep(2)
        driver.find_element(
            By.XPATH,
            elem.editButton,
        ).click()  # edit button
        time.sleep(2)
        # Menghapus teks yang ada menggunakan kombinasi tombol keyboard
        inputOrganizationName = driver.find_element(
            By.XPATH,
            elem.organizationName,
        )
        inputOrganizationName.send_keys(Keys.CONTROL + "a")  # Memilih seluruh teks
        inputOrganizationName.send_keys(Keys.DELETE)  # Menghapus teks yang terpilih
        time.sleep(2)
        inputOrganizationName.send_keys(
            dataInput.validOrganizationName
        )  # input organization name
        time.sleep(2)
        inputRegistrationNumber = driver.find_element(
            By.XPATH,
            elem.registrationNumber,
        )
        inputRegistrationNumber.send_keys(Keys.CONTROL + "a")  # Memilih seluruh teks
        inputRegistrationNumber.send_keys(Keys.DELETE)  # Menghapus teks yang terpilih
        time.sleep(2)
        inputRegistrationNumber.send_keys(
            dataInput.validRegistrationNumber
        )  # input registration number
        driver.find_element(
            By.XPATH,
            elem.saveButton,
        ).click()  # klik save
        time.sleep(1)
        driver.find_element(
            By.ID,
            elem.notificationSuccess,
        )  # notif success
        # response_data = driver.find_element(
        #     By.XPATH,
        #     elem.notificationSuccess,
        # ).text
        # self.assertIn(dataInput.reqSuccessUpdated, response_data)  # notif success

    def test_failed_edit_organization_general_information(self):
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
            elem.organizationDropdown,
        ).click()
        time.sleep(2)  # organization
        driver.find_element(
            By.XPATH,
            elem.generalInformationOption,
        ).click()  # general information
        time.sleep(2)
        driver.find_element(
            By.XPATH,
            elem.editButton,
        ).click()  # edit button
        time.sleep(2)
        # Menghapus teks yang ada menggunakan kombinasi tombol keyboard
        inputPhone = driver.find_element(
            By.XPATH,
            elem.phone,
        )
        inputPhone.send_keys(Keys.CONTROL + "a")  # Memilih seluruh teks
        inputPhone.send_keys(Keys.DELETE)  # Menghapus teks yang terpilih
        time.sleep(2)
        inputPhone.send_keys(dataInput.invalidPhone)  # input phone
        driver.find_element(
            By.XPATH,
            elem.saveButton,
        ).click()  # klik save
        time.sleep(1)
        driver.find_element(
            By.XPATH,
            elem.errorPhoneNumber,
        )  # notif error
        response_data = driver.find_element(
            By.XPATH,
            elem.errorPhoneNumber,
        ).text
        self.assertIn(dataInput.reqPhone, response_data)  # notif error

    def tearDown(self):
        self.browser.close()


if __name__ == "__main__":
    unittest.main()
