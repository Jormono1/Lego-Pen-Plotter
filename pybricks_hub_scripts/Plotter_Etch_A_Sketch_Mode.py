from pybricks.hubs import TechnicHub
from pybricks.iodevices import XboxController
from pybricks.parameters import Direction, Port, Side, Stop, Button
from pybricks.pupdevices import Motor
from pybricks.tools import wait, run_task

X_Motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
Y_Motor = Motor(Port.B)
Z_Motor = Motor(Port.C, Direction.COUNTERCLOCKWISE)
xbox = XboxController()

move_speed = 900
tollerance = 30
paper_x_min = 165
paper_y_min = 400
paper_x_max = 2250
paper_y_max = 1700
allow_x_min = paper_x_min + tollerance
allow_x_max = paper_x_max - tollerance
allow_y_min = paper_y_min + tollerance
allow_y_max = paper_y_max - tollerance
pen_engaged = False
stick_speed = 5

def homing(x_min, y_min):
    Z_Motor.run_until_stalled(move_speed,duty_limit=20)                             # raise pen
    X_Motor.run_until_stalled(-move_speed, duty_limit=18)                           # run until 0
    X_Motor.reset_angle(1)
    Y_Motor.run_until_stalled(-move_speed, duty_limit=20)
    Y_Motor.reset_angle(1)
    X_Motor.run_target(move_speed, x_min + 5, wait=True)
    Y_Motor.run_target(move_speed, y_min + 5, wait=True)                      # puts pen within paper range

def x_can_move(stick):
    if stick >= 0:
        if X_Motor.angle() >= allow_x_max:
            return 0
        else:
            return 1
    elif stick < 0:
        if X_Motor.angle() <= allow_x_min:
            return 0
        else:
            return 1

def y_can_move(stick):
    if stick >= 0:
        if Y_Motor.angle() >= allow_y_max:
            return 0
        else:
            return 1
    elif stick <0:
        if Y_Motor.angle() <= allow_y_min:
            return 0
        else:
            return 1

def main(pen_engaged):
    while True:
        stick_l = xbox.joystick_left()[1]
        stick_r = xbox.joystick_right()[0]
        X_Motor.run(stick_speed * x_can_move(stick_r) * stick_r)
        Y_Motor.run(stick_speed * y_can_move(stick_l) * stick_l)
        if Button.A in xbox.buttons.pressed():
            if pen_engaged:
                Z_Motor.run_until_stalled(move_speed, duty_limit=20)
                pen_engaged = False
            else:
                Z_Motor.run_until_stalled(-move_speed, duty_limit=20)
                pen_engaged = True

homing(allow_x_min, allow_y_min)
main(pen_engaged)