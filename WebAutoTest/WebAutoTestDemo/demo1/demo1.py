import time

from selenium import webdriver
driver = webdriver.Edge()
driver.get("http://www.baidu.com")
 
time.sleep(10)

driver.quit()
