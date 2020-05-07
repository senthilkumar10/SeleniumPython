from selenium import webdriver
from pathlib import Path
import time

driver = webdriver.Chrome(Path.joinpath(Path.cwd().parent,"drivers","chromedriver"))

driver.maximize_window()

driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")   

time.sleep(2)

#scroll down page by pixel
driver.execute_script("window.scrollBy(0,1000)","")
time.sleep(2)

#scroll down page by element
flag_ele = driver.find_element_by_xpath("//img[@alt='Flag of India']")
driver.execute_script("arguments[0].scrollIntoView();",flag_ele)

#scroll down till end of the page
time.sleep(2)
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")



time.sleep(2)
driver.quit()