# A program to get only the most relevant PDF from google chrome
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome(executable_path="/home/virej/Downloads/Apps/drivers/chromedriver/chromedriver")
driver.get("https://google.com/")
driver.minimize_window()

search = input("What PDF would you like to search for? \n")

searchbar = driver.find_element_by_xpath('//input[@name="q"]')
searchbar.send_keys(search + ''' entire "pdf"''')
searchbar.send_keys(Keys.RETURN)

driver.find_element_by_xpath('//h3[@class]').click()

print('success')