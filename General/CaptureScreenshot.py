from selenium import webdriver
from pathlib import Path
from datetime import datetime
import time

current_date_time = datetime.now()

driver = webdriver.Chrome(Path.joinpath(Path.cwd().parent,"drivers","chromedriver"))

driver.get("https://www.amazon.com/")   

driver.save_screenshot("./snapshots/homepage_"+str(current_date_time)+".png")

time.sleep(1)

driver.get_screenshot_as_file("./snapshots/homepage"+str(current_date_time)+".png")

driver.quit()