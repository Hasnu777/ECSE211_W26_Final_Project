
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
    global currentAngle, running, dps
    while running:
        both  = Gyro.get_both_measure()
        currentAngle = both[0]%360
        dps = both[1]
        time.sleep(0.01)

def maintain_angle(currentAngle):
    Gyro.reset_measure()
    while True:
        current = Gyro.get_abs_measure()
        if current != None:
            error = currentAngle - current
            correction = error * 0.5
            motor_R.set_position_relative(-correction)
            motor_L.set_position_relative(correction)

if __name__ == "__main__":
    currentAngle = 0
    dps = 0
    running = True
    t1 = Thread(currentAngle = continuous_measure_gyro)
    t1.start()
    
    #right turn overshoot
    start = currentAngle
    print("angle before rotation is: " + str(start))
    motor_L.set_position_relative(343)
    motor_R.set_position_relative(-343)
    time.sleep(2)
    turn = currentAngle - start
    while turn != 90:
        error = 90 - turn
        print("error is " + str(error))
        correction = error * 0.5
        motor_L.set_position_relative(correction)
        motor_R.set_position_relative(-correction)
    

    while True:
#         print("currentAngle is " + str(currentAngle))
        print("dps is " + str(dps))
        if TS1.is_pressed():
            break
        time.sleep(0.1)
    t1.join()
    # print("reset")
