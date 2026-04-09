from robot_color_detection import classify_unknown_color
from utils import sound
from utils import brick
from utils.brick import TouchSensor, Motor, EV3UltrasonicSensor, EV3GyroSensor, wait_ready_sensors
import time
import threading
from robot_movement import *
from robot_claw_mechanism import *
from robot_sound_system import *
import sys
import os

# CONSTANTS
TS = TouchSensor(2)
# IMPORTANT VARIABLES

door_detected = False
red_detected = False
green_detected = False
number_beds = 0
room_depth = 0
green_beds_found = 0
bed_detection_threads_killed = False
complete = False

def emergencyStop():
    """Monitors the touch sensor and immediately kills all threads on press."""
    while True:
        if TS.is_pressed():
            print("EMERGENCY STOP TRIGGERED — halting all motors and exiting.")
            # Stop motors before killing the process
            LEFT_WHEEL.set_dps(0)
            RIGHT_WHEEL.set_dps(0)
            claw_arm.set_dps(0)
            claw_gripper.set_dps(0)
            os._exit(1)
        time.sleep(0.05)

# CONFIRMED TO WORK
def getMeds():
    # 1) Prepare claw to receive blocks
    open_gripper()
    # time.sleep(0.5)
    # 2) Align claw to left block
    rotate_with_gyro_correction(10, 300, LEFT)  # in-built time.sleep()
    # 3) Move towards left block
    move_dist_fwd(SQUARE_LENGTH * 0.4, 425)
    time.sleep(0.2)
    # 4) Left block in reach, store it
    store_cube()  # in-built time.sleep()
    # 5) Move back
    move_dist_fwd(-SQUARE_LENGTH * 3 / 8, 425)
    time.sleep(0.5)
    # 6) Align claw to right block
    rotate_with_gyro_correction(25, 300, RIGHT)  # in-built time.sleep()
    # 7) Prepare for receival
    open_gripper()
    time.sleep(1)
    # 8) Move towards right block
    move_dist_fwd(SQUARE_LENGTH * (3 / 8 + 0.05), 425)
    time.sleep(1)
    # 9) Grab instead of store, storage full
    grab_cube()  # in-built time.sleep()
    move_dist_fwd(-SQUARE_LENGTH * 5.5 / 8, 425)
    time.sleep(1)
    # 10) Re-align to initial alignment
    rotate_with_gyro_correction(15, 300, LEFT)  #in-built time.sleep()
    # 11) Get robot in alignment with right line going outside of pharmacy
    move_dist_fwd(SQUARE_LENGTH * -2 / 12, 300)
    time.sleep(1)

    rotate_with_gyro_correction(90, 300, LEFT)  # in-built time.sleep()
#     rotate_with_gyro_correction(5, 300, RIGHT)  # in-built time.sleep()


# CONFIRMED TO WORK
def pharmacy_to_left_single():
    # Move out of pharmacy to intersection
    move_dist_fwd(SQUARE_LENGTH * 2, 425)
    time.sleep(3)
    rotate_with_gyro_correction(30, 300, LEFT)
    move_dist_fwd(SQUARE_LENGTH * 0.15, 425)
    time.sleep(0.5)
    rotate_with_gyro_correction(33, 300, RIGHT)
    # move_dist_fwd(SQUARE_LENGTH * -0.1, 425)
    # time.sleep(1.5)


def left_single_to_right_single():
    rotate_with_gyro_correction(35, 300, LEFT)
    # time.sleep(1.5)
    move_dist_fwd(-SQUARE_LENGTH * 0.5, 425)
    time.sleep(0.5)
    rotate_with_gyro_correction(33, 300, RIGHT)
    rotate_with_gyro_correction(93, 300, RIGHT)
    move_dist_fwd(SQUARE_LENGTH * 2, 425)
    time.sleep(3)
    rotate_with_gyro_correction(94, 300, LEFT)
    # move_dist_fwd(SQUARE_LENGTH * 0.15, 425)
    # time.sleep(0.5)


def right_single_to_double():
    move_dist_fwd(-(SQUARE_LENGTH *0.6), 425)
    rotate_with_gyro_correction(90, 300, RIGHT)
#     maintain_angle(start_angle)
    move_dist_fwd(SQUARE_LENGTH * 0.95, 425)
    time.sleep(2)
    rotate_with_gyro_correction(90, 300, RIGHT)


