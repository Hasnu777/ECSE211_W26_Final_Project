from utils import sound
from utils.brick import TouchSensor, wait_ready_sensors

TS= TouchSensor(1)

N1 = sound.Sound(duration=0.1, pitch="A5", volume=50)

wait_ready_sensors()

while (True):
    if (TS.is_pressed()):
        print("Touch Registered")
        N1.play()
        N1.wait_done()
