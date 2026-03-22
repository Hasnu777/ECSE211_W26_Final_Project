from utils import sound
from utils.brick import TouchSensor, Motor, EV3UltrasonicSensor, wait_ready_sensors
import time
import threading

# ---------- MOTOR SETUP ----------
leftWheel = Motor("B")
rightWheel = Motor("A")
arm = Motor("C")
gripper = Motor("D")
leftWheel.set_limits(power=30)
rightWheel.set_limits(power=30)
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
    
def moveForward(seconds):
    print('starting to move forward')
    leftWheel.set_dps(400)
    rightWheel.set_dps(400)
    print('going for', seconds,'seconds')
    time.sleep(seconds)
    print('stopping...')
    leftWheel.set_dps(0)
    rightWheel.set_dps(0)
    print('stopped')
    
def turnRight():
    print('starting to turn right')
    leftWheel.set_dps(0)
    rightWheel.set_dps(0)
    print('turning...')
    leftWheel.set_position_relative(1200)
    print('turned')

def turnLeft():
    print('starting to turn left')
    leftWheel.set_dps(0)
    rightWheel.set_dps(0)
    print('turning...')
    rightWheel.set_position_relative(610)
    print('turned')
    
def moveBackwards(seconds):
    print('starting to move backwards')
    leftWheel.set_dps(-400)
    rightWheel.set_dps(-400)
    print('moving now')
    time.sleep(seconds)
    print('stopping...')
    leftWheel.set_dps(0)
    rightWheel.set_dps(0)
    print('stopped')
    
def spin(seconds):
    print('starting to spin')
    leftWheel.set_dps(400)
    rightWheel.set_dps(-400)
    print('spinning')
    time.sleep(seconds)
    print('stopping...')
    leftWheel.set_dps(0)
    rightWheel.set_dps(0)
    print('stopped')
    
def testMovement():
    moveForward(3)
    time.sleep(1)
    turnRight()
    time.sleep(1)
    turnLeft()
    time.sleep(1)
    turnLeft()
    time.sleep(1)
    turnRight()
    time.sleep(1)
    moveBackwards(3)
    moveForward(3)
    spin(5)

# ---------- FUNCTION DEFINITIONS ----------
if __name__ == "__main__":
#     try:
# #         leftWheel.set_dps(0)
# #         rightWheel.set_dps(0)
# #         arm.set_dps(0)
# #         gripper.set_dps(0)
#         print('resetting')
#         leftWheel.reset_encoder()
#         time.sleep(1)
#         print('reset left')
#         rightWheel.reset_encoder()
#         time.sleep(1)
#         print('reset right')
#         arm.reset_encoder()
#         time.sleep(1)
#         print('reset arm')
#         print('done')
#     finally:
#         print('entered finally block')
#         leftWheel.reset_encoder()
#         print('left wheel has been reset')
#         time.sleep(1)
#         rightWheel.reset_encoder()
#         print('right wheel has been reset')
#         time.sleep(1)
#         arm.reset_encoder()
#         print('arm has been reset')
#         print('done')
        
    try:
        leftWheel.set_dps(0)
        rightWheel.set_dps(0)
        print('testing movement with downwards arm')
        open_gripper()
        time.sleep(4)
        testMovement()
        print('moving arm up')
        time.sleep(1)
        
        raise_arm()
        time.sleep(5)
        close_gripper()
        
#         bring_cube_up()
        print('testing movement with upwards arm')
        testMovement()
#         bring_cube_down()
        lower_arm()
        close_gripper()
        time.sleep(1)
        testMovement()
    finally:
        print('stoppong.............')
        leftWheel.set_dps(0)
        rightWheel.set_dps(0)
        arm.set_dps(0)
        gripper.set_dps(0)
        leftWheel.reset_encoder()
        rightWheel.reset_encoder()

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

    
        


    





