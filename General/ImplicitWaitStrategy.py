#Implicit Wait

from selenium import webdriver

from pathlib import Path

driver = webdriver.Chrome(Path.joinpath(Path.cwd().parent,"drivers","chromedriver"))

driver.implicitly_wait(10)

driver.get("http://newtours.demoaut.com")

assert "Welcome: Mercury Tours" in driver.title

driver.quit()