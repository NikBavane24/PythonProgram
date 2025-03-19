import time
from slenium_MIQ.page_object.Login_page import LoginPage

def test_e2emeeting(browserInstance):
    driver=browserInstance

    loginPage=LoginPage(driver)
    dashboard_page=loginPage.Login()
    createMeeting_page=dashboard_page.Dashboard()
    report_page=createMeeting_page.Meeting()
    report_page.Report()
    dashboard_page.report_search()
    createMeeting_page.meetingSearch()
    createMeeting_page.updateMeeting()
    #createMeeting_page.deleteMeeting()
    report_page.reportSearch()
    cesGoldArchive_page=report_page.updateReport()
    meetingTypes_page=cesGoldArchive_page.goldArchiveReportSearch()
    meetingTypes_page.createMeetingType()
    meetingTypes_page.createMeetingSubtype()
    meetingTypes_page.updateMeetingType()
    meetingTypes_page.updateMeetingSubType()



    time.sleep(5)