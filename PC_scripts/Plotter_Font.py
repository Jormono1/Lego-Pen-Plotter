import re
import os

seed_a = open("text_plotter_Seed_A.py", "r")
seed_b = open("text_plotter_Seed_B.py", "r")
X_Max = 2289        # Upper limit of machine travel in X direction (degrees rotation)
Y_Max = 3436        # Upper limit of machine travel in Y direction (degrees rotation)
previous_x = 0
previous_y = 0
coordinates = []
scrubbed_coordinates = []
### first value is always unit width of the letter ###
### All Letters are 4 units tall ###
### coordinates are XYZ format, Z commands ar "U" for pen up and "D" for pen down ###
font = {
" " : [2,
       [2,False,False]],
"A" : [3,
    [False,False,"D"],
    [False,3,False],
    [1,1,False],
    [1,-1,False],
    [False,-3,False],
    [False,False,"U"],
    [-2,2,False],
    [False,False,"D"],
    [2,False,False],
    [False,False,"U"],
    [1,-2,False]],
"B" : [3,
    [False,False,"D"],
    [False,4,False],
    [1,False,False],
    [1,-1,False],
    [-1,-1,False],
    [1,-1,False],
    [-1,-1,False],
    [-1,False,False],
    [False,False,"U"],
    [False,2,False],
    [False,False,"D"],
    [1,False,False],
    [False,False,"U"],
    [2,-2,False]],
"C" : [4,
    [3,1,False],
    [False,False,"D"],
    [-1,-1,False],
    [-1,False,False],
    [-1,1,False],
    [False,2,False],
    [1,1,False],
    [1,False,False],
    [1,-1,False],
    [False,False,"U"],
    [1,-3,False]],
"D" : [3,
    [False,False,"D"],
    [False,4,False],
    [1,False,False],
    [1,-1,False],
    [False,-2,False],
    [-1,-1,False],
    [-1,False,False],
    [False,False,"U"],
    [3,False,False]],
"E" : [3,
    [2,False,False],
    [False,False,"D"],
    [-2,False,False],
    [False,4,False],
    [2,False,False],
    [False,False,"U"],
    [-2,-2,False],
    [False,False,"D"],
    [1,False,False],
    [False,False,"U"],
    [2,-2,False]],
"F" : [3,
    [False,False,"D"],
    [False,4,False],
    [2,False,False],
    [False,False,"U"],
    [-2,-2,False],
    [False,False,"D"],
    [1,False,False],
    [False,False,"U"],
    [2,-2,False]],
"G" : [4,
    [2,2,False],
    [False,False,"D"],
    [1,False,False],
    [False,-1,False],
    [-1,-1,False],
    [-1,False,False],
    [-1,1,False],
    [False,2,False],
    [1,1,False],
    [1,False,False],
    [1,-1,False],
    [False,False,"U"],
    [1,-3,False]],
"H" : [3,
    [False,False,"D"],
    [False,4,False],
    [False,False,"U"],
    [2,False,False],
    [False,False,"D"],
    [False,-4,False],
    [False,False,"U"],
    [-2,2,False],
    [False,False,"D"],
    [2,False,False],
    [False,False,"U"],
    [1,-2,False]],
"I" : [3,
    [False,False,"D"],
    [2,False, False],
    [False,False,"U"],
    [-1,False,False],
    [False,False,"D"],
    [False,4,False],
    [False,False,"U"],
    [-1,False,False],
    [False,False,"D"],
    [2,False,False],
    [False,False,"U"],
    [1,-4,False]],
"J" : [4,
    [False,2,False],
    [False,False,"D"],
    [False,-1,False],
    [1,-1,False],
    [1,1,False],
    [False,3,False],
    [False,False,"U"],
    [-1,False,False],
    [False,False,"D"],
    [2,False,False],
    [False,False,"U"],
    [1,-4,False]],
"K" : [3,
    [False,False,"D"],
    [False,4,False],
    [False,False,"U"],
    [2,False,False],
    [False,False,"D"],
    [-2,-2,False],
    [2,-2,False],
    [False,False,"U"],
    [1,False,False]],
"L" : [3,
    [2,False,False],
    [False,False,"D"],
    [-2,False,False],
    [False,4,False],
    [False,False,"U"],
    [3,-4,False]],
"M" : [5,
    [False,False,"D"],
    [False,4,False],
    [2,-2,False],
    [2,2,False],
    [False,-4,False],
    [False,False,"U"],
    [1,False,False]],
"N" : [5,
    [False,False,"D"],
    [False,4,False],
    [4,-4,False],
    [False,4,False],
    [False,False,"U"],
    [1,-4,False]],
"O" : [4,
    [1,False,False],
    [False,False,"D"],
    [-1,1,False],
    [False,2,False],
    [1,1,False],
    [1,False,False],
    [1,-1,False],
    [False,-2,False],
    [-1,-1,False],
    [-1,False,False],
    [False,False,"U"],
    [3,False,False]],
"P" : [3,
    [False,False,"D"],
    [False,4,False],
    [1,False,False],
    [1,-1,False],
    [-1,-1,False],
    [-1,False,False],
    [False,False,"U"],
    [3,-2,False]],
"Q" : [4,
    [1,False,False],
    [False,False,"D"],
    [-1,1,False],
    [False,2,False],
    [1,1,False],
    [1,False,False],
    [1,-1,False],
    [False,-2,False],
    [-1,-1,False],
    [-1,False,False],
    [False,False,"U"],
    [1,1,False],
    [False,False,"D"],
    [1,-1,False],
    [False,False,"U"],
    [1,False,False]],
"R" : [3,
    [False,False,"D"],
    [False,4,False],
    [1,False,False],
    [1,-1,False],
    [-1,-1,False],
    [-1,False,False],
    [2,-2,False],
    [False,False,"U"],
    [1,False,False]],
"S" : [4,
    [False,1,False],
    [False,False,"D"],
    [1,-1,False],
    [1,False,False],
    [1,1,False],
    [-1,1,False],
    [-1,False,False],
    [-1,1,False],
    [1,1,False],
    [1,False,False],
    [1,-1,False],
    [False,False,"U"],
    [1,-3,False]],
"T" : [3,
    [1,False,False],
    [False,False,"D"],
    [False,4,False],
    [False,False,"U"],
    [-1,False,False],
    [False,False,"D"],
    [2,False,False],
    [False,False,"U"],
    [1,-4,False]],
"U" : [4,
    [False,4,False],
    [False,False,"D"],
    [False,-3,False],
    [1,-1,False],
    [1,False,False],
    [1,1,False],
    [False,3,False],
    [False,False,"U"],
    [1,-4,False]],
"V" : [5,
    [False,4,False],
    [False,False,"D"],
    [False,-2,False],
    [2,-2,False],
    [2,2,False],
    [False,2,False],
    [False,False,"U"],
    [1,-4,False]],
"W" : [5,
    [False,4,False],
    [False,False,"D"],
    [False,-4,False],
    [2,2,False],
    [2,-2,False],
    [False,4,False],
    [False,False,"U"],
    [1,-4,False]],
"X" : [5,
    [False,False,"D"],
    [4,4,False],
    [False,False,"U"],
    [-4,False,False],
    [False,False,"D"],
    [4,-4,False],
    [False,False,"U"],
    [1,False,False]],
"Y" : [3,
    [False,4,False],
    [False,False,"D"],
    [False,-1,False],
    [1,-1,False],
    [1,1,False],
    [False,1,False],
    [False,False,"U"],
    [-1,2,False],
    [False,False,"D"],
    [False,-2,False],
    [False,False,"U"],
    [2,False,False]],
"Z" :[5,
    [False,4,False],
    [False,False,"D"],
    [4,False,False],
    [-4,-4,False],
    [4,False,False],
    [False,False,"U"],
    [1,False,False]]}
