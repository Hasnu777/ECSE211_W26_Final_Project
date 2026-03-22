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

# BELOW IS HASSANS VERSION OF COLORS FOR UNIT VECTOR NORMALISATION
blue = Color('blue', 0.30514540441303245, 0.42559382484300484, 0.851873554962868, 0.005608173772585627, 0.0052204372086351, 0.0029866701058684276)
green_bed = Color('green bed', 0.5288572659051487, 0.8153196582255317, 0.23555251920848586, 0.005051739881859017, 0.0036444174525583476, 0.006328984947554189)
orange = Color('orange', 0.9193282736567624, 0.3582026489175016, 0.1625743547752035, 0.002830838124651885, 0.005676075368760179, 0.007465604939214666)
red_bed = Color('red bed',0.9682768290485266, 0.1479864922467923, 0.20072730902491995, 0.0032287074234957965, 0.011164373185914777, 0.010651763777604661)
thick_intersection = Color('thick intersection', 0.35875595176919356, 0.5148258450215546, 0.7764796797011159, 0.040709680400056375, 0.030394450281119235, 0.027326227202242318)
thick_line = Color('thick line', 0.4222264010998929, 0.6081623186340988, 0.6704320827701554, 0.032236153045677625, 0.02623960306083702, 0.025624138391881688)
thin_intersection = Color('thin intersection',0.5084433516212437, 0.5503023933503505, 0.6590710630695044, 0.04161211492811081, 0.03563952336368879, 0.03572427963003056)
thin_line = Color('thin line', 0.5885948428200825, 0.4231970291051555, 0.6883294479534854, 0.014673265027663585, 0.01581006368544569, 0.014060363505711054)
white = Color('white', 0.47856765654917144, 0.4751915744144273, 0.7383455020642785, 0.0020329695461371975, 0.0022002083544665546, 0.001706285451531559)
yellow = Color('yellow', 0.7793133994249224, 0.5986100822841631, 0.18516968094855718, 0.002988667062624679, 0.0035148365461744385, 0.005243845456394571)

# array with all the colors
all_colors = [blue, green_bed, orange, red_bed, thick_intersection, thick_line, thin_intersection, thin_line, white, yellow]
 
# Purpose of following method: Color sensor reads and identifies to what color a new color reading belongs to
def classify_unknown_color():
    # Collect raw rgb
    raw_rgb = color_sensor.get_rgb()
    raw_r = raw_rgb[0]
    raw_g = raw_rgb[1]
    raw_b = raw_rgb[2]
    print("Detected color info:", raw_r, raw_g, raw_b)

    # Normalizing the RGB values
    denominator = (raw_r**2 + raw_g**2 + raw_b**2)**0.5 # UNIT VECTOR METHOD
    # denominator = (raw_r + raw_g + raw_b) # RATIO METHOD
    norm_r = raw_r/denominator
    norm_b = raw_b/denominator
    norm_g = raw_g/denominator

#     norm_r = raw_r
#     norm_g = raw_g
#     norm_b = raw_b

    print("Detected color norm info:", norm_r, norm_g, norm_b)

    # Loop through each color and find distance between unknown color and all measured known colors
    best_distance = 100000000 # arbitrarily set a big number
    best_color = []
    best_colors = {}

    print_counter = 0
    norm_counter = 0
    # Iterate through colors to find the closest match
    for i in range(len(all_colors)):
        color = all_colors[i]
        print("Trying to match detected color to:", color.get_name())
        distance = color.find_distance(norm_r, norm_g, norm_b)
        print(print_counter, color.name, distance)
        print_counter += 1
        best_colors[distance] = i

    distances = sorted(list(best_colors.keys()))
    for i in range(3):
        color_to_check = all_colors[best_colors[distances[i]]]
        if color_to_check.is_match(norm_r, norm_g, norm_b) and i == 0:
            return f"{color_to_check.get_name()} matched to detected color. Closest three are: {all_colors[best_colors[distances[0]]].get_name()}, {all_colors[best_colors[distances[1]]].get_name()}, {all_colors[best_colors[distances[0]]].get_name()}"
    return f"unknown, after checking closest 3 colors: {best_colors[distances[0]].get_name()}, {best_colors[distances[1]].get_name()}, {best_colors[distances[2]].get_name()}"

        # if (distance < best_distance):
        #     print("Updated distance:", distance)
        #     best_distance = distance
        #     best_color = color

    # check if closest matching known color is < 5 SD's to the detected color

    # print("Trying to match to color:",best_color.get_name())
    # if (best_color.is_match(norm_r, norm_g, norm_b)):
    #     print(norm_r, norm_g, norm_b, "matched")
    #     return best_color.get_name()
    #
    # print("More than 2 SDs away")
    # return "unknown"
    

if __name__ == "__main__":
    exe_counter = 1
    while True:
        time.sleep(4)
        print("Attempt number", exe_counter)
        exe_counter += 1
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
        
