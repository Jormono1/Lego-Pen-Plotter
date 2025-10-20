from pybricks.hubs import TechnicHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Direction, Port, Side, Stop
from pybricks.tools import multitask, run_task

hub = TechnicHub()
X_Motor = Motor(Port.A)
Y_Motor = Motor(Port.B, Direction.COUNTERCLOCKWISE)
Z_Motor = Motor(Port.C, Direction.COUNTERCLOCKWISE)
move_speed = 900

### Coordinates are in [X, Y, Z] format ###
### False means no change, ignore ###
Coordinates = [[252.0,250,False],
[False,False,"D"],
[False,450,False],
[False,False,"U"],
[352,False,False],
[False,False,"D"],
[False,250,False],
[False,False,"U"],
[252,350,False],
[False,False,"D"],
[352,False,False],
[False,False,"U"],
[402,250,False],
[502,False,False],
[False,False,"D"],
[402,False,False],
[False,450,False],
[502,False,False],
[False,False,"U"],
[402,350,False],
[False,False,"D"],
[452,False,False],
[False,False,"U"],
[552,250,False],
[652,False,False],
[False,False,"D"],
[552,False,False],
[False,450,False],
[False,False,"U"],
[702,250,False],
[802,False,False],
[False,False,"D"],
[702,False,False],
[False,450,False],
[False,False,"U"],
[852,250,False],
[902,False,False],
[False,False,"D"],
[852,300,False],
[False,400,False],
[902,450,False],
[952,False,False],
[1002,400,False],
[False,350,False],
[952,300,False],
[902,False,False],
[False,False,"U"],
[1052,False,False],
[1152,False,False],
[False,500,False],
[False,False,"D"],
[False,300,False],
[1252,400,False],
[1352,300,False],
[False,500,False],
[False,False,"U"],
[1402,300,False],
[1452,False,False],
[False,False,"D"],
[1402,350,False],
[False,450,False],
[1452,500,False],
[1502,False,False],
[1552,450,False],
[False,400,False],
[1502,350,False],
[1452,False,False],
[False,False,"U"],
[1602,False,False],
[False,False,"D"],
[False,550,False],
[1652,False,False],
[1702,500,False],
[1652,450,False],
[1602,False,False],
[1702,350,False],
[False,False,"U"],
[1752,False,False],
[1852,False,False],
[False,False,"D"],
[1752,False,False],
[False,550,False],
[False,False,"U"],
[1902,350,False],
[False,False,"D"],
[False,550,False],
[1952,False,False],
[2002,500,False],
[False,400,False],
[1952,350,False],
[1902,False,False],
[False,False,"U"],
[2052,False,False],
[1,1,False]]

async def homing():
    await Z_Motor.run_until_stalled(move_speed,duty_limit=20)  # raise pen
    print("Homing X Axis")
    await X_Motor.run_until_stalled(-move_speed, duty_limit=20)    # run until 0
    X_Motor.reset_angle(1)
    print("Homing Y Axis")
    await Y_Motor.run_until_stalled(-move_speed, duty_limit=20)
    Y_Motor.reset_angle(1)

async def move (motor, coord, speed=move_speed):
    await motor.run_target(speed, coord, wait=True)

async def xy_move(x, y, speed=move_speed):
 await multitask(move(X_Motor, x), move(Y_Motor, y))

async def main():
    for line in Coordinates:
        X = line[0]
        Y = line[1]
        Z = line[2]

        if (X != False) and (Y != False):
            print("Moving to: " + str(X) + ", " + str(Y))
            await xy_move(X, Y)


        elif (X != False) and (Y == False):
            print("Moving to: " + str(X))
            await move(X_Motor, X)

        elif (Y != False) and (X == False):
            print("Moving to: " + str(Y))
            await move(Y_Motor, Y)


        elif Z != False:
            if Z == "U":
                print("Pen Up")
                await Z_Motor.run_until_stalled(move_speed, duty_limit=15)
            elif Z == "D":
                print("Pen Down")
                await Z_Motor.run_until_stalled(-move_speed, duty_limit=15)
    print("all done")

run_task(homing())
run_task(main())