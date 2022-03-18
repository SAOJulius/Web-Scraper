import os

os.getcwd()


def rename(path):
    for i, filename in enumerate(os.listdir(path), ):
        try:
            os.rename(path + filename, path + str(i) + ".jpg")
        except:
            print(filename + " Can't be renamed")

    print("Renaming Finished")
