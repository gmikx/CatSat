## Imports ##

from keras.models import load_model
from keras.preprocessing.image import ImageDataGenerator
import cv2
import numpy as np
import matplotlib.pyplot as plt
import os


# Define Colors For the Map
crop = []
desert = []
forest = []
highway = []
industrial = []
pasture = []
residential = []
river = []
sea_lake = []

## Setup ##


def set_path():
    global PATH
    try:
        PATH = os.path.dirname(os.path.realpath(__file__))
    except:
        PATH = '.'
    os.chdir(PATH)


def load_cnn_model():
    global cnn
    cnn = load_model('./best_model')


def dir_for_slices():
    try:
        os.chdir('./photos_to_process/')
        os.mkdir('tmp')
    except:
        print("Creating dir for slices failed :(")
        return 0
    else:
        print("Dir for slices created successfully!")
        return 1


def list_photos():
    global photos
    photos = os.listdir(".")
    photos.remove('tmp')


def setup():
    set_path()
    load_cnn_model()
    dir_for_slices()
    list_photos()

## Analyzing Photos ##


def load_photo(filename: str):
    img = cv2.imread(filename, cv2.IMREAD_COLOR)
    return img


def classify_slice(image):
    img = 1./255 * image
    pred = cnn.predict(img)


def generate_slices(image, filename: str):
    img_y, img_x, _ = image.shape
    win_x, win_y = 64, 64
    no_windows_x = img_x - win_x + 1
    no_windows_y = img_y - win_y + 1
    no_digits_x = len(str(no_windows_x))
    no_digits_y = len(str(no_windows_y))

    filename_strip = filename[:filename.rfind('.')]

    for y in range(no_windows_y):
        for x in range(no_windows_x):
            sl = image[y:y+win_y, x:x+win_x]
            name = f'./tmp/{filename_strip}-{x:0{no_digits_x}d}-{y:0{no_digits_y}d}.png'
            cv2.imwrite(filename=name, img=sl)


def analyze_photo(filename: str):
    img = load_photo(filename)
    generate_slices(img, filename)
    # classify_slices()
    # generate_map()
    # remove_slices()


def main():
    setup()
    analyze_photo("photo2.png")


if __name__ == "__main__":
    main()
