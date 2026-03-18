from utils import sound
from utils.brick import TouchSensor, Motor, EV3UltrasonicSensor, wait_ready_sensors, EV3ColorSensor
import time
import threading

C_SENSOR = EV3ColorSensor(3)

def colour_class():
    # previously calculated cluster centers
    cluster_center = [[0.973, 0.123, 0.191], [0.179, 0.820, 0.544], [0.206, 0.375, 0.903]]
    #previously calculated standard deviations
    cluster_SD = [[0.000153, 0.00600, 0.00378], [0.00800, 0.00239, 0.00356], [0.00119, 0.00731, 0.00559]]
    colour_adj = ["red", "green", "blue"] #purple, orange & yellow can be included as well

    #RGB values of current block
    r,g,b = C_SENSOR.read()

    #finding shortest euclidean distance 
    min_d = 1000000
    #repeat for each cluster  
    for i in range (0, cluster_center.length ):
        d = ((r-cluster_center[i][0])**2 + (g - cluster_center[i][1])**2 + (b - cluster_center[i][2])**2)**0.5
        if d < min_d:
            min_d = d
            current_colour = colour_adj[i]
        if (r-cluster_center[i][0] > cluster_SD[i][0] or r-cluster_center[i][0] > cluster_SD[i][0] or r-cluster_center[i][0] > cluster_SD[i][0]): #reading is too far from sample
            current_color = 'unknown colour, recorded data too far from samples'
    #output
    print(current_colour)