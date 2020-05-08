import unittest

class SignupTest(unittest.TestCase):

    def test_SignByEmail(self):
        print("Sign in by Email Test")
        self.assertTrue(True)

    def test_SignByTwitter(self):
        print("Sign in by Twitter Test")
        self.assertTrue(True)

    def test_SignByFB(self):
        print("Sign in by Face Book Test")
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
