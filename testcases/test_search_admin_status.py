import time

from pageobjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageobjects.AdminPage import AdminPage
from pageobjects.SearchAdminPage import SearchAdminPage


class TestSearchAdminStatus:
    baseURL = ReadConfig.getAppURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_admin_search_status(self, setup):
        self.logger.info("*** Test for login starting ***")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.login = LoginPage(self.driver)
        self.login.setUserName(self.username)
        self.login.setPassword(self.password)
        self.login.clickLogin()
        time.sleep(5)
        self.logger.info("*** Redirecting to Admin Status ***")
        self.ap = AdminPage(self.driver)
        self.ap.clickAdminMenu()
        self.logger.info("*** Searching Admin page ***")
        self.sa = SearchAdminPage(self.driver)
        self.sa.selectStatus()
        self.sa.clickSearch()
        time.sleep(4)
        status_result = self.sa.matchStatusResult()
        self.logger.info("*** Total Records fond: %s", len(status_result))
        expected_status = "Enabled"
        for i in status_result:
            if i == expected_status:
                assert True
                self.logger.info("*** Admin status matched")
            else:
                self.driver.save_screenshot("./screenshots/"+"admin_status.png")
                self.logger.error("Admin status mismatched")
                assert False
        self.driver.close()


