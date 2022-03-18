import time
import urllib.request

from bs4 import BeautifulSoup
from selenium import webdriver


def search(download, path):
    site = 'https://www.google.com/search?tbm=isch&q=' + download

    driver = webdriver.Chrome(executable_path='D:\Programmieren\Projekte\getdata\chromedriver.exe')

    driver.get(site)

    i = 0

    while i < 7:
        # for scrolling page
        driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

        try:
            driver.find_element_by_xpath("/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div/div[5]/input").click()
        except Exception as e:
            pass
        time.sleep(5)
        i += 1
        not_what_you_want_button = ""
        load_more_button = driver.find_element_by_css_selector(".mye4qd")
        if load_more_button and not not_what_you_want_button:
            driver.execute_script("document.querySelector('.mye4qd').click();")

    soup = BeautifulSoup(driver.page_source, 'html.parser')

    driver.close()

    img_tags = soup.find_all("img", class_="rg_i")

    count = 0
    for i in img_tags:
        try:
            # passing image urls one by one and downloading
            urllib.request.urlretrieve(i['src'], path + str(count) + ".jpg")
            count += 1
        except:
            pass
