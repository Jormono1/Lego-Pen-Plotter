from pybricks.hubs import TechnicHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Direction, Port, Side, Stop
from pybricks.tools import multitask, run_task
from umath import sqrt

hub = TechnicHub()
X_Motor = Motor(Port.A)
Y_Motor = Motor(Port.B, Direction.COUNTERCLOCKWISE)
Z_Motor = Motor(Port.C, Direction.COUNTERCLOCKWISE)
move_speed = 900
prev_x = 1
prev_y = 1
pen_status = False      # FALSE means pen up, TRUE means pen down. Machine should start with pen in up position.

### Coordinates are in [X, Y, Z] format ###
### False means no change, ignore ###
### Values are multiplied by 10 and rounded to make them whole numbers ###
### Float values would take up substantially more memory which is fairly limited in the hub ###
Coordinates = [[249, 2526, False],
[False, False, 1],
[6378, 163, False],
[5495, 4122, False],
[5546, 4105, False],
[1, 1, 46]]

async def homing():     # initializes machine, ensuring consistent results
    await Z_Motor.run_until_stalled(move_speed,duty_limit=20)  # raise pen
    print("Homing X Axis")
    await X_Motor.run_until_stalled(-move_speed, duty_limit=20)    # run until 1
    X_Motor.reset_angle(1)
    print("Homing Y Axis")
    await Y_Motor.run_until_stalled(-move_speed, duty_limit=20)
    Y_Motor.reset_angle(1)

async def move (motor, coord, speed=move_speed):        # when only x, y, or z coordinate changes only move one motor
    await motor.run_target(speed, coord, wait=True)

async def speed_calc (distance, time):
    speed = distance / time
    speed = round(speed)
    speed = int(speed)
    return speed

async def xy_move (x, y):                               # both x and y coordinates change, both motors need to move
    if pen_status == False:                              # if pen is up two consecutive single motor movements are acceptable and easier
        move(X_Motor, x)
        move(Y_Motor, y)
        return

    xy_travel = sqrt(pow(x-prev_x,2) + pow(y-prev_y,2))
    x_travel = abs(prev_x - x)
    y_travel = abs(prev_y - y)
    time_x = x_travel / move_speed
    time_y = y_travel / move_speed
    speed_x = move_speed
    speed_y = move_speed

    if time_x > time_y:                 # if X moves further
        speed_x = int(speed_calc(x_travel, time_y))     # adjust movement speed up to keep pace with y
        if speed_x > 1100:
            speed_x = 1100
            time_x = x_travel / speed_x
            speed_y = int(speed_calc(y_travel, time_x))
        elif speed_x < 500:
            speed_x = 500
            time_x = x_travel / speed_x
            speed_y = int(speed_calc(y_travel, time_x))

        speed_x = round(speed_x,0)  # motor speed must be whole number integer
        speed_x = int(speed_x)
    elif time_y > time_x:               # repeat but Y moves further
        speed_y = int(speed_calc(y_travel, time_x))
        if speed_y > 1100:
            speed_y = 1100
            time_y = y_travel / speed_y
            speed_x = int(speed_calc(x_travel, time_y))
        elif speed_y < 500:
            speed_y = 500
            time_y = y_travel / speed_y
            speed_x = int(speed_calc(x_travel, time_y))

        speed_y = round(speed_y,0)
        speed_y = int(speed_y)

    x_limit = X_Motor.control.limits()
    y_limit = Y_Motor.control.limits()

    print("X motor speed = ", str(speed_x))
    print("Y motor speed = ", str(speed_y))
    
    X_Motor.control.limits(speed=speed_x)
    Y_Motor.control.limits(speed=speed_y)

    await multitask(X_Motor.track_target(x), Y_Motor.track_target(y))
    while not X_Motor.done() and not Y_Motor.done():
        wait(1)
    
    X_Motor.control.limits(speed= x_limit[0])
    Y_Motor.control.limits(speed= y_limit[0])

    
async def main():       # Main loop, read coordinates and call movement functions 
    for line in Coordinates:
        X = line[0]
        Y = line[1]
        Z = line[2]

        if (X != False) and (Y != False):       # moving at an angle
            print("Moving to: " + str(X/10) + ", " + str(Y/10))
            await xy_move(float(X/10), float(Y/10))
            prev_x = X/10
            prev_y = Y/10

        elif (X != False) and (Y == False):     # moving along x axis
            print("Moving to: " + str(X/10))
            await move(X_Motor, float(X/10))
            prev_x = X/10

        elif (Y != False) and (X == False):     # moving along y axis
            print("Moving to: " + str(Y/10))
            await move(Y_Motor, float(Y/10))
            prev_y = Y/10

        elif Z != False:                        # pen up or down
            if Z == 46: # 0 and 45 were originally target angles, but some modifications to my build reduced the limit of travel, values are now arbitrary
                print("Pen Up")
                await Z_Motor.run_until_stalled(move_speed, duty_limit=15)
                pen_status = False
            elif Z == 1:
                print("Pen Down")
                await Z_Motor.run_until_stalled(-move_speed, duty_limit=15)
                pen_status = True
    print("all done")

run_task(homing())
run_task(main())
