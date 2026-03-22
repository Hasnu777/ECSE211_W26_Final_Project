from utils import sound
from utils.brick import EV3ColorSensor, TouchSensor, wait_ready_sensors, reset_brick
from time import sleep
import threading
import csv

# CONSTANTS
COLOR_SENSOR = EV3ColorSensor(1)
TOUCH_SENSOR = TouchSensor(2)
DataFile = "calibration_blue.csv"

wait_ready_sensors(True)

NUM_READINGS = 1000

def collect_color_data():
    try:
        with open(DataFile, "a", newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["R", "G", "B"])

            print("Press touch sensor to begin collecting data...")
            while not TOUCH_SENSOR.is_pressed():
                pass

            print(f"Pressed. Collecting {NUM_READINGS} readings...")
            count = 0
            while count < NUM_READINGS:
                data = COLOR_SENSOR.get_rgb()
                if data is not None:
                    writer.writerow(data)
                    count += 1
                    print(f"  [{count}/{NUM_READINGS}]  R={data[0]}  G={data[1]}  B={data[2]}", end="\r")
                else:
                    print("\nColor sensor failed to read, retrying...")
                sleep(0.05)

            print(f"\nDone! {NUM_READINGS} readings saved to {DataFile}")

    except BaseException as e:
        print("Exception occurred:", e)
    finally:
        csvfile.close()
        reset_brick()
        exit()


if __name__ == "__main__":
    collect_color_data()