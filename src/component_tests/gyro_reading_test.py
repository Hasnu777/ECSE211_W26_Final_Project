import math
from utils.brick import Motor, EV3GyroSensor, wait_ready_sensors
import time

MOTOR_POLL_DELAY = 0.05

SQUARE_LENGTH = 0.5   # (meters) Side length of square
WHEEL_RADIUS = 0.02  # (meters) Radius of one wheel
AXLE_LENGTH = 0.075   # (meters) Distance between wheel contacts

DIST_TO_DEG = 180 / (math.pi * WHEEL_RADIUS)
ORIENT_TO_DEG = AXLE_LENGTH / WHEEL_RADIUS

LEFT_WHEEL = Motor("D")
RIGHT_WHEEL = Motor("A")
GYRO = EV3GyroSensor(4, mode="both")

POWER_LIMIT = 80
SPEED_LIMIT = 720

RIGHT = "right"
LEFT = "left"

wait_ready_sensors(True)
print("Sensors initialized.")

def gyro_setup():
    LEFT_WHEEL.set_limits(power=50)
    RIGHT_WHEEL.set_limits(power=50)

    GYRO.set_mode("abs")
    wait_ready_sensors()
    GYRO.reset_measure()

    initialState = GYRO.get_abs_measure()
    print("Initial state: ", initialState)

    # Making sure the initial state is 0
    while initialState is None or not 0:
        if initialState == 0:
            break
        GYRO.reset_measure()
        initialState = GYRO.get_abs_measure()
        print(initialState)
        if initialState == 0:
            break


def wait_for_motor(motor: Motor):
    """Block until motor finishes motion"""
    while math.isclose(motor.get_speed(), 0):
        time.sleep(MOTOR_POLL_DELAY)
    while not math.isclose(motor.get_speed(), 0):
        time.sleep(MOTOR_POLL_DELAY)


def rotate_bot(angle, speed, direction):
    """Rotate in place (degrees, dps, "right"/"left")"""
    try:
        LEFT_WHEEL.set_dps(speed)
        RIGHT_WHEEL.set_dps(speed)

        LEFT_WHEEL.set_limits(POWER_LIMIT, speed)
        RIGHT_WHEEL.set_limits(POWER_LIMIT, speed)

        if direction == RIGHT:
            LEFT_WHEEL.set_position_relative(int(angle * ORIENT_TO_DEG))
            RIGHT_WHEEL.set_position_relative(-int(angle * ORIENT_TO_DEG))
        elif direction == LEFT:
            LEFT_WHEEL.set_position_relative(-int(angle * ORIENT_TO_DEG))
            RIGHT_WHEEL.set_position_relative(int(angle * ORIENT_TO_DEG))

        wait_for_motor(RIGHT_WHEEL)
    except IOError as error:
        print(error)

def move_dist_fwd(distance, speed):
    """Move forward (meters, dps)"""
    try:
        LEFT_WHEEL.set_dps(speed)
        RIGHT_WHEEL.set_dps(speed)

        LEFT_WHEEL.set_limits(POWER_LIMIT, speed)
        RIGHT_WHEEL.set_limits(POWER_LIMIT, speed)

        LEFT_WHEEL.set_position_relative(int(distance * DIST_TO_DEG))
        RIGHT_WHEEL.set_position_relative(int(distance * DIST_TO_DEG))

        wait_for_motor(RIGHT_WHEEL)
    except IOError as error:
        print(error)

if __name__ == "__main__":
    gyro_setup()

    # Test Gyro reading in straight line
    print("Gyro measurement before straight line: ", GYRO.get_abs_measure())
    move_dist_fwd(10, 300)
    print("Gyro measurement after straight line: ", GYRO.get_abs_measure())

    # Test Gyro reading after turn
    print("Gyro measurement before 90deg turn: ", GYRO.get_abs_measure())
    rotate_bot(90, 300, RIGHT)
    print("Gyro measurement after 90 deg turn: ", GYRO.get_abs_measure())

