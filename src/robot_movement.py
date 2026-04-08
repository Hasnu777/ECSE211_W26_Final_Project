#!/usr/bin/python3
"""
Code insipred by example shown in BrickPi2 Slides by F.P. Ferrie, Ryan Au
"""

import time
import math
from utils.brick import Motor, EV3GyroSensor

MOTOR_POLL_DELAY = 0.05

SQUARE_LENGTH = 0.24   # (meters) Side length of square
WHEEL_RADIUS = 0.02  # (meters) Radius of one wheel
AXLE_LENGTH = 0.075   # (meters) Distance between wheel contacts

DIST_TO_DEG = 180 / (math.pi * WHEEL_RADIUS)
ORIENT_TO_DEG = AXLE_LENGTH / WHEEL_RADIUS

FWD_SPEED = 100   # (deg/sec)
TRN_SPEED = 180   # (deg/sec)

LEFT_WHEEL = Motor("D")
RIGHT_WHEEL = Motor("A")
GYRO = EV3GyroSensor(4, mode="both")

POWER_LIMIT = 80
SPEED_LIMIT = 720

RIGHT = "right"
LEFT = "left"




def wait_for_motor(motor: Motor):
    """Block until motor finishes motion"""
    while math.isclose(motor.get_speed(), 0):
        time.sleep(MOTOR_POLL_DELAY)
    while not math.isclose(motor.get_speed(), 0):
        time.sleep(MOTOR_POLL_DELAY)


def init_motor(motor: Motor):
    """Initialize motor"""
    try:
        motor.reset_encoder()
        motor.set_limits(POWER_LIMIT, SPEED_LIMIT)
        motor.set_power(0)
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

        
        #wait_for_motor(RIGHT_WHEEL)
    except IOError as error:
        print(error)


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


def arc_bot(angle, speed, direction):
    try:
        if direction == RIGHT:
            RIGHT_WHEEL.set_dps(0)
            LEFT_WHEEL.set_dps(speed)

            LEFT_WHEEL.set_limits(POWER_LIMIT, speed)
            LEFT_WHEEL.set_position_relative(int(angle * ORIENT_TO_DEG) * 2)
        elif direction == LEFT:
            LEFT_WHEEL.set_dps(0)
            RIGHT_WHEEL.set_dps(speed)

            RIGHT_WHEEL.set_limits(POWER_LIMIT, speed)
            RIGHT_WHEEL.set_position_relative(int(angle * ORIENT_TO_DEG) * 2)
    except IOError as error:
        print(error)



def find_gyro_diff(now, old):
    return now - old


def rotate_with_gyro_correction(turn_angle, speed, direction):
    """Rotate in place, but with gyro correction (angle (in abs value), speed direction)"""
    if direction == RIGHT:
        desired_turn_angle = turn_angle
    elif direction == LEFT:
        desired_turn_angle = -turn_angle

    GYRO.reset_measure()

    # Make the robot turn
    angle_before_turn = GYRO.get_abs_measure()
    angle_invalid = (angle_before_turn is None) #or not ((angle_before_turn < 180) and (angle_before_turn > -180)))
    while angle_invalid:
        print("reset gyro")
        GYRO.reset_measure()
        angle_before_turn = GYRO.get_abs_measure()
        angle_invalid = (angle_before_turn is None )#or not ((angle_before_turn < 180) and (angle_before_turn > -180)))

    rotate_bot(turn_angle, speed, direction)
    time.sleep(0.1)

    angle_after_turn = GYRO.get_abs_measure()

    
    actual_turn_angle = find_gyro_diff(angle_after_turn, angle_before_turn)
    print("actual_turn_angle: ", actual_turn_angle)

    delta = (actual_turn_angle - desired_turn_angle)  # delta between real and expected turn angles
    print("delta_expected_from_unexpected: ", delta)

    # split problem by direction
    if direction == RIGHT:
        if delta > 0: # if delta positive, robot overshooting
            print("Overshoot case")
            rotate_bot(delta, 100, LEFT)
            time.sleep(1)
        elif delta < 0: # if delta negative, robot undershooting
            print("Undershoot case")
            rotate_bot(delta, 100, LEFT)
            time.sleep(1)
    if direction == LEFT:
        if delta < 0: # if delta negative, robot overshooting
            print("Overshoot case")
            rotate_bot(delta, 100, LEFT)
            time.sleep(1)
        elif delta > 0: # if delta positive, robot undershooting
            print("Undershoot case")
            rotate_bot(delta, 100, LEFT)
            time.sleep(1)

    print("-------------------------------------------------")

def wiggle():
    for i in range (5):
        print(i)
        rotate_with_gyro_correction(50, 100, RIGHT)
        rotate_with_gyro_correction(50, 300, LEFT)
        move_dist_fwd(0.05, 100)
        time.sleep(0.3)
        
def maintain_angle(targetAngle):
    current = GYRO.get_abs_measure()
    while current not in range(targetAngle-1 , targetAngle +1):
        current = GYRO.get_abs_measure()
        if current != None:
            error = targetAngle - current
            correction = error * 0.5
            RIGHT_WHEEL.set_position_relative(-correction)
            LEFT_WHEEL.set_position_relative(correction)
            
if __name__ == "__main__":
    wiggle()