import re
import os

file_path = "FILEPATH HERE"
file_list = []
for obj in os.listdir(file_path):       #find .txt files in the given directory
    if obj.endswith(".txt"):
        file_list.append(obj)
for index, obj in enumerate(file_list):
    print(f"{index}: {obj}")            # make a list of the eligible files
usr_input = int(input("Choose a file, type the corresponding number and press enter:"))     #user selects file from list
input_file = file_list[usr_input]       # specified file
file = open(input_file, "r")            # opens selected file
gcode = file.readlines()
partial_scrub_gcode = []
output_file = input_file[:-3] + "py"        # names new python file after original txt file
seed_a = open("PenPlotter_Seed_A.py", "r")
seed_b = open("PenPlotter_Seed_B.py", "r")
output_content = []
output = open(output_file, "w")
X = 1
Y = 1
Z = 46
previous_X = 1
previous_Y = 1
previous_Z = 46     # machine startup and homing lifts pen to prevent premature drawing, default position is up
X_Max = 2304        # Upper limit of machine travel in X direction (degrees rotation)
Y_Max = 3450        # Upper limit of machine travel in Y direction (degrees rotation)

def dim_conversion_x (length):        # dim must be in mm
    ### conversion factor is established from distance drawn as measured with a ruler and the corresponding traveled angle ###
    ### in this case I know the total range of travel in X and Y, and I know how long ###
    ### the drawn line was which corresponds to the max angle ###
    max_length = 144.4625       # X max line measurement converted from inches to mm
    conversion_factor = X_Max / max_length  # degrees/mm
    out = length * conversion_factor
    if out > X_Max:
        print("coordinate value out of range, data will be missing from output file")
        return False
    else:
        return out

def dim_conversion_y (length):        # dim must be in mm
    ### conversion factor is established from distance drawn as measured with a ruler and the corresponding traveled angle ###
    ### in this case I know the total range of travel in X and Y, and I know how long ###
    ### the drawn line was which corresponds to the max angle ###
    max_length = 144.4625       # X max line measurement converted from inches to mm
    conversion_factor = Y_Max / max_length  # degrees/mm
    out = length * conversion_factor
    if out > Y_Max:
        print("coordinate value out of range, data will be missing from output file")
        return False
    else:
        return out

for line in gcode:
    if line[0] == "G" and ("X" in line or "Y" in line or "Z" in line):      # if line is long enough to be a coordinate, and starts with G and has an X at the correct position search it for coordinates
        pattern_X = r"X([0-9.]+)"
        pattern_Y = r"Y([0-9.]+)"
        pattern_Z = r"Z([0-9.]+)"
        if "X" in line:
            X_coord = re.search(pattern_X, line)
            X_value = float(X_coord.group(1))
            X = dim_conversion_x(X_value)
            X += 1
            X = int(round(X*10, 0)) # multiply by 10 and round to 0 places to avoid float values for reasons of hub memory

        else:
            X = False

        if "Y" in line:
            Y_coord = re.search(pattern_Y, line)
            Y_value = float(Y_coord.group(1))
            Y = dim_conversion_y(Y_value)
            Y += 1
            Y = int(round(Y*10,0))

        else:
            Y = False

        if "Z" in line:
            Z_coord = re.search(pattern_Z, line)
            Z = float(Z_coord.group(1))
            if Z <=0:       # All Z output values will be either 0 or 45, down or up.
                Z = 1
            elif Z > 0:
                Z = 46

            if Z == previous_Z:        # if no functional change in Z ignore line
                Z = False
            else:
                previous_Z = Z
        else:
            Z = False
    elif "M3" or "M4" in line:      # M3 and M4 commands also mean pen up
        if Z == 46:
            Z = 1
    elif "M5" in line:      # M5 command also means pen down
        if Z == 1:
            Z = 46

    partial_scrub_gcode.append("[" + str(X) + ", " + str(Y) + ", " + str(Z) + "],\n")


for line in seed_a:                                     # write beginning part of file before data
    output.write(line)
line_counter = 0
for line in partial_scrub_gcode:                        # write data into file
    if line_counter <= 200:                             # limits what lines are written to file for reasons of size limitation
        if "0, 0, 0" not in line:
            if "1, 1, 1" not in line:
                if "False, False, False" not in line:
                    output.write(line)
                    line_counter += 1
output.write("[False, False, 46],\n[1, 1, False]]\n\n")                         # adds homing, last line of data
for line in seed_b:                                     # write functions, rest of program to file
    output.write(line)

output.close()
