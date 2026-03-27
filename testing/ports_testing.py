import utils.sound as sound
from utils.brick import TouchSensor, Motor, EV3UltrasonicSensor, wait_ready_sensors
from time import sleep

# -------------------- MOTOR TEST --------------------
m = Motor("A")
m.set_limits(power=50)
m.set_position_relative(360)

# -------------------- SENSORS AND MOTORS --------------------
"""
s = TouchSensor(1)
while (True):
    if (s.isPressed()):
        print("pressed")
    print("pressed")
"""