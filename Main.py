import random
from WebScraper import *
from selenium import webdriver

path = ""
out_path = ""
search_term = []

driver = webdriver.Chrome(executable_path='D:\Programmieren\Projekte\Web-Scraper\Bilder\chromedriver.exe')

for i, term in search_term:
    search(term, path, i, driver)

driver.close()

