# CatSat
Hi!

This is CatSat team (CanSat competition) repo for development - software for both our CanSat and ground station.

Cats also can fly! :cat::stars:

---

We are building on top of [artemisart's satellite images classificator](https://github.com/artemisart/EuroSAT-image-classification).

We combined 2 datasets - one available on [Kaggle](https://www.kaggle.com/datasets/mahmoudreda55/satellite-image-classification?resource=download) and the other one was [EuroSAT](https://madm.dfki.de/files/sentinel/EuroSAT.zip). We had to resize and preprocess images from Kaggle since their size was 128x128 not 64x64 (as was the case for EuroSat).

Our program creates a map from gathered *almost* satelite images from our cansat. It slices the images to 64x64 sub-images and feeds them into artemisart's program. Then we use the output to color the output map.
