import unittest

from appium import webdriver
from appium.options.ios import XCUITestOptions
from selenium.webdriver.common.by import By

from test import base_test


class IosDemoTest(base_test.BaseTest):
    testName = 'iOS Native Demo'
    driver = None

    def setUp(self):
        super().setUp()
        options = XCUITestOptions()
        options.app = 'cloud:com.experitest.ExperiBank'
        options.bundleId = 'com.experitest.ExperiBank'
        options.set_capability('digitalai:accessKey', self.getAccessKey())
        options.set_capability('digitalai:testName', self.testName)
        options.set_capability('digitalai:deviceQuery', "@os='ios'")
        options.set_capability('digitalai:appiumVersion', "2.18.0")
        self.driver = webdriver.Remote(self.getUrl(), options=options)

    def testIosNativeDemo(self):
        self.driver.find_element(By.XPATH, "//*[@name='usernameTextField']").send_keys('company')
        self.driver.find_element(By.XPATH, "//*[@name='passwordTextField']").send_keys('company')
        self.driver.find_element(By.XPATH, "//*[@name='loginButton']").click()
        self.driver.find_element(By.XPATH, "//*[@name='makePaymentButton']").click()
        self.driver.find_element(By.XPATH, "//*[@name='phoneTextField']").send_keys('1234567')
        self.driver.find_element(By.XPATH, "//*[@name='nameTextField']").send_keys('Jon Snow')
        self.driver.find_element(By.XPATH, "//*[@name='amountTextField']").send_keys('50')
        self.driver.find_element(By.XPATH, "//*[@name='countryButton']").click()
        self.driver.find_element(By.XPATH, "//*[@name='Switzerland']").click()
        self.driver.find_element(By.XPATH, "//*[@name='sendPaymentButton']").click()
        self.driver.find_element(By.XPATH, "//*[@name='Yes']").click()

    def tearDown(self):
        report_url = self.driver.capabilities.get('reportUrl', 'N/A')
        print(f'Report URL: {report_url}')
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
