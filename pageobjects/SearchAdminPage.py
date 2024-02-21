import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SearchAdminPage:
    search_input_xpath = "(//input[@class='oxd-input oxd-input--active'])[2]"
    search_cta_xpath = "//button[normalize-space()='Search']"
    match_result_xpath = "//div[@class='oxd-table-card']//div[2]//div[1]"
    status_xpath = "(//div[@class='oxd-select-text oxd-select-text--active'])[2]"
    status_enabled_xpath = "//span[normalize-space()='Enabled']"
    reset_xpath = "//button[normalize-space()='Reset']"
    status_results_xpath = "//div[contains(text(),'Enabled')]"

    def __init__(self, driver):
        self.driver = driver

    def typeInputInSearch(self, search):
        self.wait = WebDriverWait(self.driver, 10)
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.search_input_xpath))).send_keys(search)

    def clickSearch(self):
        self.driver.find_element(By.XPATH, self.search_cta_xpath).click()

    def matchNameResults(self):
        self.wait = WebDriverWait(self.driver, 10)
        element = self.wait.until(EC.presence_of_element_located((By.XPATH, self.match_result_xpath)))
        return element.text

    def selectStatus(self):
        self.wait = WebDriverWait(self.driver, 10)
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.status_xpath))).click()
        self.driver.find_element(By.XPATH, self.status_enabled_xpath).click()

    def matchStatusResult(self):
        elements = self.driver.find_elements(By.XPATH, self.status_results_xpath)
        text_list = [e.text for e in elements]
        return text_list[1:]  # exclude 1st element
