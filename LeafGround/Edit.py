from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from pathlib import Path


driver = webdriver.Chrome(Path.joinpath(Path.cwd().parent,"drivers","chromedriver"))

driver.maximize_window()

driver.get("http://www.leafground.com/")   

driver.find_element_by_xpath("//img[@src='images/edit.png']").click()

time.sleep(2)

driver.find_element_by_id("email").send_keys("ss@ss.com")

append_ele = driver.find_element_by_xpath("//input[@value='Append ']")

append_ele.send_keys(" This is Appended Text.")

append_ele.send_keys(Keys.TAB)

print("Text in the 3rd Text Box :- "+driver.find_element_by_name("username").get_attribute("value"))

driver.find_element_by_xpath("//input[@value='Clear me!!']").clear()

status = driver.find_element_by_xpath("//input[@disabled='true']").is_enabled()

assert status is False

driver.quit()
