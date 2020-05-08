from selenium import webdriver
from pathlib import Path
from XLUtil import getColumnCount,getRowCount,readData,writeData

def initialize():
    driver = webdriver.Chrome(Path.joinpath(Path.cwd().parent, "drivers", "chromedriver"))
    driver.maximize_window()
    driver.get("http://leaftaps.com/opentaps")
    return driver


xl_path = "./Login.xlsx"

row_count = getRowCount(xl_path,"Sheet1")
col_count = getColumnCount(xl_path,"Sheet1")

for r in range(2, row_count+1):

    driver = initialize()
    user_id = driver.find_element_by_id("username")
    password = driver.find_element_by_id("password")
    login_btn = driver.find_element_by_xpath("//input[@type='submit']")
    
    user_name_xl = readData(xl_path,"Sheet1",r,1)
    password_xl = readData(xl_path,"Sheet1",r,2)

    user_id.send_keys(user_name_xl)
    password.send_keys(password_xl)
    login_btn.click()

    message = driver.find_element_by_xpath("//h2").text
    
    if "Welcome" in message:
        writeData(xl_path,"Sheet1",r,3,"Pass")
    else:
        writeData(xl_path,"Sheet1",r,3,"Fail")

    print("Test Case "+str(r-1)+" is completed.")

    driver.quit()

