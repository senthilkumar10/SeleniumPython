from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from pathlib import Path

driver = webdriver.Chrome(Path.joinpath(Path.cwd().parent,"drivers","chromedriver"))

driver.maximize_window()

driver.get("https://www.expedia.com/")

driver.find_element(By.ID,"tab-flight-tab-hp").click()

driver.find_element(By.ID,"flight-origin-hp-flight").send_keys("SFO")

driver.find_element(By.ID,"flight-destination-hp-flight").send_keys("NYC")   

driver.find_element(By.ID,"flight-departing-hp-flight").clear()

driver.find_element(By.ID,"flight-departing-hp-flight").send_keys("05/30/2020")

driver.find_element(By.ID,"flight-returning-hp-flight").clear()

driver.find_element(By.ID,"flight-returning-hp-flight").click()

driver.find_element_by_xpath("//*[@id='traveler-selector-hp-flight']/div/ul/li/button").click()

driver.find_element(By.XPATH, "//button[@type='submit']/span[text()='Search']/parent::button").click()

wait = WebDriverWait(driver,10)

wait.until(EC.element_to_be_clickable((By.XPATH,"//input[contains(@id,'changeOptionFilter')]")))

driver.find_element_by_xpath("//input[contains(@id,'changeOptionFilter')]").click()

time.sleep(5)

driver.quit()

