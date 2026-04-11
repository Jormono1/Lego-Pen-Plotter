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

### if you run both motors at the same speed over different distances it will not result in a straight line ###
### instead run motor with less distance to travel proportionately slower so they take the same overall time and result in a straight line ###
async def xy_move (x, y):
    x_travel = abs(prev_x - x)
    y_travel = abs(prev_y - y)
    if x_travel > y_travel:
        x_time = x_travel/move_speed # degrees movement / degrees per second speed = seconds of travel
        y_speed = y_travel/x_time    # travel distance / seconds of travel = degrees per second speed
        if y_speed < 100:           # handles minimum speed for Y motor
            y_time = y_travel/100
            x_speed = x_travel/y_time
            speed = [x_speed, 100]
        else:
            speed = [move_speed, y_speed]
    elif y_travel > x_travel:           # if Y has to move further than X
        y_time = y_travel/move_speed   # Y will take this time to travel the required distance at default speed
        x_speed = x_travel/y_time      # x will need to travel this reduced speed to keep pace with y
        if x_speed < 75:               # if speed below given minimum, motor doesn't seem to work correctly
            x_time = x_travel/75       # scales up speed for longer segement and scales down speed for shorter segment to min
            y_speed = y_travel/x_time
            speed = [75, y_speed]
        else:
            speed = [x_speed, move_speed]
    elif y_travel == x_travel:         # in the off chance they do travel same distance (45 degree angle) they can run the same speed
        speed = [move_speed, move_speed]
    await multitask(move(X_Motor, x, speed[0]), move(Y_Motor, y, speed[1]))

async def main():
    for line in Coordinates:
        X = line[0]
        Y = line[1]
        Z = line[2]

        if (X != False) and (Y != False):
            print("Moving to: " + str(X/10) + ", " + str(Y/10))
            await xy_move(float(X/10), float(Y/10))
            prev_x = X/10
            prev_y = Y/10

        elif (X != False) and (Y == False):
            print("Moving to: " + str(X/10))
            await move(X_Motor, float(X/10))
            prev_x = X/10

        elif (Y != False) and (X == False):
            print("Moving to: " + str(Y/10))
            await move(Y_Motor, float(Y/10))
            prev_y = Y/10

        elif Z != False:
            if Z == 46: # 0 and 45 were originally target angles, but some modifications to my build reduced the limit of travel, values are now arbitrary
                print("Pen Up")
                await Z_Motor.run_until_stalled(move_speed, duty_limit=15)
            elif Z == 1:
                print("Pen Down")
                await Z_Motor.run_until_stalled(-move_speed, duty_limit=15)
    print("all done")

run_task(homing())
run_task(main())
