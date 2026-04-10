"""
Purpose of this files: Testing if the ports work
How to test with this code?:

"""

from utils.brick import Motor
import time

# ------------------------- CONSTANTS ------------------------

ONE_SQUARE = 710
NINETY_DEGREES_LEFT = 338
NINETY_DEGREES_RIGHT = 330

# -------------------- SENSORS AND MOTORS --------------------
rightWheel = Motor("A")
leftWheel = Motor("B")

rightWheel.set_limits(power=50, dps=425)
leftWheel.set_limits(power=50, dps=425)
rightWheel.reset_encoder()
leftWheel.reset_encoder()


# -------------------- FUNCTIONS --------------------
# file = open('data_collection_3.txt', 'a')

def moveForward(amount):
    rightWheel.set_position_relative(amount)
    leftWheel.set_position_relative(amount)
    print(f"Moved forward {amount / ONE_SQUARE} blocks.")


def moveBackward(amount):
    rightWheel.set_position_relative(-amount)
    leftWheel.set_position_relative(-amount)
    print(f"Moved backward {amount / ONE_SQUARE} blocks.")


def turnRight(amount):
    leftWheel.set_limits(power=30, dps=300)
    rightWheel.set_limits(power=30, dps=300)
    leftWheel.set_position_relative(amount)
    rightWheel.set_position_relative(-amount)
    leftWheel.set_limits(power=50, dps=425)
    rightWheel.set_limits(power=50, dps=425)
    print(f"Turned right by {90 * (amount / NINETY_DEGREES_LEFT)} degrees.")


def turnLeft(amount):
    leftWheel.set_limits(power=30, dps=300)
    rightWheel.set_limits(power=30, dps=300)
    rightWheel.set_position_relative(amount)
    leftWheel.set_position_relative(-amount)
    rightWheel.set_limits(power=50, dps=425)
    leftWheel.set_limits(power=50, dps=425)
    print(f"Turned left by {90 * (amount / NINETY_DEGREES_LEFT)} degrees.")


def arcRight(amount):
    leftWheel.set_limits(power=30, dps=300)
    rightWheel.set_dps(0)
    leftWheel.set_position_relative(amount)
    leftWheel.set_limits(power=50, dps=425)


def arcLeft(amount):
    rightWheel.set_limits(power=30, dps=300)
    leftWheel.set_dps(0)
    rightWheel.set_position_relative(amount)
    rightWheel.set_limits(power=50, dps=425)


def traverseDoubleRoom():
    leftWheel.reset_encoder()
    rightWheel.reset_encoder()
    currentLeftWheelPosition = leftWheel.get_position()
    currentRightWheelPosition = rightWheel.get_position()

    arcRight(NINETY_DEGREES_RIGHT * 0.8)
    time.sleep(1)
    arcLeft(NINETY_DEGREES_LEFT * 0.8)
    time.sleep(1)
    arcLeft(NINETY_DEGREES_LEFT * 0.8)
    time.sleep(1)
    moveForward(ONE_SQUARE * 0.1)
    time.sleep(1)
    arcRight(NINETY_DEGREES_RIGHT * 0.8)
    time.sleep(1)
    arcRight(NINETY_DEGREES_RIGHT * 0.8)
    time.sleep(1)
    moveForward(ONE_SQUARE * 0.1)
    time.sleep(1)
    arcLeft(NINETY_DEGREES_LEFT * 0.8)
    time.sleep(1)
    arcLeft(NINETY_DEGREES_LEFT * 0.8)
    time.sleep(1)
    moveForward(ONE_SQUARE * 0.1)
    time.sleep(1)
    arcRight(NINETY_DEGREES_RIGHT * 0.8)
    time.sleep(1)


