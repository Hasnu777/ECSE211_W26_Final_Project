
from utils import sound
from utils.brick import TouchSensor, Motor, EV3UltrasonicSensor, EV3GyroSensor, wait_ready_sensors, reset_brick
import time
import threading

TS1 = TouchSensor(2)
Gyro = EV3GyroSensor(3,mode="both")
motor_R = Motor("A")
motor_L = Motor("C")

motor_R.set_dps(0)
motor_L.set_dps(0)

print("Testing file running. Waiting for sensor initialisation...")

wait_ready_sensors(True)
print("Sensors initialized.")


def perform_rotations():

    motor_R.set_limits(power=50)
    motor_L.set_limits(power=50)

    Gyro.set_mode("abs")

    wait_ready_sensors()

    Gyro.reset_measure()

    initialState = Gyro.get_abs_measure()
    print(initialState)


def print_continuous_gyro_data():
    try:
        while not TS1.is_pressed():
            pass
        time.sleep(0.5)
        print("Collecting readings now.")
        Gyro.reset_measure()
        while not TS1.is_pressed():
            time.sleep(3)
            gyro_data = Gyro.get_abs_measure()
            if gyro_data is not None:
                print(gyro_data)
            time.sleep(0.5)
    except BaseException as e:
        pass
    finally:
        print("Gyro samples collected.")
        print("Testing complete.")
        reset_brick()
        exit()

def maintain_angle():
    Gyro.reset_measure()
    target = Gyro.get_abs_measure()
    while True:
        current = Gyro.get_abs_measure()
        error = target - current
        correction = error * 0.5
        time.sleep(0.1)
        motor_R.set_dps(correction)
        motor_L.set_dps(-correction)
        time.sleep(0.1)

if __name__ == "__main__":
    #maintain_angle()