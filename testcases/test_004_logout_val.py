# "1. Click on 'My Account' Dropmenu
# 2. Select 'Logout' option (Verify ER-1)
# 3. Click on 'Continue' button (Verify ER-2)"
# "1. Click on 'Logout' option from the Right Column  (Verify ER-1)
# 2. Click on 'Continue' button (Verify ER-2)"
import os
from pageObjects.MyAccountPage import MyAccountPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_Logout_val():
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()

    path = os.path.abspath(os.curdir) + "\\testdata\\Opencart_LoginData.xlsx"

    def test_logout(self, setup, login):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = login
        self.ma = MyAccountPage(self, driver)
        self.ma.clickLogout()
        assert not self.lp.isMyAccountPageExists()

        self.driver.close()
