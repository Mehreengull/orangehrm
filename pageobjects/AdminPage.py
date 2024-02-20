from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class AdminPage:
    admin_menu_link = "//aside[@class='oxd-sidepanel']//li[1]"
    add_new_xpath = "//button[normalize-space()='Add']"
    employee_name_xpath = "//input[@placeholder='Type for hints...']"
    user_status_xpath = "//div[contains(text(),'-- Select --')]"
    admin_role_xpath = "//span[contains(text(),'Admin')]"
    enabled_xpath = "//span[normalize-space()='Enabled']"
    username_xpath = "(//input[@class='oxd-input oxd-input--active'])[2]"
    password_xpath = "(//input[@type='password'])[1]"
    confirm_password_xpath = "(//input[@type='password'])[2]"
    save_cta_xpath = "//button[normalize-space()='Save']"
    success_toast_xpath = "//div[@id='oxd-toaster_1']"
    employee_select_xpath = "//span[contains(text(),'Ranga')]"

    def __init__(self, driver):
        self.driver = driver

    def clickAdminMenu(self):
        self.driver.find_element(By.XPATH, self.admin_menu_link).click()

    def clickAddNew(self):
        self.wait = WebDriverWait(self.driver, 10)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.add_new_xpath))).click()

    def SetEName(self, employeeName):
        element = self.driver.find_element(By.XPATH, self.employee_name_xpath)
        element.send_keys(employeeName)
        self.wait = WebDriverWait(self.driver, 10)
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.employee_select_xpath))).click()

    def SetUserRole(self):
        self.wait = WebDriverWait(self.driver, 10)
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.user_status_xpath))).click()
        self.driver.find_element(By.XPATH, self.admin_role_xpath).click()

    def SetUserStatus(self):
        self.wait = WebDriverWait(self.driver, 10)
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.user_status_xpath))).click()
        self.driver.find_element(By.XPATH, self.enabled_xpath).click()

    def SetUserName(self, username):
        self.driver.find_element(By.XPATH, self.username_xpath).send_keys(username)

    def SetPassword(self, password):
        self.driver.find_element(By.XPATH, self.password_xpath).send_keys(password)

    def SetConfirmPassword(self, password):
        self.driver.find_element(By.XPATH, self.confirm_password_xpath).send_keys(password)

    def SaveInfo(self):
        self.driver.find_element(By.XPATH, self.save_cta_xpath).click()

    def ToastPresent(self):
        element = self.driver.find_element(By.XPATH, self.success_toast_xpath)
        return element.text
