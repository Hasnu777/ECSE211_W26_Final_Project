from utils import sound
from utils.brick import TouchSensor, Motor, EV3UltrasonicSensor, wait_ready_sensors
import time
import threading
from robot_movement import *

# MOTOR SETUP
claw_gripper = Motor("B")
claw_arm = Motor("C")

claw_gripper.set_limits(power=30)
claw_arm.set_limits(power=30)

# CONSTANTS
OPEN_GRIPPER = -50
CLOSED_GRIPPER = 0
RAISED_ARM = 180
LOWERED_ARM = 0


# FUNCTIONS


def open_gripper():
    claw_gripper.set_position(OPEN_GRIPPER)


def close_gripper():
    claw_gripper.set_position(CLOSED_GRIPPER)


def raise_arm():
    claw_arm.set_position(RAISED_ARM)


def lower_arm():
    claw_arm.set_position(LOWERED_ARM)


def grab_cube():
    # Open gripper
    open_gripper()
#     wait_for_motor(claw_gripper)
    time.sleep(1)
    # Grab cube
    close_gripper()
#     wait_for_motor(claw_gripper)
    time.sleep(1)


def release_cube():
    # Release cube
    open_gripper()
#     wait_for_motor(claw_gripper)
    time.sleep(1)
    # Close gripper
#     close_gripper()
#     wait_for_motor(claw_gripper)
#     time.sleep(1)


def store_cube():
    # Lower the arm
    lower_arm()
#     wait_for_motor(claw_arm)
    time.sleep(1)
    # Grab cube
    grab_cube()
    # Raise the arm
    raise_arm()
#     wait_for_motor(claw_arm)
    time.sleep(1)
    # Release cube
    release_cube()
    # Lower the arm
    lower_arm()
#     wait_for_motor(claw_arm)
    time.sleep(1)
    # Close the gripper
    close_gripper()
    time.sleep(1)


def retrieve_cube():
    # Raise the arm
    raise_arm()
#     wait_for_motor(claw_arm)
    time.sleep(1)
    # Grab cube
    grab_cube()
    # Lower the arm
    lower_arm()
#     wait_for_motor(claw_arm)
    time.sleep(1)



