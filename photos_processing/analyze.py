#!/usr/bin/python3

# Following script is made to analyze photos collected by our CanSat.
# By analyze I mean predict the type of terrain on photo, and generate map based on this photo.


###########################################
###  Script by @gmikx (Mikołaj Giza)    ###
###  CatSat Team in CanSat Competition  ###
###########################################

# The script is licensed under GPLv3 license

## Imports ##
from keras.models import load_model
from keras.preprocessing.image import ImageDataGenerator
import cv2
import numpy as np
import matplotlib.pyplot as plt
import os


# Define Colors For the Map
crop = np.array([26, 127, 3])
desert = np.array([234,216,30])
forest = np.array([10,94,13])
highway = np.array([100,100,100])
industrial = np.array([225,24,73])
pasture = np.array([51,102,37])
residential = np.array([255,0,162])
river = np.array([0, 255,240])
sea_lake = np.array([0,61,225])
legend = {0:crop, 1:desert, 2:forest, 3:forest, 4:highway, 5:industrial, 6:pasture, 7:crop, 8:residential, 9:river, 10:sea_lake}


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


def create_dir_for_maps():
    try:
        os.mkdir('./maps')
    except:
        os.chdir('./photos_to_process/')
        print("Creating dir for maps failed :(")
        return 0
    else:
        os.chdir('./photos_to_process/')
        print("Dir for maps created successfully!")
        return 1


def list_photos():
    global photos
    photos = os.listdir(".")
    # photos.remove('tmp')


def setup():
    set_path()
    load_cnn_model()
    create_dir_for_maps()
    list_photos()


## Analyzing Photos ##

def load_photo(filename: str):
    img = cv2.imread(filename, cv2.IMREAD_COLOR)
    return img


def classify_slice(image):
    img = 1./255 * image
    img = img.reshape(1, 64, 64, 3)
    pred = cnn.predict(img)
    prediction = np.argmax(pred)
    color = legend[prediction]
    return color


def generate_slices_and_map(image, filename):
    global terrain_map
    img_y, img_x = image.shape[0], image.shape[1]
    win_x, win_y = 64, 64
    no_windows_x = img_x - win_x + 1
    no_windows_y = img_y - win_y + 1
    terrain_map = np.zeros((no_windows_y, no_windows_x, 3))
    filename_strip = filename[:filename.rfind('.')]

    for y in range(0, no_windows_y):
        for x in range(0, no_windows_x):
            sl = image[y:y+win_y, x:x+win_x]
            color = classify_slice(sl)
            # print(x, y, color)
            terrain_map[y,x] = color

    cv2.imwrite(f"../maps/{filename_strip}-map.jpg", terrain_map)



def analyze_photo(filename: str):
    
    img = load_photo(filename)
    generate_slices_and_map(img, filename)


def main():
    setup()
    # for photo in photos:
    #     try:
    #         analyze_photo(photo)
    #         del(terrain_map)
    #     except KeyboardInterrupt:
    #         cv2.imwrite(f"../maps/draft-map.jpg", terrain_map)

    try:
        analyze_photo("test.png")
    except KeyboardInterrupt:
        cv2.imwrite(f"../maps/draft-map.jpg", terrain_map)

if __name__ == "__main__":
    main()
