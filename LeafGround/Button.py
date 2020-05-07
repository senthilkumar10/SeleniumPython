from selenium import webdriver
from pathlib import Path
import time
from selenium.webdriver.support.color import Color


driver = webdriver.Chrome(Path.joinpath(Path.cwd().parent,"drivers","chromedriver"))

driver.maximize_window()

driver.get("http://www.leafground.com/")   

driver.find_element_by_xpath("//a[@href='pages/Button.html']").click()

time.sleep(2)

driver.find_element_by_id("home").click()

driver.find_element_by_xpath("//a[@href='pages/Button.html']").click()

print(driver.find_element_by_id("position").location)

print(driver.find_element_by_id("color").value_of_css_property("background-color"))

print(driver.find_element_by_id("size").size)



driver.quit()