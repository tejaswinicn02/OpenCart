import pytest
from utilities.readProperties import ReadConfig
from pageObjects.HomePage import HomePage
from utilities.customLogger import LogGen
from pageObjects import LoginPage
from pageObjects.LoginPage import LoginPage
import os

class Test_Login():
    baseUrl=ReadConfig.getApplicationURL()
    logger=LogGen.loggen()

    user=ReadConfig.getUseremail()
    password=ReadConfig.getPassword()


    def test_login(self,setup):
        self.logger.info("User details input")
        self.driver=setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()

        self.hp=HomePage(self.driver)
        self.hp.clickMyAccount()
        self.hp.clickLogin()

        self.lp=LoginPage(self.driver)
        self.lp.setEmail(self.user)
        self.lp.setPassword(self.password)
        self.lp.clicklogin()

        self.targetpage=self.lp.isMyAccountPageExists()
        if self.targetpage==True:
            assert True
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir)+"\\screenshots\\"+"test_login.png")
            assert False










