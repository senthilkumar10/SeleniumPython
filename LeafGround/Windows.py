from selenium import webdriver
from pathlib import Path
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(Path.joinpath(Path.cwd().parent, "drivers", "chromedriver"))

wait = WebDriverWait(driver,10)

driver.maximize_window()

driver.get("http://www.leafground.com/")

driver.find_element_by_xpath("//img[@src='images/windows.png']").click()

time.sleep(2)

original_window = driver.current_window_handle

#Switch to Frame using WebElement
driver.find_element_by_id("home").click()
handles = driver.window_handles

for handle in handles:
    if handle!=original_window:
        driver.switch_to.window(handle)
        print(driver.title)
        break

driver.close()

#Find the number of opened windows
driver.switch_to.window(original_window)
driver.find_element_by_xpath("//button[text()='Open Multiple Windows']").click()
handles = driver.window_handles

print("Total No of Windows opened: "+str(len(handles)))


#Close all the child window except the parent window
for handle in handles:
    if handle!=original_window:
        driver.switch_to.window(handle)
        time.sleep(1) #I am delaying 1 sec to view the progress of closing the window
        driver.close()


driver.switch_to.window(original_window)


#Wait for 2 secs until the windows are open 

driver.find_element_by_xpath("//button[text()='Wait for 5 seconds']").click()
wait.until(EC.number_of_windows_to_be(3))

print(len(driver.window_handles))


time.sleep(2)
driver.quit()




