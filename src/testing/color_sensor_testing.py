from utils import sound
from utils.brick import EV3ColorSensor, TouchSensor, wait_ready_sensors, reset_brick
from time import sleep
import threading
import csv

# CONSTANTS
ColorSensor = EV3ColorSensor(1)
TouchSensor = TouchSensor(2)
DataFile = "calibration_data_intersect.csv"

wait_ready_sensors(True)

def collect_color_data():
    try:
        with open(DataFile, "a", newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["R", "G", "B"])
            print("Press touch sensor to read color data")
            while not TouchSensor.is_pressed():
                pass
            print("Pressed. Reading data now in 2 second intervals.")
            count = 0
            while count < 30:
                if not TouchSensor.is_pressed():
                    data = ColorSensor.get_rgb()
                    if data is not None:
                        writer.writerow(data)
                        count += 1
                    else:
                        print("Color failed to read, try again.")
                    sleep(2)
    except BaseException as e:
        print("Exception occurred:", e)
    finally:
        csvfile.close()
        reset_brick()
        exit()

if __name__ == "__main__":
    collect_color_data()