import pkg_resources
import subprocess
import sys
import requests
from zipfile import ZipFile
import os


def set_cwd_to_good_one():
    path_to_this_file = os.path.dirname(os.path.realpath(__file__))
    os.chdir(path_to_this_file)


def install_missing_packages():
    required = {'keras', 'opencv-python', 'tensorflow'}
    installed = {pkg.key for pkg in pkg_resources.working_set}
    missing = required - installed
    if missing:
        try:
            subprocess.check_call(
                [sys.executable, '-m', 'pip', 'install', *missing])
        except:
            print("Python packages installation failed :(")
            return 0
    else:
        print("Python packages succesfully installed!")
        return 1


def download_dataset():
    link = "https://dl.dropboxusercontent.com/s/z14mgz5qdh33pgn/dataset.zip?dl=0"
    try:
        subprocess.run(["curl", "-LJOs", link])
    except:
        print("Downloading the dataset failed :(")
        return 0
    else:
        print("Dataset downloaded!")


def unzip_dataset():
    try:
        with ZipFile("dataset.zip", 'r') as zip:
            zip.extractall()
    except:
        print("Dataset extraction failed :(")
        return 0
    else:
        print("Dataset extracted!")


def remove_zip():
    try:
        os.remove("dataset.zip")
    except:
        print("Redundant files deletion failed :(")
        return 0
    else:
        print("Redundant files deleted!")
        return 1


def get_dataset():
    files_here = os.listdir('.')
    if 'dataset' in files_here:
        print("Dataset already downloaded!")
        if 'dataset.zip' in files_here:
            remove_zip()
        return 0
    if 'dataset.zip' not in files_here:
        download_dataset()
        unzip_dataset()
        remove_zip()


def main():
    set_cwd_to_good_one()
    install_missing_packages()
    get_dataset()


if __name__ == "__main__":
    main()
