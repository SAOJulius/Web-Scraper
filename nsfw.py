import opennsfw2 as n2
import os

os.getcwd()
path = "F:\JuliusKrams\Programmieren\Datasets\Frauen-Nackt\\Bilder\\"

for i, filename in enumerate(os.listdir(path), ):
    nsfw_probability = n2.predict_image(path+filename)
    if nsfw_probability < 0.9:
        os.rename(path + filename, path + str(i) + "z.jpg")
    else:
        pass


