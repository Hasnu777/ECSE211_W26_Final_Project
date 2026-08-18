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
CLOSED_GRIPPER = 10
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
    time.sleep(0.5)
    open_gripper()
    time.sleep(0.5)
    close_gripper()
    time.sleep(0.5)
    
    # lift the arm a little bit so that it doesn't catch on to anything
    claw_arm.set_position(10)
    time.sleep(0.3)


def release_cube():
    open_gripper()
    time.sleep(0.3)


def store_cube():
    lower_arm()
    time.sleep(0.1)

    grab_cube()

    raise_arm()
    time.sleep(0.8)

    release_cube()

    lower_arm()
    time.sleep(0.1)

    close_gripper()
    time.sleep(1)


def retrieve_cube():
    open_gripper()
    time.sleep(1)
    raise_arm()
    time.sleep(1)
    grab_cube()
    lower_arm()
    time.sleep(1)



