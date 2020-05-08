import unittest
import sys
sys.path.append('../')

from LoginTest.TC_Login import LoginTest
from LoginTest.TC_Signup import SignupTest

from PaymentTest.PaymentTest import PaymentTest
from PaymentTest.PaymentReturnsTest import PaymentReturnTest

#Get All Tests
TC1 = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
TC2 = unittest.TestLoader().loadTestsFromTestCase(SignupTest)
TC3 = unittest.TestLoader().loadTestsFromTestCase(PaymentTest)
TC4 = unittest.TestLoader().loadTestsFromTestCase(PaymentReturnTest)

#Creating Test Suites
Sanity_Test = unittest.TestSuite([TC1,TC2]) #Sanity Test Suite

functional_Test = unittest.TestSuite([TC3,TC4])

master_test = unittest.TestSuite([TC1,TC2,TC3,TC4])

unittest.TextTestRunner().run(master_test)

