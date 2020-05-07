from selenium import webdriver

from pathlib import Path

driver = webdriver.Chrome(Path.joinpath(Path.cwd().parent,"drivers","chromedriver"))

driver.get("http://www.leafground.com/")   

driver.find_element_by_xpath("//img[@src='images/edit.png']").click()

driver.maximize_window()

print(driver.current_url)

print(driver.title)

#print(driver.page_source)

driver.quit()