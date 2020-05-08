import unittest

class AppTest(unittest.TestCase):

    @unittest.SkipTest
    def test_search(self):
        print("This is search method")

    @unittest.skip("Skipping this test because it is not ready")
    def test_advancesearch(self):
        print("This is Advance Search")

    @unittest.skipIf(1==1,"Skip is the condition satisfy")
    def test_Prepaid(self):
        print("This is Prepaid Search")

    def test_Postpaid(self):
        print("This is Postpaid search")

    def test_login_by_gmail(self):
        print("This is login by gmail")

    def test_login_by_twitter(self):
        print("This is login by twitter")


if __name__ == "__main__":
    unittest.main()