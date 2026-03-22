
from utils import sound
from utils.brick import TouchSensor, Motor, EV3UltrasonicSensor, EV3GyroSensor, wait_ready_sensors, reset_brick
import time
import threading

TS1 = TouchSensor(2)
Gyro = EV3GyroSensor(3,mode="both")
motor1 = Motor("A")
motor2 = Motor("B")

motor1.set_dps(0)
motor2.set_dps(0)

GYRO_SENSOR_DATA_FILE = "gyro_sensor_straight.txt"

print("Testing file running. Waiting for sensor initialisation...")

wait_ready_sensors(True)
print("Sensors initialized.")

file = open(GYRO_SENSOR_DATA_FILE, mode="a")

def perform_rotations():

#     motor1.float_motor()
#     motor2.float_motor()
    motor1.set_limits(power=50)
    motor2.set_limits(power=50)

    Gyro.set_mode("abs")

    wait_ready_sensors()

    Gyro.reset_measure()

    initialState = Gyro.get_abs_measure()
    print(initialState)

#     if initialState is None:
#         print("weird")
    while initialState is None or not 0:
        if initialState == 0:
            break
        Gyro.reset_measure()
        initialState = Gyro.get_abs_measure()
        print(initialState)
        if initialState == 0:
            break 
    
    file.write("Initial state: 0\n")

if __name__ == "__main__":
    perform_rotations()
    for i in range(10):
        motor1.set_dps(360)
        motor2.set_dps(360)
        file.write(str(Gyro.get_abs_measure()) + "\n")
        time.sleep(1)

    motor1.set_dps(0)
    motor2.set_dps(0)

    file.close()

#
#     # 90 degree rotation about face
#     motor1.set_position_relative(320)
#     motor2.set_position_relative(-320)
#
#     file.write("\nExpected 90, got: " + str(Gyro.get_abs_measure()))
#
#     Gyro.reset_measure()
#
#     print(Gyro.get_abs_measure())
#
#     time.sleep(3)
#
#     file.write("\nExpected 90, got: " + str(Gyro.get_abs_measure()))
#
#     Gyro.reset_measure()
#
#     # reverse 90 degree rotation about face
#     motor1.set_position_relative(-320)
#     motor2.set_position_relative(320)
#
#     file.write("\nExpected 90, got: " + str(Gyro.get_abs_measure()))
#
#     Gyro.reset_measure()
#
#     time.sleep(3)
#
#     # 90 degree pivot
#     motor1.set_position_relative(610)
#     motor2.set_position_relative(0)
#
#     file.write("\nExpected 90, got: " + str(Gyro.get_abs_measure()))
#
#     Gyro.reset_measure()
#
#     time.sleep(3)
#
#     file.write("\nExpected 90, got: " + str(Gyro.get_abs_measure()))
#
#     Gyro.reset_measure()
#
#     # reverse 90 degree pivot
#     motor1.set_position_relative(-610)
#     motor2.set_position_relative(0)
#
#     time.sleep(3)
#
#     file.write("\nExpected 90, got: " + str(Gyro.get_abs_measure()))
#
#     Gyro.reset_measure()
#
#     # 90 degree pivot other way
#     motor1.set_position_relative(0)
#     motor2.set_position_relative(610)
#
#     time.sleep(3)
#
#     file.write("\nExpected 90, got: " + str(Gyro.get_abs_measure()))
#
#     Gyro.reset_measure()
#
#     # reverse 90 degree pivot other way
#     motor1.set_position_relative(0)
#     motor2.set_position_relative(-610)
#
#     file.write("\nExpected 90, got: " + str(Gyro.get_abs_measure()))
#
#     Gyro.reset_measure()
#
#     time.sleep(3)
#
#     # 180 degree rotation about face
#     motor1.set_position_relative(330*2)
#     motor2.set_position_relative(-330*2)
#
#     file.write("\nExpected 180, got: " + str(Gyro.get_abs_measure()))
#
#     Gyro.reset_measure()
#
#     time.sleep(3)
#
#     # reverse 180 degree rotation about face
#     motor1.set_position_relative(-330*2)
#     motor2.set_position_relative(330*2)
#
#     file.write("\nExpected 180, got: " + str(Gyro.get_abs_measure()))
#
#     Gyro.reset_measure()
#
#     time.sleep(3)
#
#     # 360 degree rotation about face
#     motor1.set_position_relative(330*4)
#     motor2.set_position_relative(-330*4)
#
#     file.write("\nExpected 360, got: " + str(Gyro.get_abs_measure()))
#
#     Gyro.reset_measure()
#
#     time.sleep(3)
#
#     # reverse 360 degree rotation about face
#     motor1.set_position_relative(-330*4)
#     motor2.set_position_relative(330*4)
#
#     file.write("\nExpected 360, got: " + str(Gyro.get_abs_measure()))
#
#     Gyro.reset_measure()
#
#     time.sleep(3)
#
#     motor1.set_dps(360)
#     motor2.set_dps(360)
#
#     time.sleep(3)
#
#     file.write("\nExpected 0, got: " + str(Gyro.get_abs_measure()))
#
#     Gyro.reset_measure()
#
#     motor1.set_dps(-360)
#     motor2.set_dps(-360)
#
#     time.sleep(3)
#
#     file.write("\nExpected 0, got: " + str(Gyro.get_abs_measure()))
#
#     Gyro.reset_measure()
#
#     motor1.set_dps(0)
#     motor2.set_dps(0)
#
#     file.close()

def collect_continuous_gyro_data():
    try:
        output_file = open(GYRO_SENSOR_DATA_FILE,"w")
        output_file.write(f"Degrees Rotated Since Beginning,Degrees Rotated Per Second\n")
        while not TS1.is_pressed():
            pass
        time.sleep(0.5)
        print("Collecting readings now.")
        Gyro.reset_measure()
        while not TS1.is_pressed():
            time.sleep(3)
            gyro_data = Gyro.get_both_measure()
            if gyro_data is not None:
                print(gyro_data)
                output_file.write(f"{gyro_data[0]},{gyro_data[1]}\n")
            time.sleep(0.5)
    except BaseException as e:
        pass
    finally:
        print("Gyro samples collected.")
        output_file.close()
        print("Testing complete.")
        reset_brick()
        exit()

# if __name__ == "__main__":
#     Gyro.reset_measure()
#     # perform_rotations()
#     collect_continuous_gyro_data()