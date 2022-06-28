#Se importan las librerias
import time 
import requests
from bs4 import BeautifulSoup
import numpy as np
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import csv

#listas
farmacias = ['Farmacia Ahumada', 'Farmacia Salcobrand']
remedios = []

#argumentos de Chrome para selenium
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://salcobrand.cl/search_result?query=JARABE")

page_source = driver.page_source

while(True):

    try:
        link = driver.find_element(By.LINK_TEXT, '»')
        driver.execute_script("arguments[0].click();", link)
        time.sleep(4)
    except:
        break