# CONFIRMED TO WORK
def inch_towards_door():
    global door_detected
    total_moved = 0
    print("Looking for the door...")
    while not door_detected:
        print("Beginning an inch search")
        move_dist_fwd(0.01, 350)
        print("Moved 0.01m forward")
        time.sleep(0.2)
        print("Slept 0.5 seconds")
        color_detected = classify_unknown_color(True)
        print("Looking for door")
        total_moved += 0.01
        print(f"Updated how much I inched forward, total is now {total_moved}m")
        print(color_detected)
        if "orange" in color_detected[0] or "orange" == color_detected:
            print("DOOR FOUND!!!! WE OUTTA HERE")
            door_detected = True
            time.sleep(0.5)
            # Move forward after having found the door
            move_dist_fwd(0.1, 250)
            time.sleep(1.5)
            break
    return (total_moved + 0.1)


def inch_away_from_door():
    global door_detected
    total_moved = 0
    print("Looking for the door...")
    while not door_detected:
        print("Beginning an inch search")
        move_dist_fwd(-0.01, 425)
        print("Moved 0.01m backwards")
        time.sleep(0.5)
        print("Slept 0.5 seconds")
        color_detected = classify_unknown_color(True)
        print("Looking for door")
        total_moved += 0.01
        print(f"Updated how much I inched BACKWARD, total is now {total_moved}m")
        print(color_detected)
        if "orange" in color_detected[0] or "orange" == color_detected:
            print("DOOR FOUND!!!! WE OUTTA HERE")
            door_detected = True
            # Move forward after having found the door
            move_dist_fwd(-0.06, 425)
            break
    return (total_moved + 0.06)


# DEPRECATED
def hassan_wiggle(amount: int):
    total_to_rotate = amount
    remaining_to_rotate = amount
    global red_detected, green_detected
    while not (red_detected or green_detected):
        if remaining_to_rotate == 0:
            print("wiggled full amount, no bed was found... ISSUE UH OH")
            break
        arc_bot(total_to_rotate / 10, 300, RIGHT)
        time.sleep(0.2)
        remaining_to_rotate -= total_to_rotate / 10
        print(f"Rotated {total_to_rotate / 10} degrees for a partial wiggle")
        print(f"Updated the remaining wiggle degree value to {remaining_to_rotate}")
        color_detected = classify_unknown_color(True)
        time.sleep(0.2)
        print("Scanned for a bed")
        print(color_detected)
        if "red" in color_detected[0] or "red" == color_detected:
            print("red bed detected, ew let's get out now")
            red_detected = True
            break
        elif "green" in color_detected[0] or "green" == color_detected:
            print("green bed detected, oh em gee I love it")
            green_detected = True
            break
    return (total_to_rotate, remaining_to_rotate)


# DEPRECATED
def process_room():
    global room_depth, green_beds_found, red_detected, green_detected

    # Continue until a bed is found, or break conditions met
    while not (red_detected or green_detected):
        print("Searching for a bed...")
        # If gone deep enough in the room, quit it to move on
        if room_depth >= 1.2:
            print("Whoa max depth reached, gotta back outta there before you hurt yourself buddy")
            # Robot will be straight, can just go backwards
            move_dist_fwd(-SQUARE_LENGTH * room_depth, 350)
            time.sleep(2)
            # Reset room depth in preparation for next process_room() call
            room_depth = 0
            print("moved back outta the room, we OUT now")
            break
        print(GYRO.get_abs_measure())
        # Get the total desired amount to wiggle, and amount rotated until complete/bed found
        total_desired, total_remaining = hassan_wiggle(50)
        print(GYRO.get_abs_measure())
        print(f"The wiggle had a total desired amount of {total_desired}, completed {total_desired - total_remaining} and {total_remaining} remaining")
        # If a bed was found
        if red_detected or green_detected:
            print("BED WAS DETECTED LETS SEE WHICH KIND")
            # If bed found was green
            if green_detected:
                print("OOOOHHHHH BED IS GREEN!!!! ITS HUNGRY FOR DRUGS")
                # rotate robot to put claw over the bed
                rotate_with_gyro_correction(36, 300, LEFT)
                # Deliver the med package if the bed is green
                print("RELEASE... THE *CUBE*")
                release_cube()
                print("cube released, notifying the blind via sound")
                task_jingle()
                move_dist_fwd(-0.05, 300)
                time.sleep(1)
                # Raise the arm to get it out of the cube's way
                raise_arm()
                time.sleep(1)
                move_dist_fwd(0.05, 300)
                time.sleep(1)
                # Put color sensor back over robot
                # rotate_with_gyro_correction(36, 300, RIGHT)
                # Increment the number of green beds found
                green_beds_found += 1
                print(f"Logging the bed, now at {green_beds_found} green beds processed")
            else:
                rotate_with_gyro_correction(36, 300, LEFT)
            # Revert to original alignment, from current mid-wiggle position
            print("Undoing the wiggle effects (partially applied since we got a bed woo)")
            print(f"Total Desired: {total_desired}\nTotal Remaining: {total_remaining}\nSum: {-total_desired + total_remaining+36}")
            arc_bot(-total_desired + total_remaining + 36 + 5, 300, RIGHT)
            time.sleep(1.5)
            # Back out of the room
            print(f"Backing out of the room: depth was {room_depth}")
            move_dist_fwd(-(SQUARE_LENGTH * room_depth), 350)
            # # Lower the arm again
