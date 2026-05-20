from  utilities import randomeString
from pageObjects.HomePage import HomePage
from pageObjects.AccountRegistrationPage import AccountRegistrationPage
import os
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_AccountReg:
    baseURL = ReadConfig.getApplicationURL()
    logger=LogGen.loggen()

    @pytest.mark.regression
    def test_account_reg(self, setup):
        self.logger.info("Testing account registration")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info("launching application")
        self.driver.maximize_window()
        self.hp = HomePage(self.driver)
        self.hp.clickMyAccount()
        self.hp.clickRegister()
        self.regpage = AccountRegistrationPage(self.driver)
        self.logger.info("Entering details")
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
            self.logger.error("Account registration failed")
            self.driver.close()
            assert False
        self.logger.info("Account registration test passed")