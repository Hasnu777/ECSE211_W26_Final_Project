from testing.unit_tests.utils.brick import TouchSensor, Motor, EV3GyroSensor, wait_ready_sensors
import time

TS1 = TouchSensor(2)
Gyro = EV3GyroSensor(3)
motor1 = Motor("A")
motor2 = Motor("D")

motor1.set_dps(0)
motor2.set_dps(0)

# GYRO_SENSOR_DATA_FILE = "gyro_sensor_straight.txt"

# print("Testing file running. Waiting for sensor initialisation...")

wait_ready_sensors(True)
print("Sensors initialized.")

# file = open(GYRO_SENSOR_DATA_FILE, mode="a")


def perform_rotations():
    #     motor1.float_motor()
    #     motor2.float_motor()
    motor1.set_limits(power=50)
    motor2.set_limits(power=50)

    Gyro.set_mode("abs")

    wait_ready_sensors()

    Gyro.reset_measure()

    initialState = Gyro.get_abs_measure()
    print(initialState)

    #     if initialState is None:
    #         print("weird")
    while initialState is None or not 0:
        if initialState == 0:
            break
        Gyro.reset_measure()
        initialState = Gyro.get_abs_measure()
        print(initialState)
        if initialState == 0:
            break

    # file.write("Initial state: 0\n")


if __name__ == "__main__":
    perform_rotations()
    for i in range(10):
        motor1.set_dps(360)
        motor2.set_dps(360)
        print(Gyro.get_abs_measure())
        # file.write(str(Gyro.get_abs_measure()) + "\n")
        time.sleep(1)

    motor1.set_dps(0)
    motor2.set_dps(0)


    # file.close()