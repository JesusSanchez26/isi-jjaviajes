from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import pandas as pd

options = webdriver.ChromeOptions() # Options for Chrome
options.add_argument('--start-maximized') # Start maximized
options.add_argument('--disable-extensions') # Disable extensions

driver_path = 'C:/Users/jsanc/Desktop/Selenium/chromedriver_win32/chromedriver.exe'

driver = webdriver.Chrome(driver_path, options=options) # Create driver

driver.get('https://comprasweb.interbus.es/venta/')

#clica en origen y pone el origen
WebDriverWait(driver, 10)\
    .until(EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-search/div[1]/div/app-search-departures/div/div[1]/div[1]/div[1]/app-location-dropdown/div/input')))\
    .send_keys('PUERTO LAPICE') 

WebDriverWait(driver, 10)\
   .until(EC.element_to_be_clickable((By.XPATH, '/html/body/ul[1]/li/div/div')))\
    .click() 

#clica en destino y pone el destino
WebDriverWait(driver, 10)\
    .until(EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-search/div[1]/div/app-search-departures/div/div[1]/div[1]/div[2]/app-location-dropdown/div/input')))\
    .send_keys('CIUDAD REAL')

WebDriverWait(driver, 10)\
   .until(EC.element_to_be_clickable((By.XPATH, '/html/body/ul[2]/li/div/div/span[1]')))\
   .click() 


#clica en solo ida
WebDriverWait(driver, 10)\
    .until(EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-search/div[1]/div/app-search-departures/div/div[2]/div[1]/label[1]')))\
    .click()

#clica en el calendario para seleccionar la fecha
WebDriverWait(driver, 10)\
    .until(EC.element_to_be_clickable((By.ID, 'departureDate')))\
    .clear()  #borra la fecha puesta  

WebDriverWait(driver, 10)\
    .until(EC.element_to_be_clickable((By.ID, 'departureDate')))\
    .send_keys('11/04/2023')    #pone la fecha elegida  

    

    
#clica en buscar
WebDriverWait(driver, 10)\
    .until(EC.element_to_be_clickable((By.CLASS_NAME, 'Button')))\
    .click()

#clica en buscar
WebDriverWait(driver, 10)\
    .until(EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-iframe-search/div/app-search-departures/div/div[4]/button')))\
    .click()


time.sleep(10) # Wait 10 seconds
driver.quit() # Close driver
