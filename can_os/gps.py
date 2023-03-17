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

class GPS():
    def __init__(self):
        self.RX = board.RX
        self.TX = board.TX
        self.uart = serial.Serial("/dev/serial0", baudrate=9600, timeout=30)
        self.gps = adafruit_gps.GPS(self.uart, debug=False)

        self.gps.send_command(b'PMTK314,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0')
        self.gps.send_command(b'PMTK220,1000')
        self.last_print = time.monotonic()
        
    # def lokalizacja(self):
    #     self.gps.update()
    #     self.current = time.monotonic()
    #     if self.current - self.last_print >= 1.0:
    #         self.last_print = self.current
    #         if not self.gps.has_fix:
    #             print('Waiting for fix...')
    #         else:
    #             print('=' * 40)  # Print a separator line.
    #             print('Latitude: {0:.6f} degrees'.format(self.gps.latitude))
    #             print('Longitude: {0:.6f} degrees'.format(self.gps.longitude))
    
    def lokalizacja(self):
        pos=""
        self.gps.update()
        if not self.gps.has_fix:
            pos="NOFIX"
        else:
            pos+='gp{0:.6f}'.format(self.gps.latitude)
            pos+=' {0:.6f}'.format(self.gps.longitude)
        return pos