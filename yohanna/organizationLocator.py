class elem:
    username = "username"
    password = "password"
    loginButton = "orangehrm-login-button"
    menuAdmin = "//div[@id='app']//aside[@class='oxd-sidepanel']/nav[@role='navigation']//ul[@class='oxd-main-menu']//a[@href='/web/index.php/admin/viewAdminModule']/span[.='Admin']"
    organizationDropdown = "//div[@id='app']//header[@class='oxd-topbar']//nav[@role='navigation']/ul/li[3]"
    generalInformationOption = "//div[@id='app']//header[@class='oxd-topbar']//nav[@role='navigation']/ul//ul[@role='menu']/li[1]/a[@role='menuitem']"
    editButton = "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//div[@class='oxd-switch-wrapper']//span"
    organizationName = (
        "//div[@id='app']//form[@class='oxd-form']/div[1]/div/div[1]/div//input"
    )
    registrationNumber = (
        "//div[@id='app']//form[@class='oxd-form']/div[2]/div/div[1]/div//input"
    )
    saveButton = "//div[@id='app']/div[@class='oxd-layout']//form[@class='oxd-form']/div[@class='oxd-form-actions']/button[@type='submit']"
    notificationSuccess = "oxd-toaster_1"
    # notificationSuccess = "//div[@id='oxd-toaster_1']/div//p[@class='oxd-text oxd-text--p oxd-text--toast-title oxd-toast-content-text']"
    phone = "//div[@id='app']//form[@class='oxd-form']/div[3]/div/div[1]/div//input"
    errorPhoneNumber = "//div[@id='app']//form[@class='oxd-form']/div[3]/div/div[1]/div/span[.='Allows numbers and only + - / ( )']"
