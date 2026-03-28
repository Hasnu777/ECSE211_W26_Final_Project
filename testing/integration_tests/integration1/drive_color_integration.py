import time
from color import *
from utils.brick import TouchSensor, Motor, wait_ready_sensors, EV3ColorSensor

# ------------------------- CONSTANTS ------------------------
ONE_SQUARE = 710
NINETY_DEGREES_LEFT = 343
NINETY_DEGREES_RIGHT = 343
EPSILON = 0.0000000001

# -------------------- SENSORS AND MOTORS --------------------
rightWheel = Motor("A")
leftWheel = Motor("D")
color_sensor = EV3ColorSensor(3)
touch_sensor = TouchSensor(2)

rightWheel.set_limits(power=50, dps=425)
leftWheel.set_limits(power=50, dps=425)
rightWheel.reset_encoder()
leftWheel.reset_encoder()
wait_ready_sensors(True)

# -------- Motor Setup --------
motor_1 = Motor("A")
motor_2 = Motor("D")
motor_1.set_dps(0)
motor_2.set_dps(0)
motor_1.reset_encoder()
motor_2.reset_encoder()

# -------- For other ways of defining each color, see the code graveyard below --------
blue = Color('blue', 0.30514540441303245, 0.42559382484300484, 0.851873554962868, 0.005608173772585627,
             0.0052204372086351, 0.0029866701058684276)
green = Color('green', 0.5288572659051487, 0.8153196582255317, 0.23555251920848586, 0.005051739881859017,
              0.0036444174525583476, 0.006328984947554189)
orange = Color('orange', 0.9193282736567624, 0.3582026489175016, 0.1625743547752035, 0.002830838124651885,
               0.005676075368760179, 0.007465604939214666)
red = Color('red', 0.9682768290485266, 0.1479864922467923, 0.20072730902491995, 0.0032287074234957965,
            0.011164373185914777, 0.010651763777604661)
white = Color('white', 0.47856765654917144, 0.4751915744144273, 0.7383455020642785, 0.0020329695461371975,
              0.0022002083544665546, 0.001706285451531559)
yellow = Color('yellow', 0.7793133994249224, 0.5986100822841631, 0.18516968094855718, 0.002988667062624679,
               0.0035148365461744385, 0.005243845456394571)
thick_intersection = Color('thick intersection', 0.35875595176919356, 0.5148258450215546, 0.7764796797011159,
                           0.040709680400056375, 0.030394450281119235, 0.027326227202242318)
thick_line = Color('thick line', 0.4222264010998929, 0.6081623186340988, 0.6704320827701554, 0.032236153045677625,
                   0.02623960306083702, 0.025624138391881688)
thin_intersection = Color('thin intersection', 0.5084433516212437, 0.5503023933503505, 0.6590710630695044,
                          0.04161211492811081, 0.03563952336368879, 0.03572427963003056)
thin_line = Color('thin line', 0.5885948428200825, 0.4231970291051555, 0.6883294479534854, 0.014673265027663585,
                  0.01581006368544569, 0.014060363505711054)

# Array with all the colors
all_colors = [blue, green, orange, red, white, yellow, thick_intersection, thick_line, thin_intersection, thin_line]


# Purpose of following method: Color sensor reads and identifies to what color a new color reading belongs to
def classify_unknown_color():
    # Collect raw rgb
    raw_rgb = color_sensor.get_rgb()
    raw_r = raw_rgb[0]
    raw_g = raw_rgb[1]
    raw_b = raw_rgb[2]

    # Normalizing the RGB values
    denominator = (raw_r ** 2 + raw_g ** 2 + raw_b ** 2) ** 0.5  # UNIT VECTOR METHOD

    # To avoid getting a float division by 0 error
    if (denominator < EPSILON):
        return "unknown"

    norm_r = raw_r / denominator
    norm_b = raw_b / denominator
    norm_g = raw_g / denominator

    # Loop through each color and find distance between unknown color and all measured known colors
    best_colors = {}

    # Iterate through colors to find the closest match
    for i in range(len(all_colors)):
        color = all_colors[i]
        distance = color.find_distance(norm_r, norm_g, norm_b)
        best_colors[distance] = i

    distances = sorted(list(best_colors.keys()))
    for i in range(3):
        color_to_check = all_colors[best_colors[distances[i]]]
        if color_to_check.is_match(norm_r, norm_g, norm_b) and i == 0:
            return color_to_check.get_name()
    return "unknown"




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


if __name__ == "__main__":
    while True:
        print("Color: ", classify_unknown_color())
        moveForward(10)
        time.sleep(1)
        if touch_sensor.is_pressed():
            break