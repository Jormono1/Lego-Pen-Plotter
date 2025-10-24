machine_x_range = 2289        # Upper limit of machine travel in X direction (degrees rotation)
machine_y_range = 3436        # Upper limit of machine travel in Y direction (degrees rotation)
paper_x_min = 62    # defines starting corner of paper to be written on
paper_y_min = 466
paper_x_max = 2064  # defines opposite corner of paper from min, describes full range of paper
paper_y_max = 2000
paper_x_range = paper_x_max - paper_x_min
paper_y_range = paper_y_max - paper_x_min
previous_x = 0
previous_y = 0

### Manually set this value ###
### False = using total machine capacity as described in lines 6-7 ###
### True = using index cards, dimensions as described in lines 8-13 ###
index_cards = False
if index_cards:
    X_Max = paper_x_max
    Y_Max = paper_y_max
    previous_x += paper_x_min
    previous_y += paper_y_max
else:
    X_Max = machine_x_range
    Y_Max = machine_y_range
    previous_y += Y_max

coordinates = []
scrubbed_coordinates = []
### first value is always unit width of the character, width includes a 1 unit space after character to prevent the characters from overlapping ###
### All Characters are 4 units tall ###
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
    [-1,-2,False],
    [False,False,"D"],
    [False,-2,False],
    [False,False,"U"],
    [2,False,False]],
"Z" : [5,
    [False,4,False],
    [False,False,"D"],
    [4,False,False],
    [-4,-4,False],
    [4,False,False],
    [False,False,"U"],
    [1,False,False]],
"0" : [4,
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
"1" : [3,
    [False,False,"D"],
    [2,False,False],
    [False,False,"U"],
    [-1,False,False],
    [False,False,"D"],
    [False,4,False],
    [-1,-1,False ],
    [False,False,"U"],
    [3,-3,False]],
"2" : [4,
    [3,False,False],
    [False,False,"D"],
    [-3,False,False],
    [3,3,False],
    [-1,1,False],
    [-1,False,False],
    [-1,-1,False],
    [False,False,"U"],
    [4,-3,False]],
"3" : [3,
    [False,1,False],
    [False,False,"D"],
    [1,-1,False],
    [1,1,False],
    [-1,1,False],
    [1,1,False],
    [-1,1,False],
    [-1,-1,False],
    [False,False,"U"],
    [3,-3,False]],
"4" : [3,
    [2,False,False],
    [False,False,"D"],
    [False,4,False],
    [False,False,"U"],
    [-2,False,False],
    [False,False,"D"],
    [False,-2,False],
    [2,False,False],
    [False,False,"U"],
    [1,-2,False]],
"5" : [3,
    [False,1,False],
    [False,False,"D"],
    [1,-1,False],
    [1,1,False],
    [-1,1,False],
    [-1,False,False],
    [False,2,False],
    [2,False,False],
    [False,False,"U"],
    [1,-4,False]],
"6" : [4,
    [False,1,False],
    [False,False,"D"],
    [1,1,False],
    [1,False,False],
    [1,-1,False],
    [-1,-1,False],
    [-1,False,False],
    [-1,1,False],
    [False,2,False],
    [1,1,False],
    [1,False,False],
    [1,-1,False],
    [False,False,"U"],
    [1,-3,False]],
"7" : [3,
    [2,False,False],
    [False,False,"D"],
    [False,4,False],
    [-2,False,False],
    [False,-1,False],
    [False,False,"U"],
    [3,-3,False]],
"8" : [4,
    [1,2,False],
    [False,False,"D"],
    [-1,-1,False],
    [1,-1,False],
    [1,False,False],
    [1,1,False],
    [-1,1,False],
    [1,1,False],
    [-1,1,False],
    [-1,False,False],
    [-1,-1,False],
    [1,-1,False],
    [1,False,False],
    [False,False,"U"],
    [2,-2,False]],
"9" : [3,
    [2,False,False],
    [False,False,"D"],
    [False,4,False],
    [-1,False,False],
    [-1,-1,False],
    [1,-1,False],
    [1,False,False],
    [False,False,"U"],
    [1,-2,False]],
"." : [2,
    [False,False,"D"],
    [1,False,False],
    [False,1,False],
    [-1,False,False],
    [False,-1,False],
    [False,False,"U"],
    [2,False,False]],
"!" : [1,
    [False,False,"D"],
    [False,1,False],
    [False,False,"U"],
    [False,1,False],
    [False,False,"D"],
    [False,2,False],
    [False,False,"U"],
    [1,-4,False]],
"," : [2,
    [False,False,"D"],
    [1,1,False],
    [False,False,"U"],
    [1,-1,False]],
"?" : [3,
    [1,False,False],
    [False,False,"D"],
    [False,False,"U"],
    [False,1,False],
    [False,False,"D"],
    [False,1,False],
    [1,1,False],
    [-1,1,False],
    [-1,-1,False],
    [False,False,"U"],
    [3,-3,False]],
"(" : [2,
    [1,False,False],
    [False,False,"D"],
    [-1,1,False],
    [False,2,False],
    [1,1,False],
    [False,False,"U"],
    [1,-4,False]],
")" : [2,
    [False,False,"D"],
    [1,1,False],
    [False,2,False],
    [-1,1,False],
    [False,False,"U"],
    [2,-4,False]]}

