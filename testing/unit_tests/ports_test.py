"""
Purpose of this files: Testing if the ports work
How to test with this code?:

"""

from testing.unit_tests.utils.brick import Motor

# -------------------- MOTOR TEST --------------------
m = Motor("A")
m.set_limits(power=50)
m.set_position_relative(360)

# -------------------- SENSORS AND MOTORS --------------------
"""
s = TouchSensor(1)
while (True):
    if (s.isPressed()):
        print("pressed")
    print("pressed")
"""