import pickle
from pageObjects.MyAccountPage import MyAccountPage
from utilities.readProperties import ReadConfig

def test_restore_session(setup):

    driver = setup
    driver.get(ReadConfig.getApplicationURL())

    # LOAD SESSION
    with open("cookies.pkl", "rb") as f:
        cookies = pickle.load(f)

    for cookie in cookies:
        driver.add_cookie(cookie)

    driver.refresh()

    ma = MyAccountPage(driver)

    assert ma.isMyAccountPageExists(), "Session expired - user not logged in"