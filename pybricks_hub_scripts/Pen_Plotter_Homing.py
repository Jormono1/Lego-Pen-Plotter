from pybricks.hubs import TechnicHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Direction, Port,Stop

hub = TechnicHub()
X_Motor = Motor(Port.A, gears=[12,40])
Y_Motor = Motor(Port.B, Direction.COUNTERCLOCKWISE, gears=[16,40])
Z_Motor = Motor(Port.C, Direction.COUNTERCLOCKWISE)
move_speed = 1000
limit = 15

def main():
    Z_Motor.run_until_stalled(move_speed,duty_limit=limit)                            # raise pen
    print("Homing X Axis")
    X_Motor.run_until_stalled(-move_speed, duty_limit=limit)    # run until 0
    X_Motor.reset_angle(0)
    print("Homing Y Axis")  
    Y_Motor.run_until_stalled(-move_speed, duty_limit=limit)
    Y_Motor.reset_angle(0)

main()
