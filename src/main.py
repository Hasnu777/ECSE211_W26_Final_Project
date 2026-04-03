from utils import sound
from utils import brick
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
    time.sleep(1)
    # Align claw to left block
    rotate_with_gyro_correction(10, 300, LEFT) # in-built time.sleep()
    # claw_arm.set_position(0)
    # claw_gripper.set_position(-100)
    # Move towards left block
    move_dist_fwd(SQUARE_LENGTH * 0.4, 425)
    time.sleep(3)
    # Left block in reach, store it
    store_cube() # in-built time.sleep()
    # Move back
    move_dist_fwd(-SQUARE_LENGTH * 3/8, 425)
    time.sleep(3)
    # Align claw to right block
    rotate_with_gyro_correction(25, 300, RIGHT) # in-built time.sleep()
    # Prepare for receival
    claw_gripper.set_position(-100)
    time.sleep(1)
    # Move towards right block
    move_dist_fwd(SQUARE_LENGTH * (3/8+0.05), 425)
    time.sleep(3)
    # Grab instead of store, storage full
    grab_cube() # in-built time.sleep()
    move_dist_fwd(-SQUARE_LENGTH * 5.5/8, 425)
    time.sleep(2)
    # Re-align to initial alignment
    rotate_with_gyro_correction(20, 300, LEFT) #in-built time.sleep()
    # NEED TO TEST - Want to get robot in alignment with right line going outside of pharmacy
    move_dist_fwd(SQUARE_LENGTH * -2/12, 425)
    time.sleep(3)
    
    rotate_with_gyro_correction(90,300, LEFT) # in-built time.sleep()
    rotate_with_gyro_correction(4,300, RIGHT) # for use with low battery power


def pharmacy_to_left_single():
    # Move out of pharmacy to intersection
    move_dist_fwd(SQUARE_LENGTH * 2, 425)
    rotate_with_gyro_correction(30, 300, LEFT)
    move_dist_fwd(SQUARE_LENGTH * 0.2, 425)
    rotate_with_gyro_correction(30,300,RIGHT)
    time.sleep(3)
    move_dist_fwd(SQUARE_LENGTH * 1.5, 425)
    # Turn left at intersection
#     rotate_with_gyro_correction(90, 300, LEFT) # in-built time.sleep()
#     # Move to next intersection
#     move_dist_fwd(SQUARE_LENGTH * 1, 425)
#     time.sleep(3)
#     # Face single room
#     rotate_with_gyro_correction(90, 300, RIGHT) # in-built time.sleep()
#     # Approach single room
#     move_dist_fwd(SQUARE_LENGTH * 0.5, 425)
#     time.sleep(3)
    
    
if __name__ == "__main__":
#     claw_arm.set_position(-10)
#     claw_arm.reset_encoder()
    LEFT_WHEEL.set_limits(power=POWER_LIMIT, dps=425)
    RIGHT_WHEEL.set_limits(power=POWER_LIMIT, dps=425)
    # Step 1: Starting position -> collected med packages
    getMeds()
    # Step 2: pharmacy -> left single room
    pharmacy_to_left_single()