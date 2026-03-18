from src.utils import sound
from src.utils.brick import TouchSensor, Motor, EV3UltrasonicSensor, wait_ready_sensors, EV3ColorSensor
import time
import threading

if __name__ == "__main__":
    while True:
        color = color_class():
        if color == "line":
            print("line detected")
        elif color == "intersect":
            print("intersection detected")
        elif color == "white":
            print("line lost. Wiggling now")
            wiggle()
        elif color == "orange":
            print("door found")
        elif color == "yellow":
            print("in patient room")
        elif color == "blue":
            print("in med bay")
        elif color == "green":
            print("sick patient found, giving medication")
            #drop medication
        elif color == "red":
            print("healthy patient found")
