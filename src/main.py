from utils import sound
from utils.brick import TouchSensor, Motor, EV3UltrasonicSensor, wait_ready_sensors
import time
import threading

# ---------- MOTOR SETUP ----------
arm = Motor("C")
gripper = Motor("D")
arm.set_limits(power=30)
gripper.set_limits(power=30)

# ---------- CONSTANTS (angles at which we open/close) ----------
OPENED_GRIPPER = -50
CLOSED_GRIPPER = 0
RAISED_ARM = 180
LOWERED_ARM = 0

# ---------- FUNCTION DEFINITIONS ----------
def open_gripper():
    gripper.set_position(OPENED_GRIPPER)

def close_gripper():
    gripper.set_position(CLOSED_GRIPPER)
    
def raise_arm():
    arm.set_position(RAISED_ARM)

def lower_arm():
    arm.set_position(LOWERED_ARM)

def bring_cube_up():
    lower_arm()
    time.sleep(1)
    open_gripper()
    time.sleep(1)
    close_gripper()
    time.sleep(1)
    raise_arm()
    time.sleep(1)
    open_gripper()
    time.sleep(1)
    lower_arm()
    time.sleep(1)
    
def bring_cube_down():
    raise_arm()
    time.sleep(1)
    open_gripper()
    time.sleep(1)
    close_gripper()
    time.sleep(1)
    lower_arm()
    time.sleep(1)
    open_gripper()
    time.sleep(1)
    lower_arm()
    time.sleep(1)

# ---------- FUNCTION DEFINITIONS ----------
if __name__ == "__main__":
    bring_cube_up()
    bring_cube_down()

    # gripper.set_position(10)
    # time.sleep(1)
    # wrist.set_position(180)
    # time.sleep(1)
    # gripper.set_position(-50)
    # time.sleep(1)
    # wrist.set_position(0)
    # time.sleep(1)
    # gripper.set_position(10)
    # time.sleep(2)
    # gripper.set_position(-50)
    # wrist.set_position(185)
    # time.sleep(1)
    # gripper.set_position(10)
    # time.sleep(1)
    # wrist.set_position(0)
    # time.sleep(1)
    # gripper.set_position(-50)

    
        


    





