import unittest

class LoginTest(unittest.TestCase):

    def test_LoginByEmail(self):
        print("Logged in by Email Test")
        self.assertTrue(True)

    def test_LoginByTwitter(self):
        print("Logged in by Twitter Test")
        self.assertTrue(True)

    def test_LoginByFB(self):
        print("Logged in by Face Book Test")
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
