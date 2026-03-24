from utils import sound
from utils.brick import TouchSensor, Motor, EV3UltrasonicSensor, wait_ready_sensors
import time
import threading

# ------------------------- CONSTANTS ------------------------

ONE_SQUARE = 710
NINETY_DEGREES = 343

# -------------------- SENSORS AND MOTORS --------------------
rightWheel = Motor("A")
leftWheel = Motor("B")

rightWheel.set_limits(power=50,dps=425)
leftWheel.set_limits(power=50,dps=425)
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
    leftWheel.set_position_relative(amount)
    rightWheel.set_position_relative(-amount)
    print(f"Turned right by { 90 * (amount / NINETY_DEGREES)} degrees.")

def turnLeft(amount):
    rightWheel.set_position_relative(amount)
    leftWheel.set_position_relative(-amount)
    print(f"Turned left by {90 * (amount / NINETY_DEGREES)} degrees.")

def main():
    rightWheel.reset_encoder()
    leftWheel.reset_encoder()
    # Moving from start to blocks (1 -> 2)
    moveForward(ONE_SQUARE * 0.55)
    time.sleep(1)
    # NEED TO PICK UP BLOCKS AND RESET
    # Turning to face outside of pharmacy and move out of it (2 -> 3)
    turnLeft(NINETY_DEGREES)
    time.sleep(1)
    moveForward(ONE_SQUARE * 1.7)
    time.sleep(1)
    # Turning right and moving forward (3 -> 4)
    turnRight(NINETY_DEGREES)
    time.sleep(1)
    moveForward(ONE_SQUARE * 1.9)
    time.sleep(1)
    # Turning right and moving into double room (4 -> 5)
    turnRight(NINETY_DEGREES)
    time.sleep(1)
    moveForward(ONE_SQUARE)
    time.sleep(1)
    # NEED TO WIGGLE AFTER DETECTING DOOR. POTENTIALLY ALTER ROOM MOVEMENT.
    # NOT DOING IT RIGHT NOW, JUST MOVING IN AND OUT
    moveForward(ONE_SQUARE * 2)
    time.sleep(1)
    print("Scanned for beds. No beds found. Scanning new section...")
    moveBackward(ONE_SQUARE * 2)
    turnLeft(NINETY_DEGREES)
    moveForward(ONE_SQUARE * 0.5)
    turnRight(NINETY_DEGREES)
    moveForward(ONE_SQUARE * 2)
    print("Scanned for beds. No beds found. Scanning new section...")
    moveBackward(ONE_SQUARE * 2)
    turnLeft(NINETY_DEGREES)
    moveForward(ONE_SQUARE * 0.5)
    turnRight(NINETY_DEGREES)
    moveForward(ONE_SQUARE * 2)
    print("Scanned for beds. No beds found. Exiting room...")
    moveBackward(ONE_SQUARE * 2)
    moveBackward(ONE_SQUARE * 0.5)
    turnRight(NINETY_DEGREES)
    moveForward(ONE_SQUARE * 2)
    turnRight(NINETY_DEGREES)
    moveForward(ONE_SQUARE * 0.5)
    moveForward(ONE_SQUARE * 2)
    print("Scanned for beds. No beds found. Exiting room...")
    moveBackward(ONE_SQUARE * 2)
    moveBackward(ONE_SQUARE * 0.5)
    turnLeft(NINETY_DEGREES)
    moveForward(ONE_SQUARE * 2)
    turnRight(NINETY_DEGREES)
    moveForward(ONE_SQUARE * 0.5)
    moveForward(ONE_SQUARE * 2)
    print("Scanned for beds. No beds found. Exiting room...")
    moveBackward(ONE_SQUARE * 2)
    moveBackward(ONE_SQUARE * 0.5)
    moveBackward(ONE_SQUARE * 2)



if __name__ == "__main__":
    print("Beginning hardcoded pathing")
    main()

#from utils import sound
#from utils.brick import TouchSensor, Motor, EV3UltrasonicSensor, wait_ready_sensors
#import time
#import threading

# -------------------- SENSORS AND MOTORS --------------------
#rightWheel = Motor("A")
#leftWheel = Motor("B")

#rightWheel.set_limits(power=50)
#leftWheel.set_limits(power=50)

# -------------------- FUNCTIONS --------------------


#def main():
#    rightWheel.reset_encoder()
#    leftWheel.reset_encoder()
#    rightWheel.set_position(-335)
#    leftWheel.set_position(335)
    #rightWheel.set_dps(720)
    #leftWheel.set_dps(720)
    #time.sleep(3)
    #rightWheel.set_dps(0)
    #leftWheel.set_dps(0)

    # rotate


#if __name__ == "__main__":
#    print("test")
#    main()
