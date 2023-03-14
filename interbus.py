from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import pandas as pd

options = webdriver.ChromeOptions() # Options for Chrome
options.add_argument('--start-maximized') # Start maximized
options.add_argument('--disable-extensions') # Disable extensions

driver_path = 'C:\Users\Usuario\OneDrive - Universidad de Castilla-La Mancha\Escritorio\Lab ISI' # Path to chromedriver

driver = webdriver.Chrome(driver_path, options=options) # Create driver

driver.get('https://comprasweb.interbus.es/venta/')

WebDriverWait(driver, 10)\
    .until(EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-search/div[1]/div/app-search-departures/div/div[1]/div[1]/div[1]/app-location-dropdown/div/input')))\
    .send_keys('PUERTO LAPICE') 

WebDriverWait(driver, 10)\
    .until(EC.element_to_be_clickable((By.XPATH, '/html/body/ul[1]/li/div/div')))\
    .click() 

WebDriverWait(driver, 10)\
    .until(EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-search/div[1]/div/app-search-departures/div/div[1]/div[1]/div[2]/app-location-dropdown/div/input')))\
    .send_keys('CIUDAD REAL')

WebDriverWait(driver, 10)\
    .until(EC.element_to_be_clickable((By.XPATH, '/html/body/ul[2]/li/div/div/span[1]')))\
    .click() 

WebDriverWait(driver, 10)\
    .until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/table/tbody/tr[3]/td[4]/a')))\
    .click()

WebDriverWait(driver, 10)\
    .until(EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-search/div[1]/div/app-search-departures/div/div[4]/button')))\
    .click() 


time.sleep(10) # Wait 10 seconds
driver.quit() # Close driver