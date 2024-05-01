import os 
from selenium import webdriver


driver = webdriver.Chrome()
driver.get('https://www.seleniumeasy.com/test/jquery-download-progress-bar-demo.html')
driver.implicitly_wait(30) 
myElement = driver.find_element('logo')
myElement.click()
