#!/usr/bin/python3

import os


def download_image_detector():
    os.system(
        'git clone https://github.com/artemisart/EuroSAT-image-classification.git')
    os.system(f"mv EuroSAT-image-classification detector")
    print("image detector downloaded!")


def copy_collected_images():
    collected_images_dir = "~/Obrazy/cansat/zebrane"
    os.system(f"cp -r {collected_images_dir} ./detector/")


download_image_detector()
copy_collected_images()
