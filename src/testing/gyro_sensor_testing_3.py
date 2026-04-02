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
from utils.brick import BP, Motor

MOTOR_POLL_DELAY = 0.05

SQUARE_LENGTH = 0.5   # (meters) Side length of square
WHEEL_RADIUS = 0.028  # (meters) Radius of one wheel
AXLE_LENGTH = 0.11    # (meters) Distance between wheel contacts

DIST_TO_DEG = 180 / (math.pi * WHEEL_RADIUS)
ORIENT_TO_DEG = AXLE_LENGTH / WHEEL_RADIUS

FWD_SPEED = 100   # (deg/sec)
TRN_SPEED = 180   # (deg/sec)

LEFT_MOTOR = Motor("A")
RIGHT_MOTOR = Motor("D")

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


def do_square(side_length):
    for _ in range(4):
        move_dist_fwd(side_length, FWD_SPEED)
        rotate_bot(90, TRN_SPEED)

    LEFT_MOTOR.set_power(0)
    RIGHT_MOTOR.set_power(0)


try:
    print("Square Driving Demo")

    init_motor(LEFT_MOTOR)
    init_motor(RIGHT_MOTOR)

    while True:
        side_length = SQUARE_LENGTH

        resp = input(
            f"Override default side length ({side_length:.2f}m)? y/n (q for quit): "
        )

        if resp.lower() == "y":
            side_length = float(input("Enter square side length (m): "))

        if resp.lower() == "q":
            BP.reset_all()
            exit()

        print(f"Starting square driver with side length = {side_length:.2f}m")

        do_square(side_length)

except KeyboardInterrupt:
    BP.reset_all()
    print("\nProgram stopped")