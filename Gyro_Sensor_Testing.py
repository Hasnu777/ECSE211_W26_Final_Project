from utils import sound
from utils.brick import TouchSensor, Motor, EV3UltrasonicSensor, EV3GyroSensor, wait_ready_sensors
import time
import threading

TS1 = TouchSensor(2)
Gyro = EV3GyroSensor(1,mode="both")

while True:
    if TS1.is_pressed():
        break
    print(Gyro.get_raw_value())
    time.sleep(0.5)