from utils import sound
from utils.brick import TouchSensor, Motor, EV3ColorSensor, wait_ready_sensors
from time import sleep
import threading

from drive_system import *
from color_detection import all_colors, classify_unknown_color

# ------------------------ CONSTANTS -------------------------
WIGGLE = NINETY_DEGREES_LEFT * 0.4
WIGGLE_COMPLETION = NINETY_DEGREES_LEFT * 0.6

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
    print("WHOA BED DETECTED OH EM GEE!")
    return color

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

#     turnRight(NINETY_DEGREES_RIGHT * 0.4)
#     turnLeft(NINETY_DEGREES_LEFT * 0.6)
# 
#     turnLeft(NINETY_DEGREES_LEFT * 0.4)
#     turnRight(NINETY_DEGREES_RIGHT * 0.6)
# 
#     turnLeft(NINETY_DEGREES_LEFT * 0.4)
#     turnRight(NINETY_DEGREES_RIGHT * 0.6)

def findBedsInDoubleRoom():
    pass

if __name__ == "__main__":
    traverseDoubleRoom()

#     color_finder = threading.Thread(target=checkForBed())
#     room_traversing = threading.Thread(target=traverseDoubleRoom())
    