### TODO: make scale a user input with default value at 4
scale = 50
scaled_font = {}
def length_finder(text):
    text_length = 0
    for i in text:
        letter = scaled_font.get(i)
        text_length += letter[0]
    return text_length

### scale data from font and put it into scaled font ###
for letter in font:
    data = font.get(letter)
    scaled_ltr = []
    width = data[0]
    scaled_ltr.append(width * scale)
    coords = data[1:]
    for c in coords:
        point = []
        x = c[0]
        y = c[1]
        z = c[2]
        if type(x) is bool:
            point.append(x)
        else:
            point.append(x * scale)
        if type(y) is bool:
            point.append(y)
        else:
            point.append(y * scale)
        point.append(z)
        scaled_ltr.append(point)
    scaled_font.update({letter: scaled_ltr})

### get text from user to be plotted ###
usr_input = input("Please type the text you wish to plot (Letters only, no numbers)")
row_number = input("would you like to start on a lower row? if yes type the row number (first row = 1, do not use with multiple line files)")
if row_number == "":
    row_number = 1
usr_input = usr_input.upper()
txt_length = length_finder(usr_input)
#print("text length = " + str(txt_length))
lines = []
line = ""
### splits user input into multiple lines as needed ###
if txt_length > X_Max:
    words = usr_input.split(" ")
    line_length = 0
    line_remaining = X_Max
    space = scaled_font.get(" ")
    space_length = space[0]
    for word in words:
        word_length = length_finder(word)
        #print("word length = " + str(word_length))
        if word_length > X_Max:     # ends loop if word is too long to fit
            print("word " + str(word) + " is too long, x Max = " + str(X_Max) + ", word length = " + str(word_length))
            break
        if word_length > line_remaining:        # if not enough room in current line, add that line to lines and clear the line for new words
            lines.append(line)
            line = ""
            line_length = 0
            line_remaining = X_Max
        line += word
        line_length += word_length
        line_remaining -= word_length
        if word == words[-1]:       # if last word in user input append the line to lines
            lines.append(line)
        else:
            if line_remaining > space_length:
                line += " "
                line_length += space_length
                line_remaining -= - space_length
