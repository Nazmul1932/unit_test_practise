import unittest
from Package1.test_loginTest import LoginTest
from Package1.test_signupTest import SignupTest
from Package2.test_paymentTest import PaymentTest
from Package2.test_paymentResturnsTest import PaymentReturnsTest

test_case1 = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
test_case2 = unittest.TestLoader().loadTestsFromTestCase(SignupTest)
test_case3 = unittest.TestLoader().loadTestsFromTestCase(PaymentTest)
test_case4 = unittest.TestLoader().loadTestsFromTestCase(PaymentReturnsTest)

sanity_test_suite = unittest.TestSuite([test_case1, test_case2])
functional_test_suite = unittest.TestSuite([test_case3, test_case4])
master_test_suite = unittest.TestSuite([test_case1, test_case2, test_case3, test_case4])


unittest.TextTestRunner(verbosity=2).run(master_test_suite)