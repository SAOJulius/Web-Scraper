import os

import keyboard
from PIL import Image


def sort(path_from, out_path_to, out_path2_to, out_path3_to):
    for image in os.listdir(path_from):
        try:
            im = Image.open(path_from + image)
            im.show()
            while True:

                if keyboard.read_key() == "1":
                    os.rename(path_from + image, out_path_to + image)
                    break
                if keyboard.read_key() == "2":
                    os.rename(path_from + image, out_path2_to + image)
                    break
                if keyboard.read_key() == "3":
                    os.rename(path_from + image, out_path3_to + image)
                    break
        except:
            os.remove(path_from + image)
