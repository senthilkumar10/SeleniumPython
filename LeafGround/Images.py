from selenium import webdriver
from pathlib import Path
import time
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(Path.joinpath(Path.cwd().parent, "drivers", "chromedriver"))

driver.maximize_window()

driver.get("http://www.leafground.com/")

driver.find_element_by_xpath("//a[@href='pages/Image.html']").click()

time.sleep(2)

# Click on the image to go Home Page

driver.find_element_by_xpath("//img[@src='../images/home.png']").click()

# Come back to the Image page again

driver.find_element_by_xpath("//a[@href='pages/Image.html']").click()

print(driver.find_element_by_xpath("//img[@src='../images/home.png']").get_attribute("naturalWidth"))

natural_width = driver.find_element_by_xpath("//img[@src='../images/abcd.jpg']").get_attribute("naturalWidth")

if natural_width == "0":
    print("Image is broken")
else:
    print("Image is not broken")

##Using Keyboard click a link

#driver.find_element_by_xpath("//img[@src='../images/keyboard.png']").send_keys(Keys.CONTROL,Keys.ENTER)

time.sleep(2)
driver.quit()
