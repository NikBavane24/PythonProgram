import time

from selenium_SSO.Page_Object.LoginPage_SSO import LoginPage


def test_e2e(browserInstance):
    driver=browserInstance

    loginPage = LoginPage(driver)
    users_page=loginPage.Login()
    users_page.Users()


    time.sleep(20)