### standard mode: Hub light = Left stick up/down controls Y motor. Left stick left/right controls X motor ###
### alt mode: Hub light = Red, Blue, Left stick up/down controls Y motor. Right stick left/right controls X motor ###
### Y button triggers homing sequence, X button Toggles standard/alt modes ###
### LB button reduces speed, RB button increases speed ###

### IF FRESH BATTERIES change value on line 36 to 15, if not fresh revert to 18 ###
from pybricks.hubs import TechnicHub
from pybricks.iodevices import XboxController
from pybricks.parameters import Direction, Port, Side, Stop, Button, Color
from pybricks.pupdevices import Motor
from pybricks.tools import wait, run_task

X_Motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
Y_Motor = Motor(Port.B)
Z_Motor = Motor(Port.C, Direction.COUNTERCLOCKWISE)
xbox = XboxController()
hub = TechnicHub()

move_speed = 900                                                                # move speed for homing function
tollerance = 30                                                                 # border inset from paper minimum
paper_x_min = 165                                                               # defines boundry of paper
paper_y_min = 500
paper_x_max = 2250
paper_y_max = 1700
allow_x_min = paper_x_min + tollerance
allow_x_max = paper_x_max - tollerance
allow_y_min = paper_y_min + tollerance
allow_y_max = paper_y_max - tollerance
pen_engaged = False
stick_speed = 5                                                                 # user controlled speed, starts at 5 can range from 1 to 10 incremented by 0.5
alt_control = False                                                             # allows user to toggle between two different control stick layouts
button_wait = 200                                                               # prevents button bounce on inputs

def homing(x_min, y_min):
    Z_Motor.run_until_stalled(move_speed,duty_limit=20)                         # raise pen
    X_Motor.run_until_stalled(-move_speed, duty_limit=18) # change to 15 if fresh battery
    X_Motor.reset_angle(1)
    Y_Motor.run_until_stalled(-move_speed, duty_limit=20)
    Y_Motor.reset_angle(1)
    X_Motor.run_target(move_speed, x_min + 5, wait=True)
    Y_Motor.run_target(move_speed, y_min + 5, wait=True)                        # puts pen within paper range

def x_can_move(stick):                                                          # Checks current position against paper boundaries
    if stick >= 0:
        if X_Motor.angle() >= allow_x_max:                                      # ignores input above max and below min but doesn't prevent return to allowable area
            return 0
        else:
            return 1                                                            # returns 1 or 0, this is multiplied into the motor speed, if 0 motor will not rotate
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

def main(pen_engaged, stick_speed, x_min, y_min, alt_control, button_wait):
    while True:
        if alt_control:                                                         # alt control is on, x on right stick y on left stick
            stick_y = xbox.joystick_left()[1]
            stick_x = xbox.joystick_right()[0]
        else:                                                                   # standard control, x and y movement controlled by left stick
            stick_y = xbox.joystick_left()[1]
            stick_x = xbox.joystick_left()[0]
        X_Motor.run(round(stick_speed * x_can_move(stick_x) * stick_x))         # round because stick speed can be a float
        Y_Motor.run(round(stick_speed * y_can_move(stick_y) * stick_y))
        if Button.A in xbox.buttons.pressed():                                  # A button toggles pen engagment
            if pen_engaged:
                Z_Motor.run_until_stalled(move_speed, duty_limit=20)
                pen_engaged = False
            else:
                Z_Motor.run_until_stalled(-move_speed, duty_limit=20)
                pen_engaged = True
        elif Button.Y in xbox.buttons.pressed():                                # Y button triggers homing sequence
            homing(x_min, y_min)
        elif Button.X in xbox.buttons.pressed():                                # X button toggles control mode
            if alt_control:
                hub.light.on(Color.BLUE)
                alt_control = False
                wait(button_wait)
            else:
                hub.light.on(Color.RED)
                alt_control = True
                wait(button_wait)
        elif Button.LB in xbox.buttons.pressed():                               # LB button decreases speed multiplier
            if stick_speed > 1:
                stick_speed -= 0.5
                wait(button_wait)
        elif Button.RB in xbox.buttons.pressed():                               # RB button increases speed multiplier
            if stick_speed < 10:
                stick_speed += 0.5      
                wait(button_wait)          
homing(allow_x_min, allow_y_min)
main(pen_engaged, stick_speed, allow_x_min, allow_y_min, alt_control, button_wait)
