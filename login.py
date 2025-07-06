from time import sleep

from selenium import webdriver

driver = webdriver.Edge()
driver.get("http://webdriveruniversity.com/")
driver.maximize_window()

sleep(5)
driver.quit()