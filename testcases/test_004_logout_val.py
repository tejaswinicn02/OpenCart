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

    def test_LG_001(self, setup, login):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()

        self.lp = login
        self.ma = MyAccountPage(self.driver)
        self.lg = LoginPage(self.driver)
        assert self.lg.isMyAccountPageExists()
        self.logger.info("login successfully")
        self.ma.clickLogout()
        self.logger.info("logout successfully")
        assert "logout" in self.driver.current_url.lower()
        self.logger.info("logout successfully")
        self.driver.quit()

    # def test_TC_LG_003(self, setup, login):
    #     self.driver = setup
    #     self.driver.get(self.baseUrl)
    #     self.driver.maximize_window()
    #
    #     self.lp = login
    #     self.ma = MyAccountPage(self.driver)
    #     self.lg = LoginPage(self.driver)
    #
    #     # Verify login successful
    #     assert self.lg.isMyAccountPageExists()
    #     self.logger.info("User logged in successfully")
    #
    #     # Save cookies
    #     cookies = self.driver.get_cookies()
    #
    #     # Close browser without logout
    #     self.driver.quit()
    #     self.logger.info("Browser closed without logout")
    #
    #     # Reopen browser
    #     self.driver = setup
    #     self.driver.get(self.baseUrl)
    #
    #     # Restore cookies
    #     for cookie in cookies:
    #         self.driver.add_cookie(cookie)
    #
    #     # Refresh page
    #     self.driver.refresh()
    #     time.sleep(3)
    #
    #     # Verify session maintained
    #     assert self.lg.isMyAccountPageExists()
    #     self.logger.info("Session maintained after reopening browser")
    #
    #     self.driver.quit()
