from pybricks.hubs import TechnicHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Direction, Port, Side, Stop
from pybricks.tools import multitask, run_task

### USE CASE ###
# - when using small piece of paper such as an index card
# - measures degrees of rotation from home position to "top left" corner of paper
# - this can be used as an offset to reliably position over paper
# - Can also be used to measure objects and paper in degrees of rotation for travel limits

### INSTRUCTIONS ###
# - manually position plotter such that the pen is located over "top left" corner of the paper
# - run this program, take note of starting positions printed to screen
# - enter those starting positons as coordinates for a movement offset
# - for measuring dimension of something run a second time on the opposite corner (if top left first, bottom right second)
# - the difference between the two pairs of coordinate returns define the size of the object measured in degrees of rotation

### NOTE ###
# - some plotter scripts store coordinates by # * 10 rounded to 0 decimals, then # / 10 when read by the plotter
# - be sure to enter the coordiantes correctly

hub = TechnicHub()
X_Motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
Y_Motor = Motor(Port.B)
Z_Motor = Motor(Port.C, Direction.COUNTERCLOCKWISE)
move_speed = 900
limit = 15

def main():
    Z_Motor.run_until_stalled(move_speed,duty_limit=limit)      # raise pen
    print("Homing X Axis")
    X_Motor.reset_angle(0)
    X_Motor.run_until_stalled(-move_speed, duty_limit=limit)    # run until 0
    print("Starting X position = " + str(X_Motor.angle()))
    print("Homing Y Axis")  
    Y_Motor.reset_angle(0)
    Y_Motor.run_until_stalled(-move_speed, duty_limit=limit)
    print("Starting Y position = " + str(Y_Motor.angle()))

main()
