
from utils import sound
from utils.brick import TouchSensor, Motor, EV3UltrasonicSensor, EV3GyroSensor, wait_ready_sensors, reset_brick
import time
from threading import Thread

TS1 = TouchSensor(2)
Gyro = EV3GyroSensor(4,mode="both")
motor_R = Motor("A")
motor_L = Motor("D")

motor_C = Motor("C")
motor_C.set_dps(0)

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


def continuous_measure_gyro():
    global target
    while True:
        target = Gyro.get_abs_measure()

def maintain_angle(target):
    Gyro.reset_measure()
    while True:
        current = Gyro.get_abs_measure()
        if current != None:
            error = target - current
            correction = error * 0.5
            motor_R.set_position_relative(-correction)
            motor_L.set_position_relative(correction)

if __name__ == "__main__":
#     print_continuous_gyro_data()
#     target = Gyro.get_abs_measure()
#     Gyro.reset_measure()
#     maintain_angle(target)
    target = 0
    t1 = Thread(target = continuous_measure_gyro())
    t1.start()
    while True:
        print(target)
        if TS1.is_pressed():
            t1.join()
            break
    # print("reset")
