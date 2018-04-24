from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os

#Environment variables
chrome_driver = os.getenv('SELENIUM_PATH','path/to/chrome/driver')
webpage = os.getenv('SELENIUM_PAGE', 'https://www.yahoo.com')

#Selenium
page = webdriver.Chrome(chrome_driver)
page.get(webpage)
