from utils.brick import TouchSensor, EV3ColorSensor, Motor, wait_ready_sensors
from color import *
import datetime
import time
import threading

# CONSTANTS

COLOR_SENSOR = EV3ColorSensor(3)

BLUE = Color('blue', 0.30514540441303245, 0.42559382484300484, 0.851873554962868,
             0.005608173772585627,0.0052204372086351, 0.0029866701058684276)
GREEN = Color('green', 0.5288572659051487, 0.8153196582255317, 0.23555251920848586,
              0.005051739881859017,0.0036444174525583476, 0.006328984947554189)
ORANGE = Color('orange', 0.9193282736567624, 0.3582026489175016, 0.1625743547752035,
               0.002830838124651885,0.005676075368760179, 0.007465604939214666)
RED = Color('red', 0.9682768290485266, 0.1479864922467923, 0.20072730902491995,
            0.0032287074234957965,0.011164373185914777, 0.010651763777604661)
WHITE = Color('white', 0.47856765654917144, 0.4751915744144273, 0.7383455020642785,
              0.0020329695461371975,0.0022002083544665546, 0.001706285451531559)
YELLOW = Color('yellow', 0.7793133994249224, 0.5986100822841631, 0.18516968094855718,
               0.002988667062624679,0.0035148365461744385, 0.005243845456394571)
THICK_INTERSECTION = Color('thick intersection', 0.35875595176919356, 0.5148258450215546, 0.7764796797011159,
                           0.040709680400056375, 0.030394450281119235, 0.027326227202242318)
THICK_LINE = Color('thick line', 0.4222264010998929, 0.6081623186340988, 0.6704320827701554,
                   0.032236153045677625,0.02623960306083702, 0.025624138391881688)
thin_intersection = Color('thin intersection', 0.5084433516212437, 0.5503023933503505, 0.6590710630695044,
                          0.04161211492811081, 0.03563952336368879, 0.03572427963003056)
THIN_LINE = Color('thin line', 0.5885948428200825, 0.4231970291051555, 0.6883294479534854,
                  0.014673265027663585,0.01581006368544569, 0.014060363505711054)

ALL_COLORS = [BLUE, GREEN, ORANGE, RED, WHITE, YELLOW, THICK_INTERSECTION, THICK_LINE, thin_intersection, THIN_LINE]

EPSILON = 0.0000000001


wait_ready_sensors(True)


def classify_unknown_color(closest_three_allowed=False):
    # Collect raw rgb
    raw_rgb = COLOR_SENSOR.get_rgb()
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
    for i in range(len(ALL_COLORS)):
        color = ALL_COLORS[i]
        distance = color.find_distance(norm_r, norm_g, norm_b)
        best_colors[distance] = i

    distances = sorted(list(best_colors.keys()))
    for i in range(3):
        color_to_check = ALL_COLORS[best_colors[distances[i]]]
        if color_to_check.is_match(norm_r, norm_g, norm_b) and i == 0:
            return color_to_check.get_name()
    if closest_three_allowed:
        return (ALL_COLORS[best_colors[distances[0]]].get_name(), ALL_COLORS[best_colors[distances[1]]].get_name(), ALL_COLORS[best_colors[distances[2]]].get_name())
    return "unknown"