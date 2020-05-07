from selenium import webdriver
from pathlib import Path
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(Path.joinpath(Path.cwd().parent, "drivers", "chromedriver"))

driver.maximize_window()

driver.get("http://www.leafground.com/")

driver.find_element_by_xpath("//img[@src='images/dropdown.png']").click()

time.sleep(2)

drp1 = Select(driver.find_element_by_id("dropdown1"))

#Select Training program using index
drp1.select_by_index(1)

#Select Traiing Program using Text
Select(driver.find_element_by_name("dropdown2")).select_by_visible_text("Appium")

#Select Training program using Value
Select(driver.find_element_by_id("dropdown3")).select_by_value("3")


#Get the number of dropdown options
total_options = driver.find_elements_by_xpath("//select[@class='dropdown']/option")

print("Total Number of options :- "+ str(len(total_options)))

#use sendKeys to select
dropdown_ele = driver.find_element_by_xpath("(//select)[5]")
dropdown_ele.click()
for i in range(1,5):
    dropdown_ele.send_keys(Keys.ARROW_DOWN)

dropdown_ele.click()


Select(driver.find_element_by_xpath("(//select)[6]")).select_by_value("2")

time.sleep(2)
driver.quit()
