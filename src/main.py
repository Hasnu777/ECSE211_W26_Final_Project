from utils import sound
from utils.brick import TouchSensor, Motor, EV3UltrasonicSensor, wait_ready_sensors, EV3ColorSensor
import time
import threading

C_SENSOR = EV3ColorSensor(1)
wait_ready_sensors(True)
m1 = Motor("A")
m2 = Motor("B")
m1.set_dps(0)
m2.set_dps(0)
m1.reset_encoder()
m2.reset_encoder()
def colour_class():
    # previously calculated cluster centers
    cluster_center = [[0.374809671, 0.558465639, 0.737471218]]
    #previously calculated standard deviations
    cluster_SD = [[0.027033036, 0.042652416, 0.034928918]]
    colour_adj = ["intersect"] #purple, orange & yellow can be included as well

    #RGB values of current block
    RGB = C_SENSOR.get_rgb()
    #print(RGB)
    r = RGB[0]
    g = RGB[1]
    b = RGB[2]
    denom = (r**2 + g**2 + b**2)**0.5
    r = r/denom
    b = b/denom
    g = g/denom
    ls = [r,g,b]
    #print(ls)
    #finding shortest euclidean distance 
    min_d = 1000000
    #repeat for each cluster  
    for i in range (0, len(cluster_center)):
#        d = ((r-cluster_center[i][0])**2 + (g - cluster_center[i][1])**2 + (b - cluster_center[i][2])**2)**0.5
#        if d < min_d:
#            min_d = d
#            current_colour = colour_adj[i]
#         print (abs(r-cluster_center[i][0]))
#         print(cluster_SD[i][0])
#         print (abs(g-cluster_center[i][1]))
#         print(cluster_SD[i][1])
#         print (abs(b-cluster_center[i][2]))
#         print(cluster_SD[i][2])
        if (abs(r-cluster_center[i][0]) > 2*cluster_SD[i][0] or abs(g-cluster_center[i][1]) > 2*cluster_SD[i][1] or abs(b-cluster_center[i][2]) > 2*cluster_SD[i][2]): #reading is too far from sample
            current_color = 'unknown colour, recorded data too far from samples'
        else:
            current_color = "intersect"
    #output
    return current_color

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
        
