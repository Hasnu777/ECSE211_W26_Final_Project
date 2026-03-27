from utils.brick import Motor, wait_ready_sensors, TouchSensor
import time

#LW = Motor("B")
#RW = Motor("C")
ARM = Motor("D")
#GRIP = Motor("C")

TS = TouchSensor(3)
#wait_ready_sensors()

#print('touch ts')
#while True:
#    if TS.is_pressed():
#       print('ts touched')
#        ARM.set_dps(0)
#        ARM.reset_encoder()
#        ARM.set_dps(0)
#        time.sleep(1)
#        print('running RW now')
#        ARM.set_dps(100)
#        time.sleep(3)
#        ARM.set_dps(0)

ARM.set_dps(0)
ARM.float_motor()
ARM.reset_encoder()
ARM.set_dps(0)
ARM.set_dps(-100)
time.sleep(1)
ARM.set_dps(0)
