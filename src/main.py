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
bed_detection_threads_killed = False
complete = False


# CONFIRMED TO WORK
def getMeds():
    # 1) Prepare claw to receive blocks
    open_gripper()
    time.sleep(0.5)
    # 2) Align claw to left block
    rotate_with_gyro_correction(10, 300, LEFT)  # in-built time.sleep()
    # 3) Move towards left block
    move_dist_fwd(SQUARE_LENGTH * 0.4, 425)
    time.sleep(1.5)
    # 4) Left block in reach, store it
    store_cube()  # in-built time.sleep()
    # 5) Move back
    move_dist_fwd(-SQUARE_LENGTH * 3 / 8, 425)
    time.sleep(1.5)
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
    rotate_with_gyro_correction(18, 300, LEFT)  #in-built time.sleep()
    # 11) Get robot in alignment with right line going outside of pharmacy
    move_dist_fwd(SQUARE_LENGTH * -2 / 12, 425)
    time.sleep(3)

    rotate_with_gyro_correction(90, 300, LEFT)  # in-built time.sleep()
#     rotate_with_gyro_correction(5, 300, RIGHT)  # in-built time.sleep()


# CONFIRMED TO WORK
def pharmacy_to_left_single():
    # Move out of pharmacy to intersection
    move_dist_fwd(SQUARE_LENGTH * 1.75, 425)
    time.sleep(3)
    rotate_with_gyro_correction(30, 300, LEFT)
    move_dist_fwd(SQUARE_LENGTH * 0.18, 425)
    time.sleep(0.5)
    rotate_with_gyro_correction(35, 300, RIGHT)
    # move_dist_fwd(SQUARE_LENGTH * -0.1, 425)
    time.sleep(1.5)


def left_single_to_right_single():
    rotate_with_gyro_correction(90, 300, RIGHT)
    move_dist_fwd(SQUARE_LENGTH * 2, 425)
    time.sleep(3)
    rotate_with_gyro_correction(90, 300, LEFT)
    move_dist_fwd(SQUARE_LENGTH * 0.4, 425)
    time.sleep(0.5)


def right_single_to_double():
    move_dist_fwd(SQUARE_LENGTH * -1, 425)
    rotate_with_gyro_correction(90, 300, RIGHT)
    move_dist_fwd(SQUARE_LENGTH * 1, 425)
    time.sleep(2)
    rotate_with_gyro_correction(90, 300, RIGHT)


# CONFIRMED TO WORK
def inch_towards_door():
    global door_detected
    total_moved = 0
    print("Looking for the door...")
    while not door_detected:
        print("Beginning an inch search")
        move_dist_fwd(0.01, 425)
        print("Moved 0.01m forward")
        time.sleep(0.5)
        print("Slept 0.5 seconds")
        color_detected = classify_unknown_color(True)
        print("Looking for door")
        total_moved += 0.01
        print(f"Updated how much I inched forward, total is now {total_moved}m")
        print(color_detected)
        if "orange" in color_detected[0]:
            print("DOOR FOUND!!!! WE OUTTA HERE")
            door_detected = True
            time.sleep(0.5)
            # Move forward after having found the door
            move_dist_fwd(0.06, 250)
            break
    return (total_moved + 0.06)


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
        time.sleep(0.5)
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
        if room_depth == 1.5:
            print("Whoa max depth reached, gotta back outta there before you hurt yourself buddy")
            # Robot will be straight, can just go backwards
            move_dist_fwd(-SQUARE_LENGTH * room_depth, 425)
            time.sleep(1.5 * room_depth)
            # Reset room depth in preparation for next process_room() call
            room_depth = 0
            print("moved back outta the room, we OUT now")
            break
        print(GYRO.get_abs_measure())
        # Get the total desired amount to wiggle, and amount rotated until complete/bed found
        total_desired, total_remaining = hassan_wiggle(50)
        print(GYRO.get_abs_measure())
        print(
            f"The wiggle had a total desired amount of {total_desired}, completed {total_desired - total_remaining} and {total_remaining} remaining")
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
                # Put color sensor back over robot
                rotate_with_gyro_correction(36, 300, RIGHT)
                # Increment the number of green beds found
                green_beds_found += 1
                print(f"Logging the bed, now at {green_beds_found} green beds processed")
            # Revert to original alignment, from current mid-wiggle position
            print("Undoing the wiggle effects (partially applied since we got a bed woo)")
            
            arc_bot(-total_desired + total_remaining, 300, RIGHT)
            # Back out of the room
            move_dist_fwd(-SQUARE_LENGTH * room_depth, 425)
            room_depth = 0
            time.sleep(1.5 * room_depth)
            red_detected = False
            green_detected = False
            print("WE BE OUTTA TS HAHA")
            break
        print("Undoing the wiggle effects (fully applied because we didn't find a bed in this scan)")
        arc_bot(-total_desired+total_remaining, 300, RIGHT)
        print("Moving forward to scan the next bit of the room in the next run of this while loop")
        print("Total:",total_desired,"\nTotal Remaining:",total_remaining)
