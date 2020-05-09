import unittest
import HtmlTestRunner
from selenium import webdriver
import time
import sys
sys.path.append('../')
from PageObjects.LoginPage import LoginPage
from pathlib import Path

class LoginTest(unittest.TestCase):
    baseURL = "https://admin-demo.nopcommerce.com/"
    userName = "admin@yourstore.com"
    password = "admin"
    driver = webdriver.Chrome(Path.joinpath(Path.cwd().parent.parent,"drivers","chromedriver"))

    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.baseURL)
        cls.driver.maximize_window()

    def test_login(self):
        lp = LoginPage(self.driver)
        lp.setUserName(self.userName)
        lp.setPassword(self.password)
        lp.clickLogin()
        time.sleep(2)
        self.assertEqual("Dashboard / nopCommerce administration",self.driver.title,"Webpage title is not matching")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=Path.joinpath(Path.cwd().parent,"Reports")))
    