#             lower_arm()
            time.sleep(2) # MATT CHANGED FROM 3
            room_depth = 0
            red_detected = False
            green_detected = False
            print("WE BE OUTTA TS HAHA")
            break
        print("Undoing the wiggle effects (fully applied because we didn't find a bed in this scan)")
        
        # arc_bot(-total_desired+total_remaining + 5, 300, RIGHT)  # FOR SINGLE ROOMS, MOSTLY WORKED
        arc_bot(-total_desired+total_remaining + 5, 300, RIGHT) # FOR DOUBLE ROOM, TEST
        
        time.sleep(1.5)
        print("Moving forward to scan the next bit of the room in the next run of this while loop")
        print("Total:",total_desired,"\nTotal Remaining:",total_remaining)
        move_dist_fwd(SQUARE_LENGTH * 0.25, 350)
        time.sleep(1)
        room_depth += 0.25
        red_detected = False
        green_detected = False


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
    move_dist_fwd(-SQUARE_LENGTH * 1.75, 425)
    time.sleep(2.5)


def return_from_double(section_number):
#     move_dist_fwd(-SQUARE_LENGTH * 0.5, 425)
    time.sleep(1)
    rotate_with_gyro_correction(90, 300, LEFT)
    if section_number == 3:
        move_dist_fwd(-SQUARE_LENGTH * 1, 425)
    elif section_number == 2:
        move_dist_fwd(-SQUARE_LENGTH * 0.5, 425)

    move_dist_fwd(-SQUARE_LENGTH * 2.5, 425)
    time.sleep(4)
    rotate_with_gyro_correction(90, 300, LEFT)
    move_dist_fwd(-SQUARE_LENGTH * 1.75, 425)
    time.sleep(2)


def sonia_detect_bed_color():
    global red_detected, green_detected, bed_detection_threads_killed
    while (not bed_detection_threads_killed):
        color_detected = classify_unknown_color()
        time.sleep(0.2)
        print("Scanned for a bed")
        if color_detected == "red":
            print("red bed detected, ew let's get out now")
            red_detected = True

        elif color_detected == "green":
            print("green bed detected, oh em gee I love it")
            green_detected = True


def sonia_wiggle():
    global red_detected, green_detected, bed_detection_threads_killed, green_beds_found
    max_wiggles = 7  # To explore a room in its entire depth, wiggle 7 times max (lowkey guessed this, untested still)
    wiggle_counter = 0

    while ((not red_detected) and (not green_detected) and (wiggle_counter < max_wiggles)):
        rotate_with_gyro_correction(50, 100, RIGHT)  # Wiggle right
        rotate_with_gyro_correction(50, 300, LEFT)  # Wiggle left

        move_dist_fwd(0.07, 300)  # Move forward 7 cm before wiggling again
        time.sleep(0.5)

        wiggle_counter += 1

    if green_detected:  # If green is detected, drop block and move back
        release_cube()
        task_jingle()
        green_beds_found += 1
        print("gripper opened")

    inch_away_from_door()
    bed_detection_threads_killed = True
    print("bed detection threads have been killed")


def sonia_bed_detection():
    """This function essentially wiggles AND tries to identify a bed at the same time with threading"""
    print("Bed detection commence")
    global red_detected, green_detected, bed_detection_threads_killed

    t1 = threading.Thread(target=sonia_detect_bed_color, args=())
    t2 = threading.Thread(target=sonia_wiggle, args=())

    t1.start()
    t2.start()

    while (True):
        print("bed detection running")
        if bed_detection_threads_killed:
            t1.join()
            t2.join()
            break

    # Reset your global variable to their default value for next bed search
    bed_detection_threads_killed = False
    red_detected = False
    green_detected = False
    print("We breaking outta the thread")


if __name__ == "__main__":
    flag = False
