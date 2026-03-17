from src.utils import sound
from src.utils.brick import EV3ColorSensor, TouchSensor, wait_ready_sensors, reset_brick
from time import sleep
import threading
import csv

# CONSTANTS
ColorSensor = EV3ColorSensor(1)
TouchSensor = TouchSensor(2)
DataFile = "../data/calibration_data_v1.csv" # Change data file if needed

wait_ready_sensors(True)

def collect_color_data():
    try:
        with open(DataFile, "a", newline='') as csvfile:
            # csv module
            writer = csv.writer(csvfile)
            # headers
            writer.writerow(["R", "G", "B"])
            print("Press touch sensor to read color data")
            while not TouchSensor.is_pressed():
                pass
            print("Pressed. Reading data now in 3 second intervals.")
            while True:
                # Press to stop, meanwhile read in 3 second intervals
                if not TouchSensor.is_pressed():
                    data = ColorSensor.get_rgb()
                    if data is not None:
                        writer.writerow(data)
                    else:
                        print("Color failed to read, try again.")
                    sleep(3)
    except BaseException as e:
        print("Exception occurred:", e)
    finally:
        # Close & save file, reset brick
        csvfile.close()
        reset_brick()
        exit()

if __name__ == "__main__":
    collect_color_data()