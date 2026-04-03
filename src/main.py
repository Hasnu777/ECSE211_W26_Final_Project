from utils import sound
from utils.brick import TouchSensor, Motor, EV3UltrasonicSensor, EV3GyroSensor, wait_ready_sensors
import time
import threading
from robot_movement import *
from robot_claw_mechanism import *
from robot_sound_system import *

#open_gripper()

def getMeds():
    open_gripper()
    rotate_with_gyro_correction(10, LEFT)
    claw_arm.set_position(0)
    claw_gripper.set_position(-100)
    
    move_dist_fwd(SQUARE_LENGTH * 0.4, 425)
    store_cube()
    move_dist_fwd(-SQUARE_LENGTH * -3/8, 425)
    rotate_with_gyro_correction(20, RIGHT)
    open_gripper()
    move_dist_fwd(SQUARE_LENGTH * 3/8, 425)
    grab_cube()
    rotate_with_gyro_correction(10, LEFT)
    move_dist_fwd(SQUARE_LENGTH * 0.15, 425)
    rotate_with_gyro_correction(90,LEFT)
    move_dist_fwd(SQUARE_LENGTH * 1.5, 425)
#     move_dist_fwd(SQUARE_LENGTH * 0.5, 425)
#     time.sleep(1)
#     store_cube()
#     time.sleep(1)
#     move_dist_fwd(-SQUARE_LENGTH * 2/11, 425)
#     time.sleep(1)
#     rotate_with_gyro_correction(35, RIGHT)
#     time.sleep(1)
#     open_gripper()
#     move_dist_fwd(SQUARE_LENGTH * 5/22, 425)
#     time.sleep(1)
#     grab_cube()
#     move_dist_fwd(SQUARE_LENGTH * 1/24, 425)
#     rotate_with_gyro_correction(135, LEFT)
#     move_dist_fwd(SQUARE_LENGTH * 0.5, 425)


if __name__ == "__main__":
    
#     init_motor(LEFT_WHEEL)
#     init_motor(RIGHT_WHEEL)
    LEFT_WHEEL.set_limits(power=POWER_LIMIT, dps=425)
    RIGHT_WHEEL.set_limits(power=POWER_LIMIT, dps=425)
    # Step 1: Starting position -> collected med packages
    getMeds()
#     move_dist_fwd(SQUARE_LENGTH,425)