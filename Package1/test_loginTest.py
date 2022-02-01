import unittest

class LoginTest(unittest.TestCase):
    def test_loginbyemail(self):
        print("email test login")
        self.assertTrue(True)

    def test_loginbyfacebook(self):
        print("facebook test login")
        self.assertTrue(True)

    def test_loginbytwitter(self):
        print("twitter test login")
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()