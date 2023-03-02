from picamera2 import Picamera2#, Preview
from datetime import datetime
import time

class Camera:
    def __init__(self) -> None:
        self.camera = Picamera2()
        camera_config = self.camera.create_still_configuration(main={"size":(1820,1080)}, lores={"size":(0, 0)}, display="lores")
        self.camera.configure(camera_config)
        self.camera.start()
        time.sleep(2)

    def zrob_zdjecie(self):
        self.camera.capture_file(datetime.now().strftime("%Y_%m_%d__%H_%M_%S") + ".jpg")

    # def rob_zdjecia(self, opoznienie:float):
    #     teraz:str = datetime.now().strftime("%Y_%m_%d__%H_%M_%S") + ".jpg"
    #     self.zrob_zdjecie(teraz)
    #     time.sleep(opoznienie)