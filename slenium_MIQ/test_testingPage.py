import time

from slenium_MIQ.page_object import meetingTypes_page
from slenium_MIQ.page_object.Login_page import LoginPage


def test_topicPage(browserInstance):
    driver=browserInstance

    loginPage=LoginPage(driver)
    meetingTypes_page=loginPage.Login()
    meetingTypes_page.createMeetingType()
    #meetingTypes_page.updateMeetingSubType()
    #meetingTypes_page.updateMeetingType()
    #meetingTypes_page.updateMeetingSubType()




    time.sleep(5)

