from selenium import webdriver
from pathlib import Path
import time
import requests


driver = webdriver.Chrome(Path.joinpath(Path.cwd().parent,"drivers","chromedriver"))

driver.maximize_window()

driver.get("http://www.leafground.com/")   

driver.find_element_by_xpath("//a[@href='pages/Link.html']").click()

time.sleep(2)

#Go to Home Page

driver.find_element_by_xpath("(//a[@href='../home.html'])[2]").click()

#Come back to the Hyperlink page again

driver.find_element_by_xpath("//a[@href='pages/Link.html']").click()

#Find the link where it should go

attr = driver.find_element_by_xpath("//a[text()='Find where am supposed to go without clicking me?']").get_attribute("href")

print(attr)

#Verify the Link is broken or not.

brokenlink = driver.find_element_by_xpath("//a[text()='Verify am I broken?']").get_attribute("href")

status_code = requests.head(brokenlink).status_code

if status_code == 200:
    print("It is not a broken link")
else:
    print("It is a broken link")  

#Go to Home Page

driver.find_element_by_xpath("(//a[@href='../home.html'])[3]").click()

#Come back to the Hyperlink page again

driver.find_element_by_xpath("//a[@href='pages/Link.html']").click()

#Find total number of links in this page

total_links = driver.find_elements_by_xpath("//a")

print("Total No of links in this page :- "+str(len(total_links)))
  

driver.quit()