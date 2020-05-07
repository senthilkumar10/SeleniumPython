from selenium import webdriver
from selenium.webdriver import ActionChains
from pathlib import Path
import time

driver = webdriver.Chrome(Path.joinpath(Path.cwd().parent, "drivers", "chromedriver"))

driver.maximize_window()

driver.get("http://www.leafground.com/")

driver.find_element_by_xpath("//img[@src='./images/mouseOver.png']").click()

time.sleep(2)

testleaf_courses = driver.find_element_by_xpath("//a[@class='btnMouse']")

actions = ActionChains(driver)

actions.move_to_element(testleaf_courses).perform()

link_texts = driver.find_elements_by_xpath("//li/a[text()='TestLeaf Courses']/parent::li/ul/li/a")

#Print all the links 
for text in link_texts:
    print(text.text)


#Click any link and handle the alert
link_texts[1].click()
time.sleep(1)
driver.switch_to.alert.accept()


time.sleep(2)
driver.quit()
