from src.utils import sound
from src.utils.brick import TouchSensor, Motor, EV3UltrasonicSensor, wait_ready_sensors, EV3ColorSensor
import time
import threading

C_SENSOR = EV3ColorSensor(1)
m1 = Motor("A")
m2 = Motor("B")
wiggleLeft = True

wait_ready_sensors(True)

m1.set_dps(0)
m2.set_dps(0)
m1.reset_encoder()
m2.reset_encoder()


def colour_class():
    # previously calculated cluster centers
    cluster_center = [[0.374809671, 0.558465639, 0.737471218]]
    # previously calculated standard deviations
    cluster_SD = [[0.027033036, 0.042652416, 0.034928918]]
    colour_adj = ["intersect"]  # purple, orange & yellow can be included as well

    # RGB values of current block
    RGB = C_SENSOR.get_rgb()
    # print(RGB)
    r = RGB[0]
    g = RGB[1]
    b = RGB[2]
    denom = (r ** 2 + g ** 2 + b ** 2) ** 0.5
    r = r / denom
    b = b / denom
    g = g / denom
    ls = [r, g, b]
    # print(ls)
    # finding shortest euclidean distance
    min_d = 1000000
    # repeat for each cluster
    for i in range(0, len(cluster_center)):
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
        if (abs(r - cluster_center[i][0]) > 2 * cluster_SD[i][0]
                or abs(g - cluster_center[i][1]) > 2 * cluster_SD[i][1]
                or abs(b - cluster_center[i][2]) > 2 * cluster_SD[i][2]):  # reading is too far from sample
            current_color = 'unknown colour, recorded data too far from samples'
        else:
            current_color = "intersect"
    # output
    return current_color


def wiggle(motor1: Motor, motor2: Motor):
    motor1.set_dps(0)
    time.sleep(0.2)
    motor1.set_dps(80)


if __name__ == "_main__":

    robotState = "wiggling"

    while True:

        inter = colour_class()

        if inter == "intersect":
            state = "intersection"
        elif inter == "door":
            state = "door"
        elif inter == "room":
            state = "room"
        elif inter == "goodBed":
            state = "goodBed"
        elif inter == "badBed":
            state = "badBed"

        match state:
            case "wiggling":
                if wiggleLeft:
                    wiggle(m1, m2)
                else:
                    wiggle(m2, m1)

            case "intersection":
                time.sleep(0.5)
                m1.set_dps(0)
                m2.set_dps(0)
                m1.reset_encoder()
                m2.reset_encoder()
                m1.set_position(-345)
                m2.set_position(345)
                state = "wiggling"

            case "door":
                break
        # m1.set_dps(80)
        # m2.set_dps(80)

        # wiggle(m1, m2)
        #
        # inter = colour_class()
        # if (inter == "intersect"):
        #     print("intersect found. Rotating now")
        #     time.sleep(0.5) # test to see if we can get robot to rotate directly onto new line
        #     m1.set_dps(0)
        #     m2.set_dps(0)
        #     time.sleep(1)
        #     m1.reset_encoder()
        #     m2.reset_encoder()
        #     m1.set_position(-345)
        #     m2.set_position(345)

