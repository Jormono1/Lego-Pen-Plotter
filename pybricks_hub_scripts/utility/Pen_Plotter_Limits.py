from pybricks.hubs import TechnicHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Direction, Port,Stop

hub = TechnicHub()
X_Motor = Motor(Port.A)
Y_Motor = Motor(Port.B, Direction.COUNTERCLOCKWISE)
Z_Motor = Motor(Port.C, Direction.COUNTERCLOCKWISE)
move_speed = 500
limit = 15

def main():
    ### Run until 0 ###
#    print("Homing Z Axis")
#    Z_Motor.run_until_stalled(-move_speed, duty_limit=limit)
#    Z_Motor.reset_angle(1)
#    Z_Motor.run_angle(move_speed,46)        # Comment this line out if you want to draw the machine limits (usefull for calibration) - See last line in main()
    print("Homing X Axis")
    X_Motor.run_until_stalled(-move_speed, duty_limit=limit)
    X_Motor.reset_angle(0)
    print("Homing Y Axis")  
    Y_Motor.run_until_stalled(-move_speed, duty_limit=limit)
    Y_Motor.reset_angle(0)

    ### Run until Max ###
    print("Seeking X Max")
    X_Motor.run_until_stalled(move_speed, duty_limit=limit)     
    print("X Max = " + str(X_Motor.angle()))                    # print max values for callibration
    print("Seeking Y Max")
    Y_Motor.run_until_stalled(move_speed, duty_limit=limit)
    print("Y Max = " + str(Y_Motor.angle()))
#    Z_Motor.run_angle(move_speed, 45)      #uncomment this line if you want to draw the machine limits

main()
