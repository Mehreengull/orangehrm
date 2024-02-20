import time

from pageobjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageobjects.AdminPage import AdminPage
import random
import string


class TestRegistration:
    baseURL = ReadConfig.getAppURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_admin_reg(self, setup):
        self.logger.info("*** Test for login starting ***")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.login = LoginPage(self.driver)
        self.login.setUserName(self.username)
        self.login.setPassword(self.password)
        self.login.clickLogin()
        time.sleep(5)
        self.logger.info("*** Test for admin registration starting ***")
        self.ap = AdminPage(self.driver)
        self.ap.clickAdminMenu()
        self.ap.clickAddNew()
        self.ap.SetUserRole()
        self.ap.SetUserStatus()
        self.ap.SetEName("Ra")
        self.ap.SetUserName("Test " + random_generator())
        password = random_generator()
        self.ap.SetPassword(password)
        self.ap.SetConfirmPassword(password)
        self.ap.SaveInfo()
        time.sleep(3)
        toast_text = self.ap.ToastPresent()
        expected_text = "Successfully Saved"
        if expected_text in toast_text:
            assert True
            self.driver.close()
            self.logger.info("*** Test Case Passed ***")
            self.logger.info("*** Admin successfully added ***")
        else:
            self.driver.save_screenshot("./screenshots/" + "registration_failed.png")
            self.driver.close()
            self.logger.info("*** Test Case Failed ***")
            self.logger.error("*** Message does not match ***")
            assert False


def random_generator(alp=5, dig=3, chars=string.digits, s_letters=string.ascii_letters):
    digits = ''.join(random.choice(chars) for x in range(dig))
    alphabets = ''.join(random.choice(s_letters) for x in range(alp))
    return digits + alphabets
