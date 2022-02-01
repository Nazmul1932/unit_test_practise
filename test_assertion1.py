import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

class Test(unittest.TestCase):
    def test_name(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://www.google.com/")
        title_of_page = driver.title
        # self.assertEqual("Google", title_of_page, "title is not same")
        self.assertNotEqual("Google123", title_of_page)

if __name__ == "__main__":
    unittest.main()