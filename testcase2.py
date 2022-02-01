import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


class SearchEngineTest(unittest.TestCase):
    def test_google(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("https://www.google.com/")
        print("title of google: " + self.driver.title)
        self.driver.close()

    def test_bing(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("https://bing.com/")
        print("title of bing: " + self.driver.title)
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
