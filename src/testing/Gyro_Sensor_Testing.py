
from utils import sound
from utils.brick import TouchSensor, Motor, EV3UltrasonicSensor, EV3GyroSensor, wait_ready_sensors, reset_brick
import time
import threading

TS1 = TouchSensor(2)
Gyro = EV3GyroSensor(4,mode="both")
motor1 = Motor("A")
motor2 = Motor("B")

GYRO_SENSOR_DATA_FILE = "gyro_sensor_data_file_for_consistency.csv"

print("Testing file running. Waiting for sensor initialisation...")

wait_ready_sensors(True)
print("Sensors initialized.")

def perform_rotations():

    # 90 degree rotation about face
    motor1.set_position_relative(292)
    motor2.set_position_relative(-292)

    time.sleep(3)

    # reverse 90 degree rotation about face
    motor1.set_position_relative(-292)
    motor2.set_position_relative(292)

    time.sleep(3)

    # 90 degree pivot
    motor1.set_position_relative(583)
    motor2.set_position_relative(0)

    time.sleep(3)

    # reverse 90 degree pivot
    motor1.set_position_relative(-583)
    motor2.set_position_relative(0)

    time.sleep(3)

    # 90 degree pivot other way
    motor1.set_position_relative(0)
    motor2.set_position_relative(583)

    time.sleep(3)

    # reverse 90 degree pivot other way
    motor1.set_position_relative(0)
    motor2.set_position_relative(-583)

    time.sleep(3)

    # 180 degree rotation about face
    motor1.set_position_relative(292*2)
    motor2.set_position_relative(-292*2)

    time.sleep(3)

    # reverse 180 degree rotation about face
    motor1.set_position_relative(-292*2)
    motor2.set_position_relative(292*2)

    time.sleep(3)

    # 360 degree rotation about face
    motor1.set_position_relative(292*4)
    motor2.set_position_relative(-292*4)

    time.sleep(3)

    # reverse 360 degree rotation about face
    motor1.set_position_relative(-292*4)
    motor2.set_position_relative(292*4)

    time.sleep(3)
    
    motor1.set_dps(360)
    motor2.set_dps(360)

    time.sleep(3)

    motor1.set_dps(-120)
    motor2.set_dps(-120)
    
    time.sleep(3)
    
    motor1.set_dps(0)
    motor2.set_dps(0)

# def collect_continuous_gyro_data():
#     try:
#         output_file = open(GYRO_SENSOR_DATA_FILE,"w")
#         output_file.write(f"Degrees Rotated Since Beginning,Degrees Rotated Per Second\n")
#         while not TS1.is_pressed():
#             pass
#         time.sleep(0.5)
#         print("Collecting readings now.")
#         Gyro.reset_measure()
#         while not TS1.is_pressed():
#             gyro_data = Gyro.get_both_measure()
#             if gyro_data is not None:
#                 print(gyro_data)
#                 output_file.write(f"{gyro_data[0]},{gyro_data[1]}\n")
#             time.sleep(0.5)
#     except BaseException as e:
#         pass
#     finally:
#         print("Gyro samples collected.")
#         output_file.close()
#         print("Testing complete.")
#         reset_brick()
#         exit()

if __name__ == "__main__":
    perform_rotations()