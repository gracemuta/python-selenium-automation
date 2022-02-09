from time import sleep
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import *

# init driver
driver = webdriver.Chrome("C:\\Users\\artby\\Desktop\\Automation\\python-selenium-automation\\chromedriver.exe")
driver.maximize_window()

driver.get("https://www.amazon.com/gp/help/customer/display.html")

searchBox= driver.find_element(By.ID, "helpsearch")
searchBox.send_keys("cancel order")
searchBox.send_keys(Keys.ENTER)

expected_result = '"cancel order"'

actual_result = '//div[@class="help-content"]/h1'

driver.close()
