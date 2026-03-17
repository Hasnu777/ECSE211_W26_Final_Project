from utils import sound
from utils.brick import TouchSensor, Motor, EV3UltrasonicSensor, wait_ready_sensors
import time
import threading

# -------------------- SENSORS AND MOTORS --------------------
m1 = Motor("A")
m2 = Motor("B")

# m1.setlimits()
# m2.setlimits()

# -------------------- FUNCTIONS --------------------


def main():
    m1.reset_encoder()
    m2.reset_encoder()
    m1.set_position(-360)
    m2.set_position(360)
    #m1.set_dps(720)
    #m2.set_dps(720)
    #time.sleep(3)
    #m1.set_dps(0)
    #m2.set_dps(0)

    # rotate


if __name__ == "__main__":
    print("test")
    main()


    




