from selenium import webdriver
from pathlib import Path
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(executable_path=Path.joinpath(Path.cwd().parent, "drivers", "geckodriver"))

driver.maximize_window()

driver.get("http://www.leafground.com/")

driver.find_element_by_xpath("//img[@src='images/alert.png']").click()

time.sleep(2)

#Click the button and accept the alert
driver.find_element_by_xpath("//button[@onclick='normalAlert()']").click()
driver.switch_to_alert().accept()
print("Alert Accepted")


#Click the button and Cancel the alert
driver.find_element_by_xpath("//button[@onclick='confirmAlert()']").click()
driver.switch_to_alert().dismiss()
print("Alert Cancelled")

#Click the button and input Text to the alert
driver.find_element_by_xpath("//button[@onclick='confirmPrompt()']").click()
driver.switch_to_alert().send_keys("Sending My Text")
time.sleep(2)
driver.switch_to_alert().accept()
print("Sent Text to an Alert")

#Click the button and get the alert text
driver.find_element_by_xpath("//button[@onclick='lineBreaks()']").click()
print("Alert Text - "+driver.switch_to_alert().text)
driver.switch_to_alert().accept()

#Click the button and click Ok on the Sweet Alert
driver.find_element_by_xpath("//button[@onclick='sweetalert()']").click()
driver.find_element_by_xpath("//button[text()='OK']").click()
print("Click Ok on the sweet Alert")


time.sleep(2)
driver.quit()




