from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    username_xpath = "//input[@placeholder='Username']"
    password_xpath = "//input[@placeholder='Password']"
    login_button_xpath = "//button[normalize-space()='Login']"

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.wait = WebDriverWait(self.driver, 10)
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.username_xpath))).clear()
        self.driver.find_element(By.XPATH, self.username_xpath).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.password_xpath).clear()
        self.driver.find_element(By.XPATH, self.password_xpath).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()