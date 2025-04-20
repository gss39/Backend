from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

# Create a webdriver instance and navigate to the webpage
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.geeksforgeeks.org/python-programming-language/")

# Hover over "Tutorials" and wait for 3 seconds
tutorials = driver.find_element(By.XPATH, "//nav//li[contains(text(), 'Tutorials')]")
actions = ActionChains(driver)
actions.move_to_element(tutorials).perform()
time.sleep(3)

# Hover over "ML & Data Science" and wait for 3 seconds
ml_and_data_science = driver.find_element(By.XPATH, "//nav//li[contains(text(), 'ML & Data Science')]")
actions.move_to_element(ml_and_data_science).perform()
time.sleep(3)

# Hover over "Machine Learning" and wait for 3 seconds
machine_learning = driver.find_element(By.XPATH, "//nav//li[contains(text(), 'Machine Learning')]")
actions.move_to_element(machine_learning).perform()
time.sleep(3)

# Hover over "Machine Learning Tutorial" and wait for 3 seconds
ml_tutorial = driver.find_element(By.XPATH, "//nav//li[contains(text(), 'Machine Learning Tutorial')]")
actions.move_to_element(ml_tutorial).perform()
time.sleep(3)

# Close the webdriver
driver.quit()
