import unittest

class AppTesting(unittest.TestCase):

    @unittest.SkipTest
    def test_search(self):
        print("this is search test")

    @unittest.skip("sorry ai test apatoto ami run koraite chai na, tmr kono problem")
    def test_advanced_search(self):
        print("this is advanced search test")

    @unittest.skipIf(1!=1, "numbers are not equal")
    def test_prepaid_search(self):
        print("this is prepaid search test")

    def test_postpaid_search(self):
        print("this is postpaid search test")

    def test_loginbygmail(self):
        print("login by gmail")

    def test_loginbytwitter(self):
        print("login by twitter")


if __name__ == "__main__":
    unittest.main()