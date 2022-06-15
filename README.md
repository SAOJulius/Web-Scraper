# Web-Scraper

**Version 1.0.0**
---


This is a easy to use Web-Scraper for image web-scraping with chrome or firefox.

# Get startet

First of all you need to install the Crome/Firefox driver matching your Browser version
For the Cromedriver go here https://chromedriver.chromium.org/downloads  
For the Firefoxdriver go here https://github.com/mozilla/geckodriver/releases


---
In the main.py you just need to specify your path where 
the images should be saved and the the terms wich shoul be searched.
The out_path is for the duplicated images to store.

---
This Funtion searches for the Data
```
search()  # Fist the term and then the Path where to store the images
```
This Funtion renames the Data
```
rename()  # Here goes just the path as an argument
```
This Funtion searches for duplicates in the Data
```
search_duplicates()  # Here goes the path and an output path where the duplicates should be saved
```
With this funtion you can manuelly sort your data press 1 to keep the image wich is displayed and 2 if you dont want to keep it
```
sort()  # Fist the path for the images you want to sort than the path where the images you want to use should go and last the path with images you dont want to use
```

