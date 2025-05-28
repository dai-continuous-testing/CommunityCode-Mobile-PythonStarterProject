import unittest

from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

from test import base_test


class AndroidDemoTest(base_test.BaseTest):
    testName = 'Android Native Demo'
    driver = None

    def setUp(self):
        options = UiAutomator2Options()
        options.app = 'cloud:com.experitest.ExperiBank/.LoginActivity'
        options.appPackage = 'com.experitest.ExperiBank'
        options.appActivity = '.LoginActivity'
        options.set_capability('digitalai:accessKey', self.getAccessKey())
        options.set_capability('digitalai:testName', self.testName)
        options.set_capability('digitalai:deviceQuery', "@os='android'")
        options.set_capability('digitalai:appiumVersion', '2.18.0')
        self.driver = webdriver.Remote(self.getUrl(), options=options)

    def testAndroidNativeDemo(self):
        self.driver.find_element(By.ID, 'com.experitest.ExperiBank:id/usernameTextField').send_keys('company')
        self.driver.find_element(By.ID, 'com.experitest.ExperiBank:id/passwordTextField').send_keys('company')
        self.driver.find_element(By.ID, 'com.experitest.ExperiBank:id/loginButton').click()

        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.ID, 'com.experitest.ExperiBank:id/makePaymentButton')))

        self.driver.find_element(By.ID, 'com.experitest.ExperiBank:id/makePaymentButton').click()
        self.driver.find_element(By.ID, 'com.experitest.ExperiBank:id/phoneTextField').send_keys('1234567')
        self.driver.find_element(By.ID, 'com.experitest.ExperiBank:id/nameTextField').send_keys('Jon Snow')
        self.driver.find_element(By.ID, 'com.experitest.ExperiBank:id/amountTextField').send_keys('50')
        self.driver.find_element(By.ID, 'com.experitest.ExperiBank:id/countryTextField').send_keys('Switzerland')
        self.driver.find_element(By.ID, 'com.experitest.ExperiBank:id/sendPaymentButton').click()
        self.driver.find_element(By.ID, 'android:id/button1').click()

    def tearDown(self):
        report_url = self.driver.capabilities.get('reportUrl', 'N/A')
        print(f'Report URL: {report_url}')
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
