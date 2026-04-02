
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
    motor_R.set_limits(power=80)
    motor_L.set_limits(power=80)

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
    # currentAngle = 0
    # dps = 0
    # running = True
    # t1 = Thread(target = continuous_measure_gyro)
    # t1.start()
    
    #right turn overshoot
    Gyro.reset_measure()
    start = Gyro.get_abs_measure()
    print("start is " + str(start))
    motor_L.set_position_relative(500) #rotate 90 degrees, overshot
    motor_R.set_position_relative(-500)
    time.sleep(2)
    print ("current angle is " + str(Gyro.get_abs_measure()))
    delta = Gyro.get_abs_measure() - start
    print("delta is " + str(delta))
    while not (delta < 92 and delta > 88):
        print("while loop entered")
        current = Gyro.get_abs_measure()
        delta =  current - start
        error = (start + 90) - delta
        print("error is " + str(error))
          
        correction = error * 0.5
#         motor_L.set_position_relative(correction)
#         motor_R.set_position_relative(-correction) 
        

        while abs(error) > 1:
            if error > 1:
                print("overshot")
                motor_L.set_position_relative(-correction)
                motor_R.set_position_relative(correction)
                
                time.sleep(0.2)
                error = (start + 90) - delta
                correction = error*0.5
                current = Gyro.get_abs_measure()
                delta =  current - start
            elif error < -1:
                print("undershot")
                motor_L.set_position_relative(correction)
                motor_R.set_position_relative(-correction)
              
                time.sleep(0.2)
                error = (start + 90) - delta
                correction = error*0.5
                current = Gyro.get_abs_measure()
                delta =  current - start
    while True:
#         print("currentAngle is " + str(currentAngle))
        print("dps is " + str(dps))
        if TS1.is_pressed():
            break
        time.sleep(0.1)
    # t1.join()
    # print("reset")
