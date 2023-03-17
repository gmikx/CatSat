from bme280pi import Sensor  # https://pypi.org/project/bme280pi/

## HOOKUP SCHEMA:
##   VCC - 3.3V (eg. pin 1)
##   GND - GND (eg. pin 6)
##   SCL - pin 5
##   SDA - pin 3

class BME():
    def __init__(self) -> None:
        self.sensor = Sensor()

    def zbierz_dane(self):
        dane = self.sensor.get_data()
        return dane
    
    def cisnienie(self):
        return self.sensor.get_pressure()

    # def zbieraj_dane(self, opoznienie):
    #     self.zbierz_dane_bme()
    #     time.sleep(opoznienie)
    #     return