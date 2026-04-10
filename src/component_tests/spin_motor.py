"""
Purpose of this file: Make a motor spin

How to test with this code?:
Specify the range
"""

from utils.brick import Motor
import time

# Adjust the constants to match your setup.
MOTOR_PORT = "A"
INITIAL_POS = 0
FINAL_POS = 360

m = Motor("A")
m.set_limits(power=50)
m.set_position_relative(INITIAL_POS)
time.sleep(3)
m.set_position_relative(FINAL_POS)

