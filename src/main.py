from utils import sound
from utils.brick import TouchSensor, Motor, EV3UltrasonicSensor, wait_ready_sensors, EV3ColorSensor
import time
import threading

C_SENSOR = EV3ColorSensor(3)

def colour_class():
    # previously calculated cluster centers
    cluster_center = [[0.374809671, 0.558465639, 0.737471218]]
    #previously calculated standard deviations
    cluster_SD = [[0.027033036, 0.042652416, 0.034928918]]
    colour_adj = ["intersect"] #purple, orange & yellow can be included as well

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