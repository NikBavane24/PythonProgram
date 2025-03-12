import time

from slenium_MIQ.page_object.Login_page import LoginPage


def test_e2emeeting(browserInstance):
    driver=browserInstance

    loginPage=LoginPage(driver)
    dashboard_page=loginPage.Login()
    createMeeting_page=dashboard_page.Dashboard()
    createMeeting_page.Meeting()

    time.sleep(5)