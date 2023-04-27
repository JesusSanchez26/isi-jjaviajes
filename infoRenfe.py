from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import pandas as pd

options = webdriver.ChromeOptions() # Options for Chrome
options.add_argument('--start-maximized') # Start maximized
options.add_argument('--disable-extensions') # Disable extensions

driver_path = 'C:/Users/jsanc/Desktop/Selenium/chromedriver_win32/chromedriver.exe' # Path to chromedriver

driver = webdriver.Chrome(driver_path, options=options) # Create driver

driver.get('https://www.renfe.com/es/es')

WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input#origin')))\
    .send_keys('Madrid') 

WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'li#awesomplete_list_1_item_0')))\
    .click() 

WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input#destination')))\
    .send_keys('Barcelona')

WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'li#awesomplete_list_2_item_0')))\
    .click() 

WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.mdc-button__touch.sc-rf-button')))\
    .click() 

wait = WebDriverWait(driver, 10)
tabla = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/section[2]/div/section[1]/div[3]/div[1]/table/tbody[1]/tr[1]")))
print(tabla.text)



time.sleep(10) # Wait 10 seconds
driver.quit() # Close driver

