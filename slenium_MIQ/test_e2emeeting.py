import time
from slenium_MIQ.page_object.Login_page import LoginPage

def test_e2emeeting(browserInstance):
    driver=browserInstance

    loginPage=LoginPage(driver)
    dashboard_page=loginPage.Login()
    createMeeting_page=dashboard_page.Dashboard()
    createReport_page=createMeeting_page.Meeting()
    createReport_page.Report()
    dashboard_page.report_search()
    createMeeting_page.meetingSearch()
    createMeeting_page.updateMeeting()

    createReport_page.reportSearch()
    createReport_page.updateReport()
    createReport_page.reportDelete()
    cesGoldArchive_page=createMeeting_page.meetingDelete()
    meetingTypes_page=cesGoldArchive_page.goldArchiveReportSearch()
    meetingTypes_page.createMeetingType()
    meetingTypes_page.createMeetingSubtype()
    meetingTypes_page.updateMeetingType()
    topic_page=meetingTypes_page.updateMeetingSubType()
    topic_page.createTopic()
    topic_page.updateTopic()
    topic_page.TopicDelete()



    time.sleep(5)