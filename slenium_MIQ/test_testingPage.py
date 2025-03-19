import time

from slenium_MIQ.page_object import meetingTypes_page
from slenium_MIQ.page_object.Login_page import LoginPage


def test_topicPage(browserInstance):
    driver=browserInstance

    loginPage=LoginPage(driver)
    topic_page=loginPage.Login()
    topic_page.createTopic()
    topic_page.updateTopic()
    topic_page.TopicDelete()




    time.sleep(5)

