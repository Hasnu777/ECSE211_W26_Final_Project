"""
Purpose of this files: Testing if the ports work
How to test with this code?:

"""

import utils.sound as sound
from utils.brick import TouchSensor, Motor, EV3UltrasonicSensor, wait_ready_sensors
from time import sleep
import threading

# ------------------------- CONSTANTS ------------------------

ONE_SQUARE = 710
NINETY_DEGREES_LEFT = 338
NINETY_DEGREES_RIGHT = 330

# -------------------- SENSORS AND MOTORS --------------------
rightWheel = Motor("C")
leftWheel = Motor("D")

rightWheel.set_limits(power=50,dps=425)
leftWheel.set_limits(power=50,dps=425)
rightWheel.reset_encoder()
leftWheel.reset_encoder()

# -------------------- FUNCTIONS --------------------

def moveForward(amount):
    rightWheel.set_position_relative(amount)
    leftWheel.set_position_relative(amount)
    print(f"Moved forward {amount / ONE_SQUARE} blocks.")

def moveBackward(amount):
    rightWheel.set_position_relative(-amount)
    leftWheel.set_position_relative(-amount)
    print(f"Moved backward {amount / ONE_SQUARE} blocks.")

def turnRight(amount):
    leftWheel.set_limits(power=30,dps=300)
    rightWheel.set_limits(power=30,dps=300)
    leftWheel.set_position_relative(amount)
    rightWheel.set_position_relative(-amount)
    leftWheel.set_limits(power=50,dps=425)
    rightWheel.set_limits(power=50,dps=425)
    print(f"Turned right by { 90 * (amount / NINETY_DEGREES_LEFT)} degrees.")

def turnLeft(amount):
    leftWheel.set_limits(power=30,dps=300)
    rightWheel.set_limits(power=30,dps=300)
    rightWheel.set_position_relative(amount)
    leftWheel.set_position_relative(-amount)
    rightWheel.set_limits(power=50,dps=425)
    leftWheel.set_limits(power=50,dps=425)
    print(f"Turned left by {90 * (amount / NINETY_DEGREES_LEFT)} degrees.")

def arcRight(amount):
    leftWheel.set_limits(power=30, dps=300)
    rightWheel.set_dps(0)
    leftWheel.set_position_relative(amount)
    leftWheel.set_limits(power=50, dps=425)


def arcLeft(amount):
    rightWheel.set_limits(power=30, dps=300)
    leftWheel.set_dps(0)
    rightWheel.set_position_relative(amount)
    rightWheel.set_limits(power=50, dps=425)


def traverseDoubleRoom():
    leftWheel.reset_encoder()
    rightWheel.reset_encoder()
    currentLeftWheelPosition = leftWheel.get_position()
    currentRightWheelPosition = rightWheel.get_position()

    arcRight(NINETY_DEGREES_RIGHT * 0.8)
    sleep(1)
    arcLeft(NINETY_DEGREES_LEFT * 0.8)
    sleep(1)
    arcLeft(NINETY_DEGREES_LEFT * 0.8)
    sleep(1)
    moveForward(ONE_SQUARE * 0.1)
    sleep(1)
    arcRight(NINETY_DEGREES_RIGHT * 0.8)
    sleep(1)
    arcRight(NINETY_DEGREES_RIGHT * 0.8)
    sleep(1)
    moveForward(ONE_SQUARE * 0.1)
    sleep(1)
    arcLeft(NINETY_DEGREES_LEFT * 0.8)
    sleep(1)
    arcLeft(NINETY_DEGREES_LEFT * 0.8)
    sleep(1)
    moveForward(ONE_SQUARE * 0.1)
    sleep(1)
    arcRight(NINETY_DEGREES_RIGHT * 0.8)
    sleep(1)

def main():
    rightWheel.reset_encoder()
    leftWheel.reset_encoder()
    moveForward(ONE_SQUARE * 2)