else:
    lines.append(usr_input)

print("plotter will draw the words in the following format:")
for line in lines:
    print(line)

output_file = input("Please type the output file name (without extension)/nmultiple lines of text will be split between multiple files starting from 0")

### finds coordinates to start the next row ###
def starting_coordinates(text):
    global previous_x, previous_y
    starting_x = length_finder(text)
    #print("line length = " + str(starting_x))
    starting_x = X_Max - starting_x     # find the amount of unused horizontal space
    #print("xmax - line length = " + str(starting_x))
    starting_x = starting_x / 2         # divide space by 2 to center text
    #print("half of previous value = " + str(starting_x))
    previous_x = starting_x
    starting_y = (5 * scale * int(row_number)) + previous_y               # all characters defined as 4 units tall, space 5 to prevent overlap
    if starting_y > Y_Max:
        print("Cannot fit all lines in plotter, exceeding size")
    #print("previous Y = " + str(previous_y) + ", next Y = " + str(starting_y))
    previous_y = starting_y
    coordinates.append([starting_x, starting_y, False])

### populates the coordinates list from the user input ###
def coordinate_generator(text):
    global previous_x, previous_y
    for letter in text:
        data = scaled_font.get(letter)
        coords = data[1:]
        for c in coords:
            point = []
            x = c[0]
            y = c[1]
            z = c[2]
            if type(x) is bool:
                point.append(x)
            else:
                new_x = x + previous_x
                point.append(int(new_x))
                previous_x = new_x
            if type(y) is bool:
                point.append(y)
            else:
                new_y = y + previous_y
                point.append(int(new_y))
                previous_y = new_y
            point.append(z)
            coordinates.append(point)

###
def coordinate_formatter(coords):
    for line in coords:
        if type(line[2]) == bool:
            new_line = "[" + str(line[0]) + "," + str(line[1]) + "," + str(line[2]) + "],\n"
        else:
            new_line = "[" + str(line[0]) + "," + str(line[1]) + "," + '"' + str(line[2]) + '"' + "],\n"
        scrubbed_coordinates.append(new_line)
    scrubbed_coordinates.append("[1,1,False]")      # clears the gantry away from the plot automatically

### call both coordinate generation functions ###
line_count = 0
for line in lines:
    starting_coordinates(line)
    coordinate_generator(line)
    coordinate_formatter(coordinates)
    output_filename = output_file + str(line_count)
    output_filename += ".py"
    output = open(output_filename, "w")
    line_count += 1
    for line in seed_a:  # write beginning part of file before data
        output.write(line)
    for line in scrubbed_coordinates:
        output.write(line)
    for line in seed_b:
        output.write(line)
    output.close()
    coordinates.clear()     # prevents re-writing old coordinates on new line file

