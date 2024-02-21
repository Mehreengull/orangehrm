import time

from pageobjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageobjects.AdminPage import AdminPage
from pageobjects.SearchAdminPage import SearchAdminPage


class TestSearchAdmin:
    baseURL = ReadConfig.getAppURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_admin_search_name(self, setup):
        self.logger.info("*** Test for login starting ***")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.login = LoginPage(self.driver)
        self.login.setUserName(self.username)
        self.login.setPassword(self.password)
        self.login.clickLogin()
        time.sleep(5)
        self.logger.info("*** Redirecting to Admin page ***")
        self.ap = AdminPage(self.driver)
        self.ap.clickAdminMenu()
        self.logger.info("*** Searching Admin page ***")
        self.sa = SearchAdminPage(self.driver)
        self.sa.typeInputInSearch("Admin")
        self.sa.clickSearch()
        search_result = self.sa.matchResults()
        if search_result == "Admin":
            assert True
            self.logger.info("*** Search result matched ***")
            self.driver.close()
        else:
            self.driver.save_screenshot("./screenshots/" + "admin_search.png")
            self.logger.error("*** Search result mis matched ***")
            self.driver.close()
            assert False
