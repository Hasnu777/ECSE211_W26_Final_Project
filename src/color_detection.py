from utils import sound
from utils.brick import TouchSensor, Motor, EV3UltrasonicSensor, wait_ready_sensors, EV3ColorSensor
import time
import threading
from color import *

# -------- Sensor Setup --------
color_sensor = EV3ColorSensor(4)
touch_sensor = TouchSensor(2)
wait_ready_sensors(True)

# -------- Motor Setup --------
motor_1 = Motor("A")
motor_2 = Motor("B")
motor_1.set_dps(0)
motor_2.set_dps(0)
motor_1.reset_encoder()
motor_2.reset_encoder()

# Known color data using unit vector normalisation method
blue = Color('blue', 0.30514540441303245, 0.42559382484300484, 0.851873554962868, 0.005608173772585627,
             0.0052204372086351, 0.0029866701058684276)
green_bed = Color('green bed', 0.5288572659051487, 0.8153196582255317, 0.23555251920848586, 0.005051739881859017,
                  0.0036444174525583476, 0.006328984947554189)
orange = Color('orange', 0.9193282736567624, 0.3582026489175016, 0.1625743547752035, 0.002830838124651885,
               0.005676075368760179, 0.007465604939214666)
red_bed = Color('red bed', 0.9682768290485266, 0.1479864922467923, 0.20072730902491995, 0.0032287074234957965,
                0.011164373185914777, 0.010651763777604661)
thick_intersection = Color('thick intersection', 0.35875595176919356, 0.5148258450215546, 0.7764796797011159,
                           0.040709680400056375, 0.030394450281119235, 0.027326227202242318)
thick_line = Color('thick line', 0.4222264010998929, 0.6081623186340988, 0.6704320827701554, 0.032236153045677625,
                   0.02623960306083702, 0.025624138391881688)
thin_intersection = Color('thin intersection', 0.5084433516212437, 0.5503023933503505, 0.6590710630695044,
                          0.04161211492811081, 0.03563952336368879, 0.03572427963003056)
thin_line = Color('thin line', 0.5885948428200825, 0.4231970291051555, 0.6883294479534854, 0.014673265027663585,
                  0.01581006368544569, 0.014060363505711054)
white = Color('white', 0.47856765654917144, 0.4751915744144273, 0.7383455020642785, 0.0020329695461371975,
              0.0022002083544665546, 0.001706285451531559)
yellow = Color('yellow', 0.7793133994249224, 0.5986100822841631, 0.18516968094855718, 0.002988667062624679,
               0.0035148365461744385, 0.005243845456394571)

# array with all the known color objects
all_colors = [blue, green_bed, orange, red_bed, thick_intersection, thick_line, thin_intersection, thin_line, white,
              yellow]


# Purpose of following method: Color sensor reads and identifies to what color a new color reading belongs to
def classify_unknown_color():
    # Collect raw rgb
    raw_rgb = color_sensor.get_rgb()
    raw_r = raw_rgb[0]
    raw_g = raw_rgb[1]
    raw_b = raw_rgb[2]
    print("Detected color info:", raw_r, raw_g, raw_b)

    # Normalizing the RGB values with unit vector normalisation method
    denominator = (raw_r ** 2 + raw_g ** 2 + raw_b ** 2) ** 0.5
    norm_r = raw_r / denominator
    norm_b = raw_b / denominator
    norm_g = raw_g / denominator

    print("Detected color norm info:", norm_r, norm_g, norm_b)

    # Loop through each color and find distance between unknown color and all measured known colors
    best_distance = 100000000  # arbitrarily set a big number
    best_colors = []

    print_counter = 0
    norm_counter = 0
    # Iterate through colors to find the closest match
    for color in all_colors:
        print("Trying to match detected color to:", color.get_name())
        distance = color.find_distance(norm_r, norm_g, norm_b)
        print(print_counter, color.name, distance)
        print_counter += 1
        best_colors.append((distance, color))

    distances = [distance for distance, color in best_colors]
    best_colors = sorted(best_colors, key=lambda x: x[0])
    for i in range(3):
        distance, color_to_check = best_colors[i]
        if color_to_check.is_match(norm_r, norm_g, norm_b) and i == 0:
            print(f"{color_to_check.get_name()} matched to detected color. Closest three are: {best_colors[0][1].get_name()}, {best_colors[1][1].get_name()}, {best_colors[2][1].get_name()}")
            return color_to_check.get_name()
    print(f"unknown, after checking closest 3 colors: {best_colors[0][1].get_name()}, {best_colors[1][1].get_name()}, {best_colors[2][1].get_name()}")
    return "unknown"


if __name__ == "__main__":
    exe_counter = 1
    while True:
        time.sleep(4)
        print("Attempt number", exe_counter)
        exe_counter += 1
        print(classify_unknown_color())
        if touch_sensor.is_pressed():
            break