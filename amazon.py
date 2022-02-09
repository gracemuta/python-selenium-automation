from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome("C:\\Users\\artby\\Desktop\\Automation\\python-selenium-automation\\chromedriver.exe")
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&')

# by ID
search = driver.find_element(By.ID, "continue")

# by ID
search = driver.find_element(By.NAME, "email")

# by ID
search = driver.find_element(By.ID, "auth-fpp-link-bottom")

# by ID
search = driver.find_element(By.ID, "ap-other-signin-issues-link")

# by ID
search = driver.find_element(By.ID, "createAccountSubmit")

#by XPATH
driver.find_element(By.XPATH, "//a[contains(@href, 'ref=ap_signin_notification_condition_of_use')]")
#by XPATH

driver.find_element(By.XPATH, "//a[contains(@href, 'ref=ap_signin_notification_privacy_notice')]")

driver.close()
