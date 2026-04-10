"""
Purpose of this files: Testing if a specific port work

How to test with this code?:
Uncomment either the motor or sensor section depending on if you want to test a sensor port or a motor port
"""

from utils.brick import Motor

# -------------------- MOTOR PORTS TEST --------------------
m = Motor("A")
m.set_limits(power=50)
m.set_position_relative(360)

# -------------------- SENSORS PORTS TEST --------------------
"""
s = TouchSensor(1)
while (True):
    if (s.isPressed()):
        print("pressed")
    print("pressed")
"""