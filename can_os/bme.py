from bme280pi import Sensor

def zbierz_dane_bme():
    sensor = Sensor()
    dane = sensor.get_data()
    return dane