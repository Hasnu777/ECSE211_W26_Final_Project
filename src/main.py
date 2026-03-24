from utils import sound
from utils.brick import TouchSensor, Motor, EV3UltrasonicSensor, wait_ready_sensors
import time
import threading


# -------------------- SENSORS AND MOTORS --------------------
m1 = Motor("A")
m2 = Motor("B")

m1.set_limits(power=50)
m2.set_limits(power=50)

# -------------------- FUNCTIONS --------------------


def main():
    oneSquare = 710
    m1.reset_encoder()
    m2.reset_encoder()
# Moving from 1 to 2
    m2.set_position(oneSquare)
    m1.set_position(oneSquare)
    time.sleep(5)
    m2.reset_encoder()
    m1.reset_encoder()

# Turning from 2 to 3 and moving
    m1.set_position(340)
    m2.set_position(-340)
    time.sleep(1)
    m2.reset_encoder()
    m1.reset_encoder()
    m1.set_position(oneSquare*2)
    m2.set_position(oneSquare*2)
    time.sleep(5)
    m2.reset_encoder()
    m1.reset_encoder()
#Turning 3 to 4 and moving
    m2.set_position(340)
    m1.set_position(-340)
    time.sleep(2)
    m2.reset_encoder()
    m1.reset_encoder()
    m2.set_position(oneSquare*2)
    m1.set_position(oneSquare*2)
    time.sleep(5)
    m2.reset_encoder()
    m1.reset_encoder()
    m1.set_position(-340)
    m2.set_position(340)
    time.sleep(5)
    m2.reset_encoder()
    m1.reset_encoder()
    m1.set_position(oneSquare)
    m2.set_position(oneSquare)
    time.sleep(3)

#
#Moving 4    
#m1.set_dps(720)
    #m2.set_dps(720)
    #time.sleep(3)
    #m1.set_dps(0)
    #m2.set_dps(0)

    # rotate


if __name__ == "__main__":
    print("test")
    main()

#from utils import sound
#from utils.brick import TouchSensor, Motor, EV3UltrasonicSensor, wait_ready_sensors
#import time
#import threading

# -------------------- SENSORS AND MOTORS --------------------
#m1 = Motor("A")
#m2 = Motor("B")

#m1.set_limits(power=50)
#m2.set_limits(power=50)

# -------------------- FUNCTIONS --------------------


#def main():
#    m1.reset_encoder()
#    m2.reset_encoder()
#    m1.set_position(-335)
#    m2.set_position(335)
    #m1.set_dps(720)
    #m2.set_dps(720)
    #time.sleep(3)
    #m1.set_dps(0)
    #m2.set_dps(0)

    # rotate


#if __name__ == "__main__":
#    print("test")
#    main()
