from pageobjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class TestLogin:
    baseURL = ReadConfig.getAppURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_login(self, setup):
        self.logger.info("*** Test for login starting ***")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.login = LoginPage(self.driver)
        self.login.setUserName(self.username)
        self.login.setPassword(self.password)
        self.login.clickLogin()
        self.actualTitle = self.driver.title
        self.expectedTitle = "OrangeHRM"
        if self.actualTitle == self.expectedTitle:
            assert True
            self.driver.close()
            self.logger.info("*** Test Case Passed ***")
            self.logger.info("*** Title successfully matched ***")
        else:
            self.driver.save_screenshot("./screenshots/" + "login_failed.png")
            self.driver.close()
            self.logger.info("*** Test Case Failed ***")
            self.logger.error("*** Title does not match ***")
            assert False
