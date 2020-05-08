import unittest

def setUpModule():
    print("Setup Module")

def tearDownModule():
    print("Tear Down Module")

class AppTesting(unittest.TestCase):

    def test_search(self):
        print("This is search method")

    def test_advancesearch(self):
        print("This is Advance Search")

    def test_Prepaid(self):
        print("This is Prepaid Search")

    def test_Postpaid(self):
        print("This is Postpaid search")

    def setUp(self):
        print("This is a Login Test")

    def tearDown(self):
        print("This is a logout test")

    @classmethod
    def setUpClass(cls):
        print("Open Application")

    @classmethod
    def tearDownClass(cls):
        print("Close Application")



if __name__ == "__main__":
    unittest.main()