from utils import sound
from utils.brick import TouchSensor, Motor, EV3UltrasonicSensor, wait_ready_sensors
import time
import threading

m1 = Motor("C")
gripper = Motor("D")
m1.set_limits(power=30)
gripper.set_limits(power=30)
#m1.reset_encoder()

def setup():
    m1.set_position(0)
    
def loop_grab():
    while(True):
        print("test")
        m1.set_position(70) #if want claw closer, increase absolute value
        time.sleep(0.5)
        m1.set_position(0)
        time.sleep(0.5)

def single_grab():
    m1.set_position(-110) #if want claw closer, increase absolute value

def reset_position_of_claw():
    m1.set_position(0)
    

if __name__ == "__main__":
    setup() # Should never be commented
    #loop_grab() # Uncomment to grap in a loop
    #single_grab() # Uncomment to grap once
    #reset_position_of_claw()
    
    # Wrist Movement
#     time.sleep(1)
#     while(True):
#         gripper.set_position(-50)
#         time.sleep(1)
#         gripper.set_position(10)
#         time.sleep(1)
        
    time.sleep(1)
    
#    gripper.set_position(-50)
#     m1.set_position(0)
#     time.sleep(3)
#     gripper.set_position(-50)
#     time.sleep(2)
    gripper.set_position(10)
    time.sleep(1)
    m1.set_position(180)
    time.sleep(1)
    gripper.set_position(-50)
    time.sleep(1)
    m1.set_position(0)
    time.sleep(1)
    gripper.set_position(10)
    time.sleep(2)
    gripper.set_position(-50)
    m1.set_position(185)
    time.sleep(1)
    gripper.set_position(10)
    time.sleep(1)
    m1.set_position(0)
    time.sleep(1)
    gripper.set_position(-50)

    
    # Shoulder Movement
#     time.sleep(1)
#     while(True):
#         m1.set_position(180)
#         time.sleep(1)
#         m1.set_position(0)
#         time.sleep(1)
        


    





