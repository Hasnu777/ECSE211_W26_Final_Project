from robot_color_detection import classify_unknown_color
from utils import sound
from utils import brick
from utils.brick import TouchSensor, Motor, EV3UltrasonicSensor, EV3GyroSensor, wait_ready_sensors
import time
import threading
from robot_movement import *
from robot_claw_mechanism import *
from robot_sound_system import *

# CONSTANTS

# IMPORTANT VARIABLES

door_detected = False
red_detected = False
green_detected = False
number_beds = 0
room_depth = 0
green_beds_found = 0
complete = False

# CONFIRMED TO WORK
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
    rotate_with_gyro_correction(4,300, RIGHT) # in-built time.sleep()

# CONFIRMED TO WORK
def pharmacy_to_left_single():
    # Move out of pharmacy to intersection
    move_dist_fwd(SQUARE_LENGTH * 2, 425)
    time.sleep(3)
    rotate_with_gyro_correction(30, 300, LEFT)
    move_dist_fwd(SQUARE_LENGTH * 0.1, 425)
    time.sleep(0.5)
    rotate_with_gyro_correction(30,300,RIGHT)
    move_dist_fwd(SQUARE_LENGTH * 0.1, 425)
    time.sleep(1.5)


def left_single_to_right_single():
    rotate_with_gyro_correction(90, 300, RIGHT)
    move_dist_fwd(SQUARE_LENGTH * 2, 425)
    time.sleep(3)
    rotate_with_gyro_correction(90, 300, LEFT)
    move_dist_fwd(SQUARE_LENGTH * 0.3, 425)
    time.sleep(0.5)


def right_single_to_double():
    rotate_with_gyro_correction(90, 300, RIGHT)
    move_dist_fwd(SQUARE_LENGTH * 1, 425)
    time.sleep(2)
    rotate_with_gyro_correction(90, 300, RIGHT)


def inch_towards_door():
    global door_detected
    total_moved = 0
    while not door_detected:
        move_dist_fwd(0.02, 425)
        time.sleep(1)
        color_detected = classify_unknown_color()
        total_moved += 0.1
        if color_detected == "orange":
            door_detected = True
    return total_moved


def hassan_wiggle(amount : int):
    total_to_rotate = amount
    remaining_to_rotate = amount
    global red_detected, green_detected
    while not (red_detected or green_detected):
        if remaining_to_rotate == 0:
            break
        arc_bot(total_to_rotate/10, 300, RIGHT)
        color_detected = classify_unknown_color()
        if color_detected == "red":
            red_detected = True
            break
        elif color_detected == "green":
            green_detected = True
            break
    return (total_to_rotate, remaining_to_rotate)


def process_room():
    global room_depth, green_beds_found, red_detected, green_detected

    # Continue until a bed is found, or break conditions met
    while not (red_detected or green_detected):
        # If gone deep enough in the room, quit it to move on
        if room_depth == 1.5:
            # Robot will be straight, can just go backwards
            move_dist_fwd(-SQUARE_LENGTH * room_depth, 425)
            time.sleep(1.5*room_depth)
            # Reset room depth in preparation for next process_room() call
            room_depth = 0
            break

        # Get the total desired amount to wiggle, and amount rotated until complete/bed found
        total_desired, total_remaining = hassan_wiggle(50)
        # If a bed was found
        if red_detected or green_detected:
            # If bed found was green
            if green_detected:
                # Deliver the med package if the bed is green
                release_cube()
                task_jingle()
                # Increment the number of green beds found
                green_beds_found += 1
            # Revert to original alignment, from current mid-wiggle position
            rotate_with_gyro_correction(total_desired - total_remaining, 300, LEFT)
            break

        rotate_with_gyro_correction(total_desired, 300, LEFT)
        move_dist_fwd(SQUARE_LENGTH * 0.25, 425)
        time.sleep(0.5)
        room_depth += 0.25


def all_beds_found():
    global green_beds_found, complete
    if green_beds_found == 2:
        complete = True


