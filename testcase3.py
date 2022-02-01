import unittest

def setUpModule():
    print("setUpModule")

def tearDownModule():
    print("tearDownModule")

class AppTesting(unittest.TestCase):

    @classmethod
    def setUp(self): # setup class execute hoi every method er age
        print("this is setup")

    @classmethod
    def tearDown(self): #every method er por ai method call hoi
        print("this is tear down")

    @classmethod
    def setUpClass(self): # ai method call hoi only once mne every class e akbar call hbe
        print("set up class")

    @classmethod
    def tearDownClass(self): # ai method call hoi shobar seshe mne jokhon class er shob method execute houa sesh tokhon
        print("tear down class")

    def test_search(self):
        print("this is search test")

    def test_advanced_search(self):
        print("this is advanced search test")

    def test_prepaid_search(self):
        print("this is prepaid search test")

    def test_postpaid_search(self):
        print("this is postpaid search test")


if __name__ == "__main__":
    unittest.main()
