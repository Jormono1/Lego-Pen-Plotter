from pybricks.hubs import TechnicHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = TechnicHub()
X_Motor = Motor(Port.A)
Y_Motor = Motor(Port.B, Direction.COUNTERCLOCKWISE)
Z_Motor = Motor(Port.C, Direction.COUNTERCLOCKWISE)
set_speed1 = 500
set_speed2 = 200
set_speed3 = 100
x_limits = X_Motor.control.limits()
print("Default speed = " + str(x_limits[0]))
print("Default acceleration = " + str(x_limits[1]))
print("Default torque = " + str(x_limits[2]))

def movement_loop(speed):
    X_Motor.track_target(2000)
    while not X_Motor.done():
        wait(1)
    Y_Motor.track_target(2000)
    while not Y_Motor.done():
        wait(1)
    X_Motor.run_target(speed, 200, wait=True)
    Y_Motor.run_target(speed, 200, wait=True)

def homing():
    print("Homing")
    X_Motor.run_until_stalled(-set_speed3, duty_limit=15)    # run until 0
    X_Motor.reset_angle(0)
    Y_Motor.run_until_stalled(-set_speed3, duty_limit=15)
    Y_Motor.reset_angle(0)

def main():
    homing()
    
    X_Motor.control.limits(speed=set_speed1)
    Y_Motor.control.limits(speed=set_speed1)
    print("Motor speed set to ", str(set_speed1))
    movement_loop(set_speed1)

    X_Motor.control.limits(speed=set_speed2)
    Y_Motor.control.limits(speed=set_speed2)
    print("Motor speed set to ", str(set_speed2))
    movement_loop(set_speed2)

    X_Motor.control.limits(speed=set_speed3)
    Y_Motor.control.limits(speed=set_speed3)
    print("Motor speed set to ", str(set_speed3))
    movement_loop(set_speed3)

    homing()

main()
