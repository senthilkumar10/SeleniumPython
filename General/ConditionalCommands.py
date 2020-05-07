"""
Conditional Statements:- 

is_displayed()
is_enabled()
is_selected()
"""

from selenium import webdriver
import time
from pathlib import Path

driver = webdriver.Chrome(Path.joinpath(Path.cwd().parent,"drivers","chromedriver"))

driver.maximize_window()

driver.get("http://newtours.demoaut.com")

UserName_ele = driver.find_element_by_name("userName")

print(UserName_ele.is_displayed())

print(UserName_ele.is_enabled())

Password_ele = driver.find_element_by_name("password")

UserName_ele.send_keys("mercury")
Password_ele.send_keys("mercury")

driver.find_element_by_name("login").click()

time.sleep(5)

driver.quit()