#         arc_bot(-total_desired + total_remaining, 300, RIGHT)
        move_dist_fwd(SQUARE_LENGTH * 0.25, 425)
        time.sleep(0.5)
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

LEFT_WHEEL.set_dps(0)
RIGHT_WHEEL.set_dps(0)
if __name__ == "__main__":
    GYRO.reset_measure()
    LEFT_WHEEL.set_limits(power=POWER_LIMIT, dps=425)
    RIGHT_WHEEL.set_limits(power=POWER_LIMIT, dps=425)
    drive_straight(10,200)
    
    # Step 1: Starting position -> collected med packages [CONFIRMED]
    getMeds()

    # Step 2: pharmacy -> left single room [CONFIRMED]
    pharmacy_to_left_single()

    # Step 3: Align to left single room door [CONFIRMED]
    total_door_adjustment = inch_towards_door()
    door_detected = False
    
    # Hassan Hijacking
    process_room()
    
    move_dist_fwd(-total_door_adjustment,425)

#     # Step 4: Find the bed in the left single room, deposit if green, and get out of room [CONFIRMED]
#     move_dist_fwd(0.05, 300)
#     time.sleep(1.5)
# #     sonia_bed_detection()  # Detects bed, deposits if green, gets out of room
#     if green_beds_found == 1:
#         retrieve_cube()

    # Step 5: Move from left single to right single
    left_single_to_right_single()

    # Step 6: Find bed in right single room, deposit if green, get out of room
    sonia_bed_detection()

    # Check if both green beds found after checking both singles
    if green_beds_found == 2:
        return_from_right_single()
        victory_jingle()

    # Step 7: Move to double room [FIX RETREAT]
    move_dist_fwd(-0.10, 300)
    time.sleep(1)
    right_single_to_double()

    # Step 8: Scan double room section 1
    move_dist_fwd(0.05, 300)
    time.sleep(1.5)
    sonia_bed_detection()  # Detects bed, deposits if green, gets out of room

    # Check if both green beds found after checking section 1 of double room
    if green_beds_found == 2:
        return_from_double(section_number=1)
        victory_jingle()

    # Two beds not found, must continue checking double room. Move to section 2
    rotate_with_gyro_correction(90, 300, LEFT)
    move_dist_fwd(SQUARE_LENGTH * 0.5, 425)
    time.sleep(1)
    rotate_with_gyro_correction(90, 300, RIGHT)

    # Find the door
    total_door_adjustment = inch_towards_door()
    door_detected = False

    # Find bed in second section of the double room, deposit if green, and get out of room
    move_dist_fwd(0.05, 300)
    time.sleep(1.5)
    sonia_bed_detection()  # Detects bed, deposits if green, gets out of room

    # Return to position before having to find the room door
    move_dist_fwd(-total_door_adjustment, 425)
    time.sleep(total_door_adjustment * 2)

    # Check if both green beds found after checking first double section
    if green_beds_found == 2:
        # Return to pharmacy
        return_from_double(section_number=2)
        victory_jingle()

    # Two beds not found, must continue checking double room. Move to section 3
    rotate_with_gyro_correction(90, 300, LEFT)
    move_dist_fwd(SQUARE_LENGTH * 0.5, 425)
    time.sleep(1)
    rotate_with_gyro_correction(90, 300, RIGHT)

    # Find the door
    total_door_adjustment = inch_towards_door()
    door_detected = False

    # Find bed in second section of the double room, deposit if green, and get out of room
    move_dist_fwd(0.05, 300)
    time.sleep(1.5)
    sonia_bed_detection()  # Detects bed, deposits if green, gets out of room

    # Return to position before having to find the room door
    move_dist_fwd(-total_door_adjustment, 425)
    time.sleep(total_door_adjustment * 2)

    # At this point, it's guaranteed both beds are found
    return_from_double(section_number=3)
    victory_jingle()
