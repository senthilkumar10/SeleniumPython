from selenium import webdriver
from selenium.webdriver import ActionChains
from pathlib import Path
import time

driver = webdriver.Chrome(Path.joinpath(Path.cwd().parent, "drivers", "chromedriver"))

driver.maximize_window()

driver.get("http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")

actions = ActionChains(driver)

#Source Elements
Oslo = driver.find_element_by_id("box1")
Stockholm = driver.find_element_by_id("box2")
Washington = driver.find_element_by_id("box3")
Copenhagen = driver.find_element_by_id("box4")
Seoul = driver.find_element_by_id("box5")
Rome = driver.find_element_by_id("box6")
Madrid = driver.find_element_by_id("box7")

#Target Elements
Italy = driver.find_element_by_id("box106")
Spain = driver.find_element_by_id("box107")
Norway = driver.find_element_by_id("box101")
Denmark = driver.find_element_by_id("box104")
South_Korea = driver.find_element_by_id("box105")
Sweden = driver.find_element_by_id("box102")
United_States = driver.find_element_by_id("box103")

actions.drag_and_drop(Oslo,Norway).perform()
actions.drag_and_drop(Stockholm,Sweden).perform()
actions.drag_and_drop(Washington,United_States).perform()
actions.drag_and_drop(Copenhagen,Denmark).perform()
actions.drag_and_drop(Seoul,South_Korea).perform()
actions.drag_and_drop(Rome,Italy).perform()
actions.drag_and_drop(Madrid,Spain).perform()

time.sleep(2)
driver.quit()