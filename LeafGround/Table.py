from selenium import webdriver
from pathlib import Path
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(Path.joinpath(Path.cwd().parent, "drivers", "chromedriver"))

driver.maximize_window()

driver.get("http://www.leafground.com/")

driver.find_element_by_xpath("//img[@src='images/table.png']").click()

time.sleep(2)

#Get the count of number of columns
print("Total No of Columns :- "+str(len(driver.find_elements_by_xpath("//th"))))

#Get the count of number of rows
print("Total No of Rows :- "+str(len(driver.find_elements_by_xpath("//tr"))))

#Get the Progress Value of Learn to interact using Keyboard, Actions
print("The Progress Value :- "+driver.find_element_by_xpath("//td[text()='Learn to interact using Keyboard, Actions']/following-sibling::td").text)

#Check the vital task for the least completed progress
progress_values = driver.find_elements_by_xpath("//td[2]")


# progress_val_list = []

# for each_progress_value in progress_values:
#     progress_val_list.append(int(each_progress_value.text.replace("%","")))    

progress_val_list = list(map(lambda x : int(x.text.replace("%","")),progress_values))

min_progress_val = min(progress_val_list)

progress_val_index = progress_val_list.index(min_progress_val)

driver.find_element_by_xpath("(//td[3])["+str(progress_val_index+1)+"] /input").click()

print("Vital task for the least completed progress is checked sucessfully")

time.sleep(2)
driver.quit()