scale = 40
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
usr_input = input("Please type the text you wish to plot: ")
row_number = input("would you like to start on a lower row? if yes type the row number (first row = 1, do not use with multiple line files)")
if row_number == "":
    row_number = 1
usr_input = usr_input.upper()
txt_length = length_finder(usr_input)
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
        else:                       # if not last word now add a space instead
            if line_remaining > space_length:
                line += " "
                line_length += space_length
                line_remaining -= space_length
else:
    lines.append(usr_input)

print("plotter will draw the words in the following format:")
for line in lines:
    print(line)

output_file = input("Please type the output file name (without extension)\nmultiple lines of text will be split between multiple files starting from 0 ")
if output_file == "":    # set default file name
    output_file = "output"

### finds coordinates to start the next row ###
def starting_coordinates(text):
    global previous_x, previous_y
    starting_x = length_finder(text)
    #print("line length = " + str(starting_x))
    starting_x = X_Max - starting_x     # find the amount of unused horizontal space
    if index_cards:
        starting_x += paper_x_min
    #print("xmax - line length = " + str(starting_x))
    starting_x = int(round(starting_x / 2,0))         # divide space by 2 to center text
    #print("half of previous value = " + str(starting_x))
    previous_x = starting_x
    starting_y = previous_y - (5 * scale * int(row_number))               # 5 is because all characters defined as 4 units tall, plus 1 to prevent overlap
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

### formats coordinates to be written into output file ###
def coordinate_formatter(coords):
    if index_cards:                 # adds offset to automatically align machine to known repeatable paper position
        paper_offset = "[" + str(paper_x_min) + "," + str(paper_y_max) + ",False],\n"
        scrubbed_coordinates.append(paper_offset)
    else:
        paper_offset = "[False," + str(Y_Max) + ",False],\n"
        scrubbed_coordinates.append(paper_offset)
    for line in coords:
        if type(line[2]) == bool:
            new_line = "[" + str(line[0]) + "," + str(line[1]) + "," + str(line[2]) + "],\n"
        else:
            new_line = "[" + str(line[0]) + "," + str(line[1]) + "," + '"' + str(line[2]) + '"' + "],\n"
        scrubbed_coordinates.append(new_line)
    final_jog = "[" + str(paper_x_max) + "," + str(paper_y_max) + ",False]"
    scrubbed_coordinates.append(final_jog)

### call both coordinate generation functions ###
line_count = 0
for line in lines:
    seed_a = open("text_plotter_Seed_A.py", "r")
    seed_b = open("text_plotter_Seed_B.py", "r")
    starting_coordinates(line)
    coordinate_generator(line)
    coordinate_formatter(coordinates)
    if line_count > 0:      # don't append the 0 to all single line files, only append on multiple file outs
        output_filename = output_file + str(line_count)
    else:
        output_filename = output_file
    output_filename += ".py"
    output = open(output_filename, "w")
    line_count += 1
    output.write("#This file will write the following: " + str(line) + "\n")
    if index_cards:
        output.write("#Formatted for an index card\n")
    else:
        output.write("#Formatted for full machine capacity\n")
    for i in seed_a:  # write beginning part of file before data
        output.write(i)
    for ii in scrubbed_coordinates:
        output.write(ii)
    for iii in seed_b:
        output.write(iii)
    output.close()
    coordinates.clear()     # prevents re-writing old coordinates on new line file
    scrubbed_coordinates.clear()
