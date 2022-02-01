import unittest

class PaymentTest(unittest.TestCase):
    def test_paymentindollar(self):
        print("payment in dollar test")
        self.assertTrue(True)

    def test_paymentinrupee(self):
        print("payment in rupees")
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()