def return_from_right_single():
    close_gripper()
    time.sleep(0.5)
    raise_arm()
    time.sleep(0.5)
    move_dist_fwd(-SQUARE_LENGTH * 0.3, 425)
    time.sleep(0.6)
    rotate_with_gyro_correction(90, 300, RIGHT)
    move_dist_fwd(-SQUARE_LENGTH * 1, 425)
    time.sleep(2)
    rotate_with_gyro_correction(90, 300, LEFT)
    move_dist_fwd(-SQUARE_LENGTH * 1.3, 425)
    time.sleep(2.5)


def return_from_double(section_number):
    rotate_with_gyro_correction(90, 300, LEFT)
    if section_number == 3:
        move_dist_fwd(-SQUARE_LENGTH * 1, 425)
    elif section_number == 2:
        move_dist_fwd(-SQUARE_LENGTH * 0.5, 425)

    move_dist_fwd(-SQUARE_LENGTH * 2, 425)
    time.sleep(2)
    rotate_with_gyro_correction(90, 300, LEFT)
    move_dist_fwd(-SQUARE_LENGTH * 2, 425)
    time.sleep(2)



if __name__ == "__main__":
    LEFT_WHEEL.set_limits(power=POWER_LIMIT, dps=425)
    RIGHT_WHEEL.set_limits(power=POWER_LIMIT, dps=425)

    # Step 1: Starting position -> collected med packages
    getMeds()

    # Step 2: pharmacy -> left single room
    pharmacy_to_left_single()

    # Find the door
    total_door_adjustment = inch_towards_door()
    door_detected = False

    # Find the bed in the left single room, deposit if green, and get out of room
    process_room()

    # Return to position before having to find the room door
    move_dist_fwd(-total_door_adjustment, 425)

    # Move from left single to right single
    left_single_to_right_single()

    # Find the door
    total_door_adjustment = inch_towards_door()
    door_detected = False

    # Find the bed in the right single room, deposit if green, and get out of room
    process_room()

    # Return to position before having to find the room door
    move_dist_fwd(-total_door_adjustment, 425)

    # Check if both green beds found after checking both singles
    if green_beds_found == 2:
        return_from_right_single()
        victory_jingle()

    # Must find both green beds, continue on to the double room...
    right_single_to_double()

    # Find the door
    total_door_adjustment = inch_towards_door()
    door_detected = False

    # Find bed in first section of the double room, deposit if green, and get out of room
    process_room()

    # Return to position before having to find the room door
    move_dist_fwd(-total_door_adjustment, 425)

    # Check if both green beds found after checking first double section
    if green_beds_found == 2:
        # Return to pharmacy
        return_from_double(section_number=1)
        victory_jingle()

    # Two beds not found, must continue checking double room. Move to section 2
    rotate_with_gyro_correction(90, 300, LEFT)
    move_dist_fwd(SQUARE_LENGTH * 0.5, 425)
    rotate_with_gyro_correction(90, 300, RIGHT)

    # Find the door
    total_door_adjustment = inch_towards_door()
    door_detected = False

    # Find bed in second section of the double room, deposit if green, and get out of room
    process_room()

    # Return to position before having to find the room door
    move_dist_fwd(-total_door_adjustment, 425)

    # Check if both green beds found after checking first double section
    if green_beds_found == 2:

        # Return to pharmacy
        return_from_double(section_number=2)
        victory_jingle()

    # Two beds not found, must continue checking double room. Move to section 3
    rotate_with_gyro_correction(90, 300, LEFT)
    move_dist_fwd(SQUARE_LENGTH * 0.5, 425)
    rotate_with_gyro_correction(90, 300, RIGHT)

    # Find the door
    total_door_adjustment = inch_towards_door()
    door_detected = False

    # Find bed in second section of the double room, deposit if green, and get out of room
    process_room()

    # Return to position before having to find the room door
    move_dist_fwd(-total_door_adjustment, 425)

    # At this point, it's guaranteed both beds are found
    return_from_double(section_number=3)
    victory_jingle()
