# "1. Click on 'My Account' Dropmenu
# 2. Select 'Logout' option (Verify ER-1)
# 3. Click on 'Continue' button (Verify ER-2)"
# "1. Click on 'Logout' option from the Right Column  (Verify ER-1)
# 2. Click on 'Continue' button (Verify ER-2)"
from utilities.readProperties import ReadConfig
import os
from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen
import pytest
from pageObjects.MyAccountPage import MyAccountPage
class Test_LogOut_val():
    baseUrl = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()

    user = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    def test_LG_001(self,setup,login):

        self.driver=setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()

        self.lp=login
        self.ma=MyAccountPage(self.driver)
        self.lg=LoginPage(self.driver)
        assert self.lg.isMyAccountPageExists
        self.logger.info("login successfully")
        self.ma.clickLogout()
        self.logger.info("logout successfully")
        assert "logout" in self.driver.current_url.lower()
        self.logger.info("logout successfully")
        self.driver.quit()

    def test_LG_002(self,setup,login):
        self.driver=setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
#28 95
        self.lg=login
        self.ma=MyAccountPage(self.driver)
        self.ma.clickLogout()
        self.logger.info("login successfully")
        self.driver.quit()

