from utils import sound
from utils.brick import TouchSensor, Motor, EV3UltrasonicSensor, EV3GyroSensor, wait_ready_sensors
import time
import threading
from robot_movement import *
from robot_claw_mechanism import *
from robot_sound_system import *


def getMeds():
    move_dist_fwd(SQUARE_LENGTH * 0.55, SPEED_LIMIT)
    store_cube()
    move_dist_fwd(-SQUARE_LENGTH * 2/11, 425)
    rotate_with_gyro_correction(45, RIGHT)
    move_dist_fwd(SQUARE_LENGTH * 5/22, 425)
    grab_cube()
    rotate_with_gyro_correction(135, LEFT)
    move_dist_fwd(SQUARE_LENGTH * 0.5, 425)


if __name__ == "__main__":
    init_motor(LEFT_WHEEL)
    init_motor(RIGHT_WHEEL)
    # Step 1: Starting position -> collected med packages
    getMeds()