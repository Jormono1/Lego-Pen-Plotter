#This file will write the following: HELLO WORLD
#Formatted for an index card
from pybricks.hubs import TechnicHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Direction, Port, Side, Stop
from pybricks.tools import multitask, run_task

hub = TechnicHub()
X_Motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
Y_Motor = Motor(Port.B)
Z_Motor = Motor(Port.C, Direction.COUNTERCLOCKWISE)
move_speed = 900

### Coordinates are in [X, Y, Z] format ###
### False means no change, ignore ###
Coordinates = [[62,2000,False],
[343,1800,False],
[False,False,"D"],
[False,1960,False],
[False,False,"U"],
[423,False,False],
[False,False,"D"],
[False,1800,False],
[False,False,"U"],
[343,1880,False],
[False,False,"D"],
[423,False,False],
[False,False,"U"],
[463,1800,False],
[543,False,False],
[False,False,"D"],
[463,False,False],
[False,1960,False],
[543,False,False],
[False,False,"U"],
[463,1880,False],
[False,False,"D"],
[503,False,False],
[False,False,"U"],
[583,1800,False],
[663,False,False],
[False,False,"D"],
[583,False,False],
[False,1960,False],
[False,False,"U"],
[703,1800,False],
[783,False,False],
[False,False,"D"],
[703,False,False],
[False,1960,False],
[False,False,"U"],
[823,1800,False],
[863,False,False],
[False,False,"D"],
[823,1840,False],
[False,1920,False],
[863,1960,False],
[903,False,False],
[943,1920,False],
[False,1840,False],
[903,1800,False],
[863,False,False],
[False,False,"U"],
[983,False,False],
[1063,False,False],
[False,1960,False],
[False,False,"D"],
[False,1800,False],
[1143,1880,False],
[1223,1800,False],
[False,1960,False],
[False,False,"U"],
[1263,1800,False],
[1303,False,False],
[False,False,"D"],
[1263,1840,False],
[False,1920,False],
[1303,1960,False],
[1343,False,False],
[1383,1920,False],
[False,1840,False],
[1343,1800,False],
[1303,False,False],
[False,False,"U"],
[1423,False,False],
[False,False,"D"],
[False,1960,False],
[1463,False,False],
[1503,1920,False],
[1463,1880,False],
[1423,False,False],
[1503,1800,False],
[False,False,"U"],
[1543,False,False],
[1623,False,False],
[False,False,"D"],
[1543,False,False],
[False,1960,False],
[False,False,"U"],
[1663,1800,False],
[False,False,"D"],
[False,1960,False],
[1703,False,False],
[1743,1920,False],
[False,1840,False],
[1703,1800,False],
[1663,False,False],
[False,False,"U"],
[1783,False,False],
[2064,2000,False]]

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
