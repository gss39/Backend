# Importing libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import pandas as pd
import re
import time
import mysql.connector


s = Service("C:\Program Files\Google\Chrome\Application\chrome.exe")
driver = webdriver.Chrome()
# driver.get("https://www.google.com")

# URL of website
url = "https://www.geeksforgeeks.org/"

# Opening the website
driver.get(url)

# getting the button by class name
button = driver.find_elements('slide-out-btn')

# clicking on the button
button.click()

# # # Intializing driver
# driver = webdriver.Chrome()



# urls = []
# for i in flip_database.fetch_data():


# driver.get(link)

# content = driver.page_source
# soup = BeautifulSoup(content, "html.parser")

# print(soup)