#     claw_arm.reset_encoder()
#     claw_arm.set_position(-5)
#     claw_arm.reset_encoder()
    es = threading.Thread(target=emergencyStop, daemon=True)
    es.start()
    GYRO.reset_measure()
    LEFT_WHEEL.set_limits(power=POWER_LIMIT, dps=425)
    RIGHT_WHEEL.set_limits(power=POWER_LIMIT, dps=425)
    start_angle = GYRO.get_abs_measure()


    # Step 1: Starting position -> collected med packages
    getMeds()

    # Step 2: pharmacy -> left single room
    pharmacy_to_left_single()

    # Step 3: Align to left single room door
    total_door_adjustment = inch_towards_door()
    door_detected = False
    
    # Step 4: Find the bed in the left single room, deposit if green, and get out of room
    process_room()

    # Undo door alignment
    move_dist_fwd(-total_door_adjustment,425)
    time.sleep(1)

    # Step 5: Retrieve stored cube if the other one was dropped off
    if green_beds_found == 1:
        grab_cube()
        lower_arm()
        
    # Step 6: Move from left single to right single
    left_single_to_right_single()

    # Step 7: Align to right single room door
    # HASSAN HIJACKS AGAIN MWAHAHAHA
    total_door_adjustment = inch_towards_door()
    door_detected = False

    # Step 8: Find bed in right single room, deposit if green, get out of room
    process_room()

    # Step 9: Undo door alignment
    move_dist_fwd(-total_door_adjustment, 425)
    time.sleep(1.5)

    # Step 10: Check if both green beds found after checking both singles, return if true and quit
    if green_beds_found == 1:
        grab_cube()
        lower_arm()
        
    if green_beds_found == 2:
        return_from_right_single()
        lower_arm()
        victory_jingle()
        sys.exit()

    # Step 11: Move from right single to double
    right_single_to_double()
    
    # Step 12: Align to door
    total_door_adjustment = inch_towards_door()
    door_detected = False

    # Step 13: Scan first section of double room
    # SECTION 1
    # (theorised 3 sections, changing this will lead to changes in return_from_double() func and scanning/returning behavior below)
    if green_beds_found == 0:
        flag = True
    process_room()

    # Step 14: Undo door alignment
    move_dist_fwd(-total_door_adjustment-(SQUARE_LENGTH*0.3), 300)
    time.sleep(2)

    # Step 15: Check if both green beds found after checking section 1 of double room, return if true and quit
    if green_beds_found == 1 and Flag:
        grab_cube()
        lower_arm()
        
    if green_beds_found == 2:
        return_from_double(section_number=1)
        victory_jingle()
        sys.exit()

    # Step 16: Two beds not found, must continue checking double room. Move to section 2
    #SECTION 2
    rotate_with_gyro_correction(91, 300, LEFT)
    move_dist_fwd(SQUARE_LENGTH * 0.5, 425)
    time.sleep(1)
    rotate_with_gyro_correction(90, 300, RIGHT)

    # Step 17: Find the door
    total_door_adjustment = inch_towards_door()
    door_detected = False

    # Step 18: Find bed in second section of the double room, deposit if green, and get out of room
    if green_beds_found == 0:
        flag = True
    process_room()

    # Step 19: Return to position before having to find the room door
    move_dist_fwd(-total_door_adjustment-(SQUARE_LENGTH*0.3), 425)
    time.sleep(2)

    # Step 20: Check if both green beds found after checking first double section, return if true and quit
    if green_beds_found == 1 and flag:
        grab_cube()
        lower_arm()
    if green_beds_found == 2:
        # Return to pharmacy
        return_from_double(section_number=2)
        victory_jingle()
        sys.exit()

    # Step 21: Two beds not found, must continue checking double room. Move to section 3
    # SECTION 3
    rotate_with_gyro_correction(91, 300, LEFT)
    move_dist_fwd(SQUARE_LENGTH * 0.5, 425)
    time.sleep(1)
    rotate_with_gyro_correction(90, 300, RIGHT)

    # Step 24: Find the door
    total_door_adjustment = inch_towards_door()
    door_detected = False

    # Step 25: Find bed in second section of the double room, deposit if green, and get out of room
    process_room()

    # Step 26: Return to position before having to find the room door
    move_dist_fwd(-total_door_adjustment, 425)
    time.sleep(total_door_adjustment * 2)

    # Step 27: At this point, it's guaranteed both beds are found (assuming only 3 sections for double room)
    return_from_double(section_number=3)
    victory_jingle()
    sys.exit()
    