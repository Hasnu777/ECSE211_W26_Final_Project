#!/usr/bin/python3
"""
DPM Hands On Example 4 (Lecture 10) - SquareDriver

A simple program that drives a two-wheeled robot along a square trajectory
with size specified by the user. Program will execute prompt-drive loop
until halted with ^C.

Author: F.P. Ferrie, Ryan Au
Date: January 13th, 2022
"""

from cmath import isclose
import time
import math
from utils import brick
from utils.brick import BP, Motor, EV3GyroSensor

MOTOR_POLL_DELAY = 0.05

SQUARE_LENGTH = 0.5   # (meters) Side length of square
WHEEL_RADIUS = 0.0205  # (meters) Radius of one wheel
AXLE_LENGTH = 0.075   # (meters) Distance between wheel contacts

DIST_TO_DEG = 180 / (math.pi * WHEEL_RADIUS)
ORIENT_TO_DEG = AXLE_LENGTH / WHEEL_RADIUS

FWD_SPEED = 100   # (deg/sec)
TRN_SPEED = 180   # (deg/sec)

LEFT_MOTOR = Motor("A")
RIGHT_MOTOR = Motor("D")
GYRO = EV3GyroSensor(4, mode="both")

POWER_LIMIT = 80
SPEED_LIMIT = 720


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
        LEFT_MOTOR.set_dps(speed)
        RIGHT_MOTOR.set_dps(speed)

        LEFT_MOTOR.set_limits(POWER_LIMIT, speed)
        RIGHT_MOTOR.set_limits(POWER_LIMIT, speed)

        LEFT_MOTOR.set_position_relative(int(distance * DIST_TO_DEG))
        RIGHT_MOTOR.set_position_relative(int(distance * DIST_TO_DEG))

        wait_for_motor(RIGHT_MOTOR)
    except IOError as error:
        print(error)


def rotate_bot(angle, speed):
    """Rotate in place (degrees, dps)"""
    try:
        LEFT_MOTOR.set_dps(speed)
        RIGHT_MOTOR.set_dps(speed)

        LEFT_MOTOR.set_limits(POWER_LIMIT, speed)
        RIGHT_MOTOR.set_limits(POWER_LIMIT, speed)

        LEFT_MOTOR.set_position_relative(int(angle * ORIENT_TO_DEG))
        RIGHT_MOTOR.set_position_relative(-int(angle * ORIENT_TO_DEG))

        wait_for_motor(RIGHT_MOTOR)
    except IOError as error:
        print(error)


def turnRight(angle, speed):
    """Rotate in place (degrees, dps)"""
    try:
        LEFT_MOTOR.set_dps(speed)
        RIGHT_MOTOR.set_dps(speed)

        LEFT_MOTOR.set_limits(POWER_LIMIT, speed)
        RIGHT_MOTOR.set_limits(POWER_LIMIT, speed)

        LEFT_MOTOR.set_position_relative(-int(angle * ORIENT_TO_DEG))
        RIGHT_MOTOR.set_position_relative(int(angle * ORIENT_TO_DEG))

        wait_for_motor(LEFT_MOTOR)
    except IOError as error:
        print(error)


def turnLeft(angle, speed):
    """Rotate in place (degrees, dps)"""
    try:
        LEFT_MOTOR.set_dps(speed)
        RIGHT_MOTOR.set_dps(speed)

        LEFT_MOTOR.set_limits(POWER_LIMIT, speed)
        RIGHT_MOTOR.set_limits(POWER_LIMIT, speed)

        LEFT_MOTOR.set_position_relative(int(angle * ORIENT_TO_DEG))
        RIGHT_MOTOR.set_position_relative(-int(angle * ORIENT_TO_DEG))

        wait_for_motor(RIGHT_MOTOR)
    except IOError as error:
        print(error)


def find_gyro_diff(old, now):
    diff = now - old
    mod = diff % 360
    if (diff >= 0):
        return mod
    else:
        return -mod

def turn_90_deg():
    actual_turn_angle = 150
    expected_turn_angle = 90

    GYRO.reset_measure()
    angle_before_turn = GYRO.get_abs_measure()
    turnRight(actual_turn_angle, 200)
    #turnLeft(actual_turn_angle, 200)
    time.sleep(1)
    angle_after_turn = GYRO.get_abs_measure()

    expected = expected_turn_angle

    delta_turn = find_gyro_diff(angle_after_turn, angle_before_turn)
    print("delta_turns: ", delta_turn)

    delta_expected_from_unexpected = (expected - delta_turn)
    print("delta_expected_from_unexpected: ", delta_expected_from_unexpected)

    if delta_expected_from_unexpected > 0:
        print("one")
        turnLeft(delta_expected_from_unexpected, 100) # 5 is just a corrective constant
        # turnRight(delta2) # Adjustment to reach 90 deg again
        time.sleep(1)
    elif delta_expected_from_unexpected < 0:
        print("two")
        turnRight(delta_expected_from_unexpected - 5, 100)
        # turnLeft(delta2) # Adjustment to reach 90 deg again
        time.sleep(1)


if __name__ == "__main__":
    #turnRight(30, 200)
    turn_90_deg()