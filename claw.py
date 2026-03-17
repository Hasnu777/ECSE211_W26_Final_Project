from utils import sound
from utils.brick import TouchSensor, Motor, EV3UltrasonicSensor, wait_ready_sensors
import time
import threading

# -------------------- SENSORS AND MOTORS --------------------
m1 = Motor("A")
m2 = Motor("B")


m1.setlimits()
m2.setlimits()

# -------------------- FUNCTIONS --------------------


def main():
    # rotate
    m1.set_position(180)
    m2.set_position(-180)
    
    m1.set_dps(0)
    m2.set_dps(0)
    
    m1.set_position(200)
    m2.set_position(-200)