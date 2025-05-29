import unittest

from appium import webdriver
from appium.options.ios import XCUITestOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

from test import base_test


class LocalIosTest(base_test.BaseTest):
    testName = 'iOS Web Demo'
    driver = None

    def setUp(self):
        super().setUp()
        options = XCUITestOptions()
        options.browser_name = 'Safari'
        options.set_capability('digitalai:accessKey', self.getAccessKey())
        options.set_capability('digitalai:testName', self.testName)
        options.set_capability('digitalai:deviceQuery', "@os='ios'")
        options.set_capability('digitalai:appiumVersion', "2.18.0")
        self.driver = webdriver.Remote(self.getUrl(), options=options)

    def testIosWebDemo(self):
        self.driver.implicitly_wait(10)
        self.driver.get('https://demo-bank.ct.digital.ai')
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.ID, 'login')))
        self.driver.find_element(By.XPATH, "//*[@data-auto='username']//input").send_keys('company')
        self.driver.find_element(By.XPATH, "//*[@data-auto='password']//input").send_keys('company')
        self.driver.find_element(By.XPATH, "//*[@data-auto='login']").click()
        self.driver.find_element(By.XPATH, "//*[@data-auto='transfer-funds']").click()
        self.driver.find_element(By.XPATH, "//input[@name='NAME']").send_keys('John')
        self.driver.find_element(By.XPATH, "//input[@name='PHONE']").send_keys('1-234-5678')
        self.driver.find_element(By.XPATH, "//input[@name='AMOUNT']").send_keys('1000')
        self.driver.find_element(By.XPATH, "//*[@data-auto='country']").click()
        self.driver.find_element(By.XPATH, "//*[text()='India']").click()
        self.driver.find_element(By.XPATH, "//*[@data-auto='transfer-button']").click()

    def tearDown(self):
        report_url = self.driver.capabilities.get('reportUrl', 'N/A')
        print(f'Report URL: {report_url}')
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
