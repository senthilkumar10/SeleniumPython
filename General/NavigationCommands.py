from selenium import webdriver
import time

from pathlib import Path

driver = webdriver.Chrome(Path.joinpath(Path.cwd().parent,"drivers","chromedriver"))
driver.maximize_window()

driver.get("http://www.leafground.com/")  

print(driver.title)

time.sleep(2)

driver.find_element_by_xpath("//img[@src='images/edit.png']").click()

print(driver.title)
time.sleep(2)

driver.back()

print(driver.title)
time.sleep(2)

driver.forward()

print(driver.title)
time.sleep(2)


driver.quit()