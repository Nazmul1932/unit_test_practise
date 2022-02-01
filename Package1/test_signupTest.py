import unittest

class SignupTest(unittest.TestCase):
    def test_signupbyemail(self):
        print("email test sign up")
        self.assertTrue(True)

    def test_signupbyfacebook(self):
        print("facebook test sign up")
        self.assertTrue(True)

    def test_signupytwitter(self):
        print("twitter test sign up")
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()