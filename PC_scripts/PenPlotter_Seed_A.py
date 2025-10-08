from pybricks.hubs import TechnicHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Direction, Port, Side, Stop
from pybricks.tools import multitask, run_task

hub = TechnicHub()
X_Motor = Motor(Port.A)
Y_Motor = Motor(Port.B, Direction.COUNTERCLOCKWISE)
Z_Motor = Motor(Port.C, Direction.COUNTERCLOCKWISE)
move_speed = 300
prev_x = 0
prev_y = 0

### Coordinates are in [X, Y, Z] format ###
### False means no change, ignore ###
### Values are multiplied by 10 and rounded to make them whole numbers ###
### Float values would take up substantially more memory which is fairly limited in the hub ###
Coordinates = [
