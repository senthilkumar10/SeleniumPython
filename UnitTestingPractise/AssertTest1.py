import unittest
from pathlib import Path
from selenium import webdriver

class AssertTest1(unittest.TestCase):

    def test_google(self):
        self.driver = webdriver.Chrome(Path.joinpath(Path.cwd().parent,"drivers","chromedriver"))
        self.driver.get("https://www.google.com")
        titleName = self.driver.title
        self.assertEqual("Google",titleName,"The title is not equal")
        self.assertNotEqual("Google12",titleName)

        self.assertTrue(titleName,"Google")
        self.assertFalse(titleName,"Google12")


if __name__ == "__main__":
    unittest.main()