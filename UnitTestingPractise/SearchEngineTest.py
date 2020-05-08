import unittest
from pathlib import Path
from selenium import webdriver

class SearchEngineTest(unittest.TestCase):
    def test_google(self):
        self.driver = webdriver.Chrome(Path.joinpath(Path.cwd().parent,"drivers","chromedriver"))
        self.driver.get("https://www.google.com")
        print("Title of the page :"+self.driver.title)

    def test_bing(self):
        self.driver = webdriver.Chrome(Path.joinpath(Path.cwd().parent,"drivers","chromedriver"))
        self.driver.get("https://www.bing.com")
        print("Title of the page :"+self.driver.title)
        

if __name__ == "__main__":
    unittest.main()