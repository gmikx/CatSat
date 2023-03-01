### PIN EXPLANATION
###     VIN -- Power for module (3-5V)
###     GND -- Ground
###     optional:
###         - VBAT - battery
###         - EN - allows for disabling the module by connecting to GND
###                may be useful before landing
###     TX -- GPS data output
###     RX -- GPS data input

import time
import board
import serial
import adafruit_gps

RX = board.RX
TX = board.TX

uart = serial.Serial("/dev/serial1", baudrate=9600, timeout=30)

gps = adafruit_gps.GPS(uart, debug=False)

gps.send_command(b'PMTK314,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0')

gps.send_command(b'PMTK220,1000')

last_print = time.monotonic()
while True:
    gps.update()
    current = time.monotonic()
    if current - last_print >= 1.0:
        last_print = current
        if not gps.has_fix:
            print('Waiting for fix...')
            continue
        print('=' * 40)  # Print a separator line.
        print('Latitude: {0:.6f} degrees'.format(gps.latitude))
        print('Longitude: {0:.6f} degrees'.format(gps.longitude))