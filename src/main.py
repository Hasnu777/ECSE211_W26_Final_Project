from utils import sound
from utils.brick import TouchSensor, Motor, EV3UltrasonicSensor, wait_ready_sensors
import time
import threading

# -------------------- SENSORS AND MOTORS --------------------
m1 = Motor("A")
m2 = Motor("B")

# m1.reset_encoder();
# m2.reset_encoder();
# m1.setlimits()
# m2.setlimits()

# -------------------- FUNCTIONS --------------------


# rotate
while (True):
    m1.set_position(-80)
    m2.set_position(-50)
    time.sleep(1)
    m1.set_position(0)
    m2.set_position(0)
    time.sleep(1)

    




