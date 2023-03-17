#!/usr/bin/python3

# from camera import *
from bme import *
from gps import *

# cam = Camera()
bme = BME()
gps = GPS()
log = open("zebrane_dane.txt")
prs = open("wysokosc.txt")

pr0 = bme.cisnienie() # initial pressure. used for altitude
wys = 150
p_wys = pr0 / ((1 - (wys / 44330))**5.255)


while True:
    b = bme.zbierz_dane()
    b_str = f"p{b['pressure']};t{b['temperature']};h{b['humidity']};"

    g = gps.lokalizacja()
    # cam.zrob_zdjecie()