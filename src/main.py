from utils import sound
from utils.brick import TouchSensor, Motor, EV3ColorSensor, wait_ready_sensors
import time
import threading

from drive_system import *
from color_detection import all_colors, classify_unknown_color

# -------------------- SENSORS AND MOTORS --------------------
rightWheel = Motor("A")
leftWheel = Motor("B")

rightWheel.set_limits(power=50, dps=425)
leftWheel.set_limits(power=50, dps=425)
rightWheel.reset_encoder()
leftWheel.reset_encoder()

color_sensor = EV3ColorSensor(4)
touch_sensor = TouchSensor(2)

wait_ready_sensors(True)

def checkForBed():
    color = ""
    while color != "green bed" or color != "red bed":
        unknownColor = color_sensor.get_color()
        color = classify_unknown_color(unknownColor)

    return color

def traverseDoubleRoom():
    leftWheel.reset_encoder()
    rightWheel.reset_encoder()
    currentLeftWheelPosition = leftWheel.get_position()
    currentRightWheelPosition = rightWheel.get_position()

    turnRight(NINETY_DEGREES_RIGHT * 0.4)
    turnLeft(NINETY_DEGREES_LEFT * 0.6)

    turnLeft(NINETY_DEGREES_LEFT * 0.4)
    turnRight(NINETY_DEGREES_RIGHT * 0.6)

    turnRight(NINETY_DEGREES_RIGHT * 0.4)
    turnLeft(NINETY_DEGREES_LEFT * 0.6)

    turnLeft(NINETY_DEGREES_LEFT * 0.4)
    turnRight(NINETY_DEGREES_RIGHT * 0.6)turnRight(NINETY_DEGREES_RIGHT * 0.4)
    turnLeft(NINETY_DEGREES_LEFT * 0.6)

    turnLeft(NINETY_DEGREES_LEFT * 0.4)
    turnRight(NINETY_DEGREES_RIGHT * 0.6)

def findBedsInDoubleRoom():
    leftWheel.reset_encoder()
    rightWheel.reset_encoder()

if __name__ == "__main__":
    traverseDoubleRoom()