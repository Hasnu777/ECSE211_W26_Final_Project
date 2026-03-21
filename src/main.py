from utils import sound
from utils.brick import TouchSensor, Motor, EV3UltrasonicSensor, wait_ready_sensors, EV3ColorSensor
import time
import threading
from color import *

# -------- Sensor Setup -------- 
color_sensor = EV3ColorSensor(1)
touch_sensor = TouchSensor(2)
wait_ready_sensors(True)

# -------- Motor Setup -------- 
motor_1 = Motor("A")
motor_2 = Motor("B")
motor_1.set_dps(0)
motor_2.set_dps(0)
motor_1.reset_encoder()
motor_2.reset_encoder()

# Defining Color Objects (all mean and sd values are obtained via measurement)
red = Color("red", 0.019313118, 0.00257185, 0.004151466, 0.000734278, 0.000353749, 0.000330727)
green = Color("green", 0.540724541, 0.800827897, 0.256963438, 0.009701897, 0.007359186, 0.010637534)
blue = Color("blue", 0.00189331, 0.002569377, 0.005527913, 0.000259899, 0.000311934, 0.000780373)
orange = Color("orange", 0.012555844, 0.004891167, 0.002517735, 0.000375845, 0.000209882, 0.000220295)
white = Color("white", 0.002300318, 0.002193182, 0.003858842, 0.000085778549, 0.000077360638, 0.000147553553)
yellow = Color("yellow", 0.012555844, 0.004891167, 0.002517735, 0.000375845, 0.000209882, 0.000220295)

# array with all the colors
all_colors = [red, green, blue, orange, white, yellow]
 
# Purpose of following method: Color sensor reads and identifies to what color a new color reading belongs to
def classify_unknown_color():
    # Collect raw rgb
    raw_rgb = color_sensor.get_rgb()
    raw_r = raw_rgb[0]
    raw_g = raw_rgb[1]
    raw_b = raw_rgb[2]

    # Normalizing the RGB values
    denominator = (raw_r**2 + raw_g**2 + raw_b**2)**0.5
    norm_r = raw_r/denominator
    norm_b = raw_b/denominator
    norm_g = raw_g/denominator

    # Loop through each color and find distance between unknown color and all measured known colors
    best_distance = 100000000          # arbitrarily set a big number
    best_color = "unknown"

    print_counter = 0
    norm_counter = 0
    # Iterate through colors to find the closest match
    for color in all_colors:
        distance = color.find_distance(norm_r, norm_g, norm_b)
        print(print_counter, color.name, distance)
        print_counter += 1

        if (distance < best_distance):
            best_distance = distance
            best_color = color.name

    # check if closest matching known color is < 2 SD's to the detected color
    print(norm_counter, norm_r, norm_g, norm_b)
    norm_counter += 1
    if (color.is_match(norm_r, norm_g, norm_b)):
        print(norm_r, norm_g, norm_b + "matched")
        return best_color

    return "unknown"
    

if __name__ == "__main__":
    while True:
        time.sleep(2)
        print(classify_unknown_color())
        if touch_sensor.is_pressed():
            break



# -------------------------- Coding Graveyard --------------------------
    # def classify_new_color():

#     # Getting raw RGB data: 
#     RGB = C_SENSOR.get_rgb()
#     r = RGB[0]
#     g = RGB[1]
#     b = RGB[2]

#     # Normalize the RGB values:
#     denom = (r**2 + g**2 + b**2)**0.5
#     norm_r = r/denom
#     norm_b = b/denom
#     norm_g = g/denom
#     # norm_rgb = [norm_r,norm_g,norm_b]  # normalized rgb values in a list


#     #print(ls)
#     #finding shortest euclidean distance 
#     # min_d = 1000000
    
#     #repeat for each cluster  
#     for i in range (0, len(cluster_center)):
# #        d = ((r-cluster_center[i][0])**2 + (g - cluster_center[i][1])**2 + (b - cluster_center[i][2])**2)**0.5
# #        if d < min_d:
# #            min_d = d
# #            current_colour = colour_adj[i]
# #         print (abs(r-cluster_center[i][0]))
# #         print(cluster_SD[i][0])
# #         print (abs(g-cluster_center[i][1]))
# #         print(cluster_SD[i][1])
# #         print (abs(b-cluster_center[i][2]))
# #         print(cluster_SD[i][2])
#         if (abs(r-cluster_center[i][0]) > 2*cluster_SD[i][0] or abs(g-cluster_center[i][1]) > 2*cluster_SD[i][1] or abs(b-cluster_center[i][2]) > 2*cluster_SD[i][2]): #reading is too far from sample
#             current_color = 'unknown colour, recorded data too far from samples'
#         else:
#             current_color = "intersect"
#     #output
#     return current_color

        # m1.set_dps(80)
        # m2.set_dps(80)
        # inter = colour_class()
        # if (inter == "intersect"):
        #     print("intersect found. Rotating now")
        #     m1.set_dps(0)
        #     m2.set_dps(0)
        #     time.sleep(1)
        #     m1.reset_encoder()
        #     m2.reset_encoder()
        #     m1.set_position(-345)
        #     m2.set_position(345)
        
