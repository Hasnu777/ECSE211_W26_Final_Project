from utils import sound
from utils.brick import TouchSensor, Motor, EV3UltrasonicSensor, wait_ready_sensors, EV3ColorSensor
import time
import threading
from color import *

# -------- Sensor Setup -------- 
color_sensor = EV3ColorSensor(1)
wait_ready_sensors(True)

# -------- Motor Setup -------- 
m1 = Motor("A")
m2 = Motor("B")
m1.set_dps(0)
m2.set_dps(0)
m1.reset_encoder()
m2.reset_encoder()


# Defining Color Objects (all mean and sd values are obtained via measurement)
red = Color("red", 0.019313118, 0.00257185, 0.004151466, 0.000734278, 0.000353749, 0.000330727)
green = Color("green", 0.540724541, 0.800827897, 0.256963438, 0.009701897, 0.007359186, 0.010637534)
blue = Color("blue", 0.00189331, 0.002569377, 0.005527913, 0.000259899, 0.000311934, 0.000780373)
orange = Color("orange", 0.012555844, 0.004891167, 0.002517735, 0.000375845, 0.000209882, 0.000220295)
white = Color("white", 0.002300318, 0.002193182, 0.003858842, 0.000085778549, 0.000077360638, 0.000147553553)
yellow = Color("yellow", 0.012555844, 0.004891167, 0.002517735, 0.000375845, 0.000209882, 0.000220295)

# array with all the colors
all_colors = [red, green, blue, orange, white, yellow]

# Purpose of following method:
# Color sensor read and identifies to what color a new color reading belongs to
def classify_new_color():
    # Collect raw rgb
    raw_rgb = color_sensor.get_rgb()
    raw_r = new_rgb[0]
    raw_g = new_rgb[1]
    raw_b = new_rgb[2]

    # Normalizing the RGB values
    denominator = (raw_r**2 + raw_g**2 + raw_b**2)**0.5
    norm_r = raw_r/denominator
    norm_b = raw_b/denominator
    norm_g = raw_g/denominator



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


# -------- Main -------- 
if __name__ == "_main__":
    while True:
        m1.set_dps(80)
        m2.set_dps(80)
        inter = colour_class()
        if (inter == "intersect"):
            print("intersect found. Rotating now")
            m1.set_dps(0)
            m2.set_dps(0)
            time.sleep(1)
            m1.reset_encoder()
            m2.reset_encoder()
            m1.set_position(-345)
            m2.set_position(345)
        
