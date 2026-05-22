from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from datetime import datetime
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
import os
import pytest


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def setup(request):

    browser = request.config.getoption("--browser")

    if browser == "chrome":
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

    elif browser == "firefox":
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)

    elif browser == "edge":
        service = EdgeService(EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=service)

    else:
        raise ValueError("Browser not supported")

    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture()
def login(setup):
    driver=setup
    driver.get(ReadConfig.getApplicationURL())


    hp = HomePage(driver)
    hp.clickMyAccount()
    hp.clickLogin()

    lp = LoginPage(driver)
    lp.setEmail(ReadConfig.getUseremail())
    lp.setPassword(ReadConfig.getPassword())
    lp.clicklogin()

    return lp


###################pytest HTML Report#######
# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'Opencart'
    config._metadata['Module Name'] = 'CustRegistration'
    config._metadata['Tester'] = 'Teja'

# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)

#Specifying report folder location and save report with timestamp
@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.option.htmlpath = os.path.abspath(os.curdir)+"\\reports\\"+datetime.now().strftime("%d-%m-%Y %H-%M-%S")+".html"


class ReadConfig:
    pass