import os
import time
import urllib.request
import urllib.request

import cv2
import numpy as np
import opennsfw2 as n2
import pandas as pd
from PIL import Image
from difPy import dif
from selenium import webdriver
from selenium.webdriver.common.by import By

os.getcwd()


def lookForPeople(path, out_path):
    for i, pictures in enumerate(os.listdir(path), ):

        if i <= -1:
            pass
        else:
            try:
                image = cv2.imread(path + pictures)
                gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

                faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_alt.xml")
                faces = faceCascade.detectMultiScale(
                    gray,
                    scaleFactor=1.3,
                    minNeighbors=3,
                    minSize=(30, 30)
                )

                faceCascade2 = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_fullbody.xml")
                faces2 = faceCascade.detectMultiScale(
                    gray,
                    scaleFactor=1.3,
                    minNeighbors=3,
                    minSize=(30, 30)
                )

                if len(faces) <= 1:
                    os.rename(path + pictures, out_path + pictures)
                elif len(faces2) <= 1:
                    os.rename(path + pictures, out_path + pictures)

            except:
                pass

        if i % 1000 == 0:
            print(i)

        else:
            pass


def findSize(path):
    size = []
    for i, images in enumerate(os.listdir(path), ):
        try:
            image = Image.open(path + images)
            size.append([image.size[0], image.size[1]])
        except Exception as e:
            print(e)

        if i % 1000 == 0:
            print(i)
        else:
            pass

    print(pd.value_counts(np.array(size)))


def cropImages(path, out_path):

    for i, images in enumerate(os.listdir(path), ):
        try:
            img = Image.open(path + images)

            faceCascade = cv2.CascadeClassifier('cascade\haarcascade_fullbody.xml')

            image = cv2.imread(img)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            faces = faceCascade.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30),
                # flags = cv2.CV_HAAR_SCALE_IMAGE
            )

            print("Found {0} faces!".format(len(faces)))

            for (x, y, w, h) in faces:
                # cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
                img_res = img.crop((x, y, (x + w), (y + h)))

            cv2.imwrite(path + i + "cropped.jpg", img_res)
            os.rename(path + images, out_path + str(i) + ".jpg")

        except Exception as e:
            print(e)



def detectNSFW(path, out_path):
    for i, filename in enumerate(os.listdir(path), ):
        nsfw_probability = n2.predict_image(path + filename)
        if nsfw_probability < 0.9:
            os.rename(path + filename, out_path + str(i) + ".jpg")
            print(i)
        else:
            pass


def search(term, path, counter, driver):
    site = 'https://www.google.com/search?tbm=isch&q=' + term

    driver.get(site)

    m = 0
    while m < 3:
        # for scrolling page
        driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

        try:
            driver.find_element_by_xpath("/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div/div[5]/input").click()
        except:
            pass
        time.sleep(0.1)
        m += 1
        not_what_you_want_button = ""
        load_more_button = driver.find_element_by_css_selector(".mye4qd")
        if load_more_button and not not_what_you_want_button:
            driver.execute_script("document.querySelector('.mye4qd').click();")
        # time.sleep(0.3)

    images = driver.find_elements_by_tag_name('img')

    for i, url in images:
        try:
            urllib.request.urlretrieve(url.get_attribute('src'), path + i + counter + ".jpg")
        except Exception as e:
            print(e)
        time.sleep(0.1)


def searchFromOtherURL(path):
    driver = webdriver.Chrome(executable_path='D:\Programmieren\Projekte\Web-Scraper\chromedriver.exe')

    driver.get("URL")
    l = 0
    uri = []
    while True:
        driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

        images = driver.find_elements_by_tag_name('img')
        for i in images:
            src = i.get_attribute("src")
            uri.append(src)

        try:
            button = driver.find_element(By.LINK_TEXT, 'Next')
            button.click()
            print("Seite " + str(l))
        except Exception as f:
            print(f)
            break

        l += 1
    count = 0
    for i in uri:
        urllib.request.urlretrieve(i, path + str(count) + "e" + str(count) + ".jpg")
        time.sleep(0.1)
        count += 1

    driver.close()


def search_duplicates(path, out_path):
    search = dif(path)
    print(search.result)
    i = 0
    for image in search.result:
        os.rename(path + image, out_path + image + str(i) + ".jpg")
        print(image)
        i += 1

    print("Suche abgeschlossen")


def rename(path):
    for i, filename in enumerate(os.listdir(path), ):
        try:
            os.rename(path + filename, path + str(i) + ".jpg")
        except Exception as e:
            print(e)

        if i % 1000 == 0:
            print(i)
        else:
            pass

    print("Renaming Finished")
