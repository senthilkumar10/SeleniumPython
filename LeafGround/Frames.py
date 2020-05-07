from selenium import webdriver
from pathlib import Path
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(Path.joinpath(Path.cwd().parent, "drivers", "chromedriver"))

driver.maximize_window()

driver.get("http://www.leafground.com/")

driver.find_element_by_xpath("//img[@src='images/frame.png']").click()

time.sleep(2)

#Switch to Frame using WebElement

driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@src='default.html']"))
driver.find_element_by_id("Click").click()
driver.switch_to.default_content()

#Switch to Frame using index
driver.switch_to.frame(1) 
driver.switch_to.frame(0) #Going to the nested Frame
driver.find_element_by_id("Click1").click()
driver.switch_to.default_content()

#Find the total number of Frames
print("The Total Number of Frames - "+str(len(driver.find_elements_by_xpath("//iframe"))))

time.sleep(2)
driver.quit()




