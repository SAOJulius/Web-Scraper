import os

from difPy import dif

os.getcwd()


def search_duplicates(path, out_path):
    search = dif(path)
    print(search.result)
    i = 0
    for image in search.result:
        os.rename(path + image, out_path + image + str(i) + ".jpg")
        print(image)
        i += 1

    print("Suche abgeschlossen")
