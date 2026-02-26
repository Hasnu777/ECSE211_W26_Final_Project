from utils import sound
from utils.brick import TouchSensor, Motor, EV3UltrasonicSensor, EV3GyroSensor, wait_ready_sensors, reset_brick
import time
import threading

TS1 = TouchSensor(2)
Gyro = EV3GyroSensor(1,mode="both")

GYRO_SENSOR_DATA_FILE = "gyro_sensor_data_file_for_consistency.csv"

print("Testing file running. Waiting for sensor initialisation...")

wait_ready_sensors(True)
print("Sensors. Initialized.")

def collect_continuous_gyro_data():
    try:
        output_file = open(GYRO_SENSOR_DATA_FILE,"w")
        output_file.write(f"Degrees Rotated Since Beginning,Degrees Rotated Per Second\n")
        while not TS1.is_pressed():
            pass
        time.sleep(0.5)
        print("Collecting readings now.")
        Gyro.reset_measure()
        while not TS1.is_pressed():
            gyro_data = Gyro.get_both_measure()
            if gyro_data is not None:
                print(gyro_data)
                output_file.write(f"{gyro_data[0]},{gyro_data[1]}\n")
            time.sleep(0.5)
    except BaseException as e:
        pass
    finally:
        print("Gyro samples collected.")
        output_file.close()
        print("Testing complete.")
        reset_brick()
        exit()

if __name__ == "__main__":
    collect_continuous_gyro_data()