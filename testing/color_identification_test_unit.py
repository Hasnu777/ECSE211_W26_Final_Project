"""
Purpose of this files: Testing if the ports work
How to test with this code?:

"""
from utils.brick import TouchSensor, Motor, wait_ready_sensors, EV3ColorSensor
import time
from color import *

# -------- Sensor Setup --------
color_sensor = EV3ColorSensor(3)
touch_sensor = TouchSensor(2)
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

# Array with all the colors
all_colors = [blue, green, orange, red, white, yellow]


# Purpose of following method: Color sensor reads and identifies to what color a new color reading belongs to
def classify_unknown_color():
    # Collect raw rgb
    raw_rgb = color_sensor.get_rgb()
    raw_r = raw_rgb[0]
    raw_g = raw_rgb[1]
    raw_b = raw_rgb[2]

    # Normalizing the RGB values
    denominator = (raw_r ** 2 + raw_g ** 2 + raw_b ** 2) ** 0.5  # UNIT VECTOR METHOD

    norm_r = raw_r / denominator
    norm_b = raw_b / denominator
    norm_g = raw_g / denominator

    # Loop through each color and find distance between unknown color and all measured known colors
    best_distance = 100000000  # arbitrarily set a big number
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


if __name__ == "__main__":
    while True:
        time.sleep(1)
        print("Color: ", classify_unknown_color())
        if touch_sensor.is_pressed():
            break

# ----------------------- CODE GRAVEYARD -----------------------

# Defining Color Objects (all mean and sd values are obtained via measurement) UNIT VECTOR NORMALISATION
# red = Color("red", 0.019313118, 0.00257185, 0.004151466, 0.000734278, 0.000353749, 0.000330727)
# green = Color("green", 0.540724541, 0.800827897, 0.256963438, 0.009701897, 0.007359186, 0.010637534)
# blue = Color("blue", 0.00189331, 0.002569377, 0.005527913, 0.000259899, 0.000311934, 0.000780373)
# orange = Color("orange", 0.012555844, 0.004891167, 0.002517735, 0.000375845, 0.000209882, 0.000220295)
# white = Color("white", 0.002300318, 0.002193182, 0.003858842, 0.000085778549, 0.000077360638, 0.000147553553)
# yellow = Color("yellow", 0.012555844, 0.004891167, 0.002517735, 0.000375845, 0.000209882, 0.000220295)

# RATIO METHOD
# red = Color("red", 0.741824288,0.098789986,0.159385726, 0.019852985,0.013327676,0.011013703)
# green = Color("green", 0.338262801,0.501012684,0.160724514, 0.005607666,0.006761501,0.00595247)
# blue = Color("blue", 0.189484037,0.257711208,0.552804755, 0.003798342,0.004916666,0.006644135)
# orange = Color("orange", 0.628879119,0.244945924,0.126174957, 0.010417871,0.00748031,0.011306495)
# white = Color("white", 0.275411125,0.26260196,0.461986915, 0.002241287,0.002003323,0.002767336)
# yellow = Color("yellow", 0.501769776,0.368411827,0.129818397, 0.004752631,0.003487286,0.004773292)

# BELOW IS HASSANS VERSION OF COLORS FOR RAW VALUES
# blue = Color('blue', 80.4622641509434, 112.21278825995807, 224.60796645702305, 1.9135239505320853, 1.5913168416741919, 1.968669552261819)
# green_bed = Color('green bed', 84.56631578947369, 130.36631578947367, 37.66842105263158, 1.3808167320993143, 1.2824820118829443, 1.2141935298698636)
# orange = Color('orange', 142.99899899899899, 55.72172172172172, 25.293293293293292, 1.3699911951811488, 1.228881111998254, 1.2902440834430997)
# red_bed = Color('red bed', 98.86666666666666, 15.12, 20.501538461538463, 1.337685205645076, 1.278203868013678, 1.2235918928775156)
# thick_intersection = Color('thick intersection', 9.175, 13.131, 19.778, 1.39941952251639, 1.2376748361342733, 1.237221079678163)
# thick_line = Color('thick line', 11.844, 17.027, 18.762, 1.3578158932638844, 1.2562925614680682, 1.2146423341873112)
# thin_intersection = Color('thin intersection', 10.212, 11.035, 13.188, 1.3874638734035565, 1.2457026129859405, 1.1334266628238459)
# thin_line = Color('thin line', 30.104104104104103, 21.64864864864865, 35.193193193193196, 1.3516657032515547, 1.2170278684188722, 1.1937917961547064)
# white = Color('white', 203.32290615539858, 201.88900100908174, 313.6902119071645, 1.3237983261613457, 1.4304565581244055, 1.4776829762517514)
# yellow = Color('yellow', 154.011, 118.301, 36.598, 1.3648732541888275, 1.2978439813783471, 1.2059834161380496)
