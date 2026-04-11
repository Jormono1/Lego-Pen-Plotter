from pybricks.hubs import TechnicHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Direction, Port,Stop

hub = TechnicHub()
X_Motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
Y_Motor = Motor(Port.B)
Z_Motor = Motor(Port.C, Direction.COUNTERCLOCKWISE)
move_speed = 900
limit = 15

def main():
    Z_Motor.run_until_stalled(move_speed,duty_limit=limit)      # raise pen
   
    ### Run until 0 ###
    print("Homing X Axis")
    X_Motor.run_until_stalled(-move_speed, duty_limit=limit)
    X_Motor.reset_angle(0)
    print("Homing Y Axis")  
    Y_Motor.run_until_stalled(-move_speed, duty_limit=limit)
    Y_Motor.reset_angle(0)

#    Z_Motor.run_until_stalled(-move_speed,duty_limit=limit)      #uncomment this line if you want to draw the machine limits

    ### Run until Max ###
    print("Seeking X Max")
    X_Motor.run_until_stalled(move_speed, duty_limit=limit)     
    print("X Max = " + str(X_Motor.angle()))                    # print max values for callibration
    print("Seeking Y Max")
    Y_Motor.run_until_stalled(move_speed, duty_limit=limit)
    print("Y Max = " + str(Y_Motor.angle()))


main()
