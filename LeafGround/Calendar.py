from selenium import webdriver
from pathlib import Path
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(Path.joinpath(Path.cwd().parent, "drivers", "chromedriver"))

wait = WebDriverWait(driver,10)

driver.maximize_window()

driver.get("http://www.leafground.com/")

driver.find_element_by_xpath("//img[@src='images/calendar-icon.png']").click()

time.sleep(2)

driver.find_element_by_id("datepicker").click()

wait.until(EC.element_to_be_clickable((By.XPATH,"//a[contains(@class,'ui-state-highlight')]")))

day = driver.find_element_by_xpath("//a[contains(@class,'ui-state-highlight')]").text

new_day = int(day)+10


driver.find_element_by_xpath("//a[@class='ui-state-default'][text()='"+str(new_day)+"']").click()



time.sleep(2)
driver.quit()




