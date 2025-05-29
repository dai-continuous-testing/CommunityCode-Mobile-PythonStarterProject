import configparser
import unittest
import urllib.parse


class BaseTest(unittest.TestCase):
    config = configparser.ConfigParser()
    config.read('cloud.properties')

    def getUrl(self):
        url = self.config.get('cloud', 'url')
        return urllib.parse.urljoin(url, '/wd/hub')

    def getAccessKey(self):
        return self.config.get('cloud', 'accessKey')

    def getProperty(self, property_name: str):
        return self.config.get('cloud', property_name)


if __name__ == '__main__':
    unittest.main()
