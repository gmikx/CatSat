#!/usr/bin/python3

### IMPORTS ###
# from camera import *
from bme import *
from gps import *
# from rfm22b import *
import time

### SETTING UP MODULES ###
# cam = Camera()
bme = BME()
gps = GPS()
# rfm = Rfm22()
# rfm.initialise()
# rfm.start()

### OPENING LOG FILES ###
time.sleep(1)
cz = time.time()
log = open(f"zebrane_dane_{cz}.txt", "a")
alt = open("wysokosc.txt", "w")
alt.write("0")

### CALCULATING PRESSURE NEEDED TO START CAMERA AND STOP GPS ###
pr0 = bme.cisnienie() # initial pressure. used for altitude
wys = 150
p_wys = pr0 * ((1 - (wys / 44330))**5.255)

### INITIALISING SOME VARIABLES FOR LATER USE ###
b_str=""
g_str=""
i=1

### GIVE A SIGN THAT PROGRAM STARTED ###
print("="*40 + "\n\nwystartowalem\n\n" + "="*40)

### MAIN FUNCTION ###
while True:
    b = bme.zbierz_dane()
    if c:= (b["pressure"] >= p_wys):
        alt.write("1") # send signal to program handling camera to start capturing photos
        g_str='za_wysoko' # gps doesn't have signal on such altitudes
    elif b['pressure'] <= p_wys+15:
        g_str = gps.lokalizacja() # get gps data
    else:
        alt.write("0")
    alt.flush()

    b_str = f"p{b['pressure']:.5f};t{b['temperature']};h{b['humidity']:.5f};" # format bme output

    do_wyslania = 'jd'+b_str + g_str + f"{i:08d}" # 'jd' to help our team recognize that the signal we're getting is from our cansat
                                                  # b_str contains pressure, temperature and humidity
                                                  # g_str contains data from gps
                                                  # f"{i:08d}" is number of packet being sent - used to estimate number of lost packets.
    log.write(do_wyslania)
    log.flush()

    # rfm.put_tx_data(bytes(do_wyslania, 'utf-8'))
    i+=1
