"""
Purpose of this files: Testing if the ports work
How to test with this code?:

"""

from utils.brick import Motor
import time

# ------------------------- CONSTANTS ------------------------
print("ayo?")

ONE_SQUARE = 710
NINETY_DEGREES_LEFT = 338
NINETY_DEGREES_RIGHT = 330

# -------------------- SENSORS AND MOTORS --------------------
rightWheel = Motor("A")
leftWheel = Motor("D")

#rightWheel.set_limits(power=50,dps=425)
#leftWheel.set_limits(power=50,dps=425)
#rightWheel.reset_encoder()
#leftWheel.reset_encoder()

# -------------------- FUNCTIONS --------------------

def wiggle(amount):
    rightWheel.set_limits(power=20)
    leftWheel.set_limits(power=20)
    rightWheel.set_position_relative(amount)
    time.sleep(1)
    leftWheel.set_position_relative(amount)
    time.sleep(1)
    
    
if __name__ == "__main__":
    while (True):
        wiggle(180)
    