def main():
    rightWheel.reset_encoder()
    leftWheel.reset_encoder()
    # Moving from start to blocks (1 -> 2)
    moveForward(ONE_SQUARE * 0.55)
    time.sleep(3)
    # TODO: PICK UP BLOCKS AND RESET
    # Turning to face outside of pharmacy and move out of it (2 -> 3)
    turnLeft(NINETY_DEGREES_LEFT)
    time.sleep(3)
    moveForward(ONE_SQUARE * 1.75)  # exit pharmacy and move forward
    time.sleep(4)
    # Turning right and moving forward (3 -> 4)
    turnRight(NINETY_DEGREES_RIGHT)
    time.sleep(3)
    moveForward(ONE_SQUARE * 1.9)
    time.sleep(4)
    # Turning right and moving into double room (4 -> 5)
    turnRight(NINETY_DEGREES_RIGHT - 3)
    time.sleep(3)
    moveForward(ONE_SQUARE * 0.5)
    time.sleep(3)
    # TODO: WIGGLE AFTER DETECTING DOOR. POTENTIALLY ALTER ROOM MOVEMENT.
    # NOT DOING IT RIGHT NOW, JUST MOVING IN AND OUT
    # scanning room in sections
    # section 1
    moveForward(ONE_SQUARE * 1.2)
    time.sleep(4)
    print("Scanned for beds. No beds found. Scanning new section...")
    # Move to section 2
    moveBackward(ONE_SQUARE * 1.2)
    time.sleep(4)
    turnLeft(NINETY_DEGREES_LEFT)
    time.sleep(3)
    moveForward(ONE_SQUARE * 0.4)
    time.sleep(3)
    turnRight(NINETY_DEGREES_RIGHT)
    time.sleep(3)
    moveForward(ONE_SQUARE * 1.2)
    time.sleep(4)
    print("Scanned for beds. No beds found. Scanning new section...")
    # Move to section 3
    moveBackward(ONE_SQUARE * 1.2)
    time.sleep(4)
    turnLeft(NINETY_DEGREES_LEFT)
    time.sleep(3)
    moveForward(ONE_SQUARE * 0.4)
    time.sleep(3)
    turnRight(NINETY_DEGREES_RIGHT)
    time.sleep(3)
    moveForward(ONE_SQUARE * 1.2)
    time.sleep(4)
    print("Scanned for beds. No beds found. Exiting room...")
    moveBackward(ONE_SQUARE * 1.2)
    time.sleep(4)
    moveBackward(ONE_SQUARE * 0.5)
    time.sleep(3)
    turnRight(NINETY_DEGREES_RIGHT)
    # Moving to single room
    time.sleep(3)
    moveForward(ONE_SQUARE * 1.7)
    time.sleep(4)
    turnRight(NINETY_DEGREES_RIGHT)
    time.sleep(3)
    moveForward(ONE_SQUARE * 0.5)
    time.sleep(3)
    moveForward(ONE_SQUARE * 1.2)
    time.sleep(4)
    print("Scanned for beds. No beds found. Exiting room...")
    moveBackward(ONE_SQUARE * 1.2)
    time.sleep(4)
    moveBackward(ONE_SQUARE * 0.5)
    # Moving to other single room
    time.sleep(3)
    turnLeft(NINETY_DEGREES_LEFT)
    time.sleep(3)
    moveForward(ONE_SQUARE * 2)
    time.sleep(4)
    turnRight(NINETY_DEGREES_RIGHT)
    time.sleep(3)
    moveForward(ONE_SQUARE * 0.5)
    time.sleep(3)
    moveForward(ONE_SQUARE * 1.2)
    time.sleep(4)
    print("Scanned for beds. No beds found. Exiting room...")
    moveBackward(ONE_SQUARE * 1.2)
    time.sleep(4)
    # Returning to pharmacy
    moveBackward(ONE_SQUARE * 0.5)
    time.sleep(3)
    moveBackward(ONE_SQUARE * 1.8)
    time.sleep(4)

if "__init__" == "__main__":
   print("test")
   main()