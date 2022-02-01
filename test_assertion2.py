import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

class Test(unittest.TestCase):
    def test_name(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://www.google.com/")
        title_of_page = driver.title
        # self.assertTrue(title_of_page == "Google")
        self.assertFalse(title_of_page != "Google")

if __name__ == "__main__":
    unittest.main()