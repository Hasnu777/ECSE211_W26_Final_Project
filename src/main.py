from utils import sound
from utils.brick import TouchSensor, Motor, EV3UltrasonicSensor, EV3GyroSensor, wait_ready_sensors
import time
import threading
from robot_movement import *
from robot_claw_mechanism import *
from robot_sound_system import *

#open_gripper()

def getMeds():
    # Prepare claw to receive blocks
    open_gripper()
    time.sleep(0.5)
    # Align claw to left block
    rotate_with_gyro_correction(10, 300, LEFT) # in-built time.sleep()
    # claw_arm.set_position(0)
    # claw_gripper.set_position(-100)
    # Move towards left block
    move_dist_fwd(SQUARE_LENGTH * 0.4, 425)
    time.sleep(1)
    # Left block in reach, store it
    store_cube() # in-built time.sleep()
    # Move back
    move_dist_fwd(-SQUARE_LENGTH * -3/8, 425)
    time.sleep(1)
    # Align claw to right block
    rotate_with_gyro_correction(20, 300, RIGHT) # in-built time.sleep()
    # Prepare for receival
    open_gripper()
    time.sleep(0.5)
    # Move towards right block
    move_dist_fwd(SQUARE_LENGTH * 3/8, 425)
    time.sleep(1)
    # Grab instead of store, storage full
    grab_cube() # in-built time.sleep()
    # Re-align to initial alignment
    rotate_with_gyro_correction(10, 300, LEFT) #in-built time.sleep()
    # NEED TO TEST - Want to get robot in alignment with right line going outside of pharmacy
    move_dist_fwd(SQUARE_LENGTH * 0.15, 425)
    time.sleep(1)
    rotate_with_gyro_correction(90,300, LEFT) # in-built time.sleep()


def pharmacy_to_left_single():
    # Move out of pharmacy to intersection
    move_dist_fwd(SQUARE_LENGTH * 1.5, 425)
    # Turn left at intersection
    rotate_with_gyro_correction(90, 300, LEFT)
    # Move to next intersection
    move_dist_fwd(SQUARE_LENGTH * 1, 425)
    # Face single room
    rotate_with_gyro_correction(90, 300, RIGHT)
    # Approach single room
    move_dist_fwd(SQUARE_LENGTH * 0.5, 425)

if __name__ == "__main__":

    LEFT_WHEEL.set_limits(power=POWER_LIMIT, dps=425)
    RIGHT_WHEEL.set_limits(power=POWER_LIMIT, dps=425)
    # Step 1: Starting position -> collected med packages
    getMeds()