import unittest

class AssetTestWithCollection(unittest.TestCase):

    def test(self):
        list = {"Python","Selenium","Java"}
        self.assertIn("Python",list)

if __name__ == "__main__":
    unittest.main()