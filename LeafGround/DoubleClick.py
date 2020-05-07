from selenium import webdriver
from selenium.webdriver import ActionChains
from pathlib import Path
import time

driver = webdriver.Chrome(Path.joinpath(Path.cwd().parent, "drivers", "chromedriver"))

driver.maximize_window()

driver.get("http://testautomationpractice.blogspot.com/")

actions = ActionChains(driver)

dbl_click_btn = driver.find_element_by_xpath("//button[text()='Copy Text']")

actions.double_click(dbl_click_btn).perform()

time.sleep(2)
driver.quit()