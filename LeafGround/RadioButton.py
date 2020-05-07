from selenium import webdriver
from pathlib import Path
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(Path.joinpath(Path.cwd().parent, "drivers", "chromedriver"))

driver.maximize_window()

driver.get("http://www.leafground.com/")

driver.find_element_by_xpath("//img[@src='images/radio.png']").click()

time.sleep(2)

#Click the Yes button
driver.find_element_by_id("yes").click()

#Find default selected radio button
radio_buttons= driver.find_elements_by_name("news")

for each_radio_btn in radio_buttons:
    print(each_radio_btn.is_selected())






time.sleep(2)
driver.quit()
