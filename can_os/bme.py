from bme280pi import Sensor
import time

class BME():
    def __init__(self) -> None:
        self.sensor = Sensor()

    def zbierz_dane(self):
        dane = self.sensor.get_data()
        return dane

    # def zbieraj_dane(self, opoznienie):
    #     self.zbierz_dane_bme()
    #     time.sleep(opoznienie)
    #     return