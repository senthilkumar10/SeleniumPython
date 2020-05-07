from selenium import webdriver
from pathlib import Path
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(Path.joinpath(Path.cwd().parent, "drivers", "chromedriver"))

driver.maximize_window()

driver.get("http://www.leafground.com/")

driver.find_element_by_xpath("//img[@src='images/checkbox.png']").click()

time.sleep(2)

#Select the Languages that you know
for i in range(1,4):
    driver.find_element_by_xpath("(//input[@type='checkbox'])["+str(i)+"]").click()

#Confirm Selenium is checked
check_box_selection = driver.find_element_by_xpath("//div[text()='Selenium']/input").is_selected()
assert check_box_selection is True

#DeSelect only checked
for i in range(7,9):
    status = driver.find_element_by_xpath("(//div/input)["+str(i)+"]").is_selected()
    if status:
        driver.find_element_by_xpath("(//div/input)["+str(i)+"]").click()


#Select all the checkbox
for i in range(9,14):
    driver.find_element_by_xpath("(//div/input)["+str(i)+"]").click()

time.sleep(2)
driver.quit()
