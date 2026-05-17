from  utilities import randomeString
from pageObjects.HomePage import HomePage
from pageObjects.AccountRegistrationPage import AccountRegistrationPage
import os
from utilities.readProperties import ReadConfig


class Test_001_AccountReg:
    baseURL = ReadConfig.getApplicationURL()

    def test_account_reg(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.hp = HomePage(self.driver)
        self.hp.clickMyAccount()
        self.hp.clickRegister()
        self.regpage = AccountRegistrationPage(self.driver)
        self.regpage.setFirstName("John")
        self.regpage.setLastName("Canedy")

        self.email = randomeString.random_string_generator() + '@gmail.com'
        self.regpage.setEmail(self.email)

        self.regpage.setTelephone("65656565")
        self.regpage.setPassword("abcxyz")
        self.regpage.setConfirmPassword("abcxyz")
        self.regpage.setPrivacyPolicy()
        self.regpage.clickContinue()
        self.confmsg = self.regpage.getconfirmationmsg()

        if self.confmsg == "Your Account Has Been Created!":
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "test_account_reg.png")
            self.driver.close()
            assert False

