]

async def homing():
    await Z_Motor.run_until_stalled(move_speed,duty_limit=20)  # raise pen
    print("Homing X Axis")
    ### I've observed that the X motor limit has required adjustment based on remaining battery capacity ###
    ### set to 15 when battery is fresh, set to 18 when battery is low ###
    ### when battery fresh too high of a threshold it will skip gears and not stop at 0 point ###
    ### when battery is low a high threshold can cause it to read high torque without any movement to 0 point ###
    await X_Motor.run_until_stalled(-move_speed, duty_limit=15)    # run until 0
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


