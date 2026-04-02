
from utils import sound
from utils.brick import TouchSensor, Motor, EV3UltrasonicSensor, EV3GyroSensor, wait_ready_sensors, reset_brick
import time
from threading import Thread

TS1 = TouchSensor(2)
Gyro = EV3GyroSensor(4,mode="both")
motor_R = Motor("A")
motor_L = Motor("D")

motor_C = Motor("C")
motor_C.set_dps(0)

motor_R.set_dps(0)
motor_L.set_dps(0)

print("Testing file running. Waiting for sensor initialisation...")

wait_ready_sensors(True)
print("Sensors initialized.")


def perform_rotations():
    motor_R.set_limits(power=100)
    motor_L.set_limits(power=100)

    Gyro.set_mode("abs")

    wait_ready_sensors()

    Gyro.reset_measure()

    initialState = Gyro.get_abs_measure()
    print(initialState)


def continuous_measure_gyro():
    global target, running, dps
    while True:
        target = Gyro.get_abs_measure()%360
        dps = Gyro.get_dps_measure()
        time.sleep(0.01)

def maintain_angle(target):
    Gyro.reset_measure()
    while True:
        current = Gyro.get_abs_measure()
        if current != None:
            error = target - current
            correction = error * 0.5
            motor_R.set_position_relative(-correction)
            motor_L.set_position_relative(correction)

if __name__ == "__main__":
#     print_continuous_gyro_data()
#     target = Gyro.get_abs_measure()
#     Gyro.reset_measure()
#     maintain_angle(target)
    target = 0
    dps = 0
    running = True
    t1 = Thread(target = continuous_measure_gyro)
    t1.start()
    
    #right turn overshoot
    start = target
    print(start)
    motor_L.set_position_relative(343)
    motor_R.set_position_relative(-343)
#     dps = 200 #set arbitrary val
    while dps != 0:
        turn = target - start
    print(turn)
    time.sleep(0.1)

#     error = 90-turn
#     if turn != 90:
#         motor_R.set_position_relative(-error)
#         motor_L.set_position_relative(error)
# #     This shit don't work yet
# 
    while True:
#         print("target is " + str(target))
        print("dps is " + str(dps))
        if TS1.is_pressed():
            break
        time.sleep(0.1)
    t1.join()
    # print("reset")
