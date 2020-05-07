from selenium import webdriver
from pathlib import Path

driver = webdriver.Chrome(Path.joinpath(Path.cwd().parent,"drivers","chromedriver"))

driver.get("https://www.amazon.com/")   

#Capture all the cookies captured by the browser

Cookies = driver.get_cookies()
print(len(Cookies))
print(Cookies)

#Add a new cookie 

my_cookie = {"name":"MyCookie","value":"12345678"}
driver.add_cookie(my_cookie)

Cookies = driver.get_cookies()
print(len(Cookies))
print(Cookies)


#Delete the Cookie

driver.delete_cookie(my_cookie)

Cookies = driver.get_cookies()
print(len(Cookies))

#Delete all cookies

driver.delete_all_cookies()

Cookies = driver.get_cookies()
print(len(Cookies